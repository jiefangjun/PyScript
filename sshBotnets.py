#!/usr/bin/python

from pexpect import pxssh

botNet = []

class Client:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()
    
    def connect(self):
        try:
            s = pxssh.pxss()
            s.login(self.host, self.user, self.password)
            return s
        except Exception as e:
            print(str(e))
            print('Error Connecting')

    def send_command(self, cmd):
        if not self.session:
            return '链接失败'
        self.session.sendline(cmd)
        self.session.promt()
        return self.session.before

def botnetCommand(command):
    global botNet
    for client in botNet:
        output = client.send_command(command)
        print('[*] Output form ' + client.host + ' ' + command)
        print('[+] ' + output +'\n')

def addClient(host, user, password):
    global botNet
    client = Client(host, user, password)
    botNet.append(client)

if __name__ == '__main__':
    addClient('10.0.0.110', 'root', 'toor')
    addClient('10.0.0.120', 'root', 'toor')
    addClient('10.0.0.130', 'root', 'toor')

    botnetCommand('uname -v')
    botnetCommand('cat /etc/issue')



