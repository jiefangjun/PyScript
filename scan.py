#!/usr/bin/python

import socket
import sys
import threading
from socket import *

c = bytes(123)
screenLock = threading.Semaphore(value=1)


def connScan(tgtHost, tgtPort):
    global c
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send(c)
        results = connSkt.recv(100)
        screenLock.acquire()
        print('[+]%d/tcp open' % tgtPort)
        print('[+] ' + str(results))
        connSkt.close()
    except:
        screenLock.acquire()
        print('[-]%d/tcp closed' % tgtPort)
    finally:
        screenLock.release()
        connSkt.close()


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve '%s': Unknow host" % tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for: ' + tgtNAme[0])
    except:
        print('\n[+] Scan Results for: ' + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = threading.Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()
        #print('Scanning port ' + tgtPort)
        #connScan(tgtHost, int(tgtPort))


def main():
    tgtHost = sys.argv[1]
    tgtPorts = sys.argv[2].split(', ')
    portScan(tgtHost, tgtPorts)


if __name__ == '__main__':
    main()
