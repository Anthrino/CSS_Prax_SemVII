# Client Program for OTP Challenge Response System

import socket

print('\n## OTP Client ##\n')

client_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9000

client_skt.connect((host, port))

name = input('Enter username : ').lower()
client_skt.send(bytes(name, 'UTF-8'))
s_random = int((client_skt.recv(9999).decode('UTF-8')))

print('OTP received (challenge): ', s_random)
key = int(input('Enter function key: '))

client_skt.send(bytes(str(key), 'UTF-8'))

response = str(client_skt.recv(9999).decode('UTF-8'))
print(response)

