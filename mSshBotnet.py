from pexpect import pxssh
import getpass


def connect(user, host, password):
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        # s.sendline('uptime')
        # s.prompt()
        # print(s.before)
        # s.logout()
        return s
    except pxssh.ExceptionPxssh as e:
        print('pxssh failed on login.')
        print(e)


def sendCommand(child, cmd):
    child.sendline(cmd)
    child.prompt()
    print(child.before)
    child.logout()


if __name__ == '__main__':
    host = input('hostname: ')
    user = input('username: ')
    password = getpass.getpass('password: ')
    child = connect(user, host, password)
    sendCommand(child, 'uptime')
