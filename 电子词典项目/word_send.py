# word_send.py
from socket import *
import os
import sys
import getpass


def main():
    if len(sys.argv) < 3:
        print('argv is error')
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except:
        print('连接服务器失败')
        return

    while True:
        print('+=====电子词典===+')
        print('|    1.注册      |')
        print('|    2.登录      |')
        print('|    3.退出      |')
        print('+================+')
        cmd = int(input('输入命令选项>>>'))
        if cmd not in [1,2,3]:
            print('请输入正确选项')
            sys.stdin.flush()#清除标准输入
            continue

        elif cmd == 1:
            r = do_register(sockfd)
            if r == 0:
                print('注册成功')
            elif r == 1:
                print('用户存在')
            else:
                print('注册失败')
        elif cmd == 2:
            name = do_login(sockfd)
            if name:
                print('登陆成功')
                login(sockfd,name)
            else:
                print('用户名和密码不正确')
        elif cmd == 3:
            sockfd.send(b'E')
            sys.exit('谢谢使用')

def do_register(sockfd):
    while True:
        username = input('请输入注册用户名:')
        password = getpass.getpass()
        password1 = getpass.getpass('Again:')
        if (' ' in username) or (' ' in password):
            print('用户名和密码不允许有空格')
        if password != password1:
            print('两次密码不一致')
            continue
        msg = 'R {} {}'.format(username,password)
        sockfd.send(msg.encode())
        data = sockfd.recv(1024).decode()
        if data == 'OK':
            return 0
        elif data == 'EXISTS':
            return 1
        else:
            return 2
def do_login(sockfd):
    name = input('请输入用户名:')
    password = getpass.getpass()
    sockfd.send('L {} {}'.format(name,password).encode())
    data = sockfd.recv(1024).decode()
    if data == 'OK':
        return name
    else:
        return
def login(sockfd,name):
    while True:
        print('+=====电子词典===+')
        print('|    1.查询单词  |')
        print('|    2.历史记录  |')
        print('|    3.退出      |')
        print('+================+')


        cmd = int(input('输入命令选项>>>'))
        if cmd not in [1,2,3]:
            print('请输入正确选项')
            sys.stdin.flush()#清除标准输入
            continue
        elif cmd == 1:
            do_query(sockfd,name)
        elif cmd == 2:
            do_hist(sockfd,name)
        elif cmd == 3:
            return

def do_query(sockfd,name):
    while True:
        word = input('单词:')
        if word == '##':
            break
        msg = 'Q {} {}'.format(name,word)
        sockfd.send(msg.encode())
        data = sockfd.recv(1024).decode()
        if data == 'OK':
            data = sockfd.recv(2048).decode()
            print(data)
        else:
            print('没有查到该单词')
def do_hist(sockfd,name):
    msg = 'H {}'.format(name)
    sockfd.send(msg.encode())
    data = sockfd.recv(128).decode()
    if data == 'OK':
        while True:
            data = sockfd.recv(1024).decode()
            if data == '##':
                break
            print(data)
    else:
        print('没有历史记录')
if __name__ == '__main__':
    main()













