print('OTP Client')

import socket

s = socket.socket()
port = 12345


def socket_connect():
    global s
    try:
        s.connect(('127.0.0.1', port))
    except Exception as e:
        print('Socket creation error ' + str(e))
        time.sleep(5)
        socket_connect()
    name = input(s.recv(20480).decode('UTF-8')).lower()
    s.send(bytes(name, 'UTF-8'))
    s_random = int((s.recv(20480).decode('UTF-8')))
    print('Random number received:', s_random)
    key = int(input('Enter key: '))
    print('Key generated:', key)
    s.send(bytes(str(key), 'UTF-8'))
    while True:
    	pass


socket_connect()
