# Server Program for OTP Challenge Response System

import socket
from random import randint

server_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9000
hit_ct = 0

server_skt.bind((host, port))
server_skt.listen(5)
print("\n> OTP Authentication Server running on port", port)


# Accept and process client requests

def OTP_Gen(num):
	num = str(num)
	tot = 0
	for n in num:
		tot += int(n)
	return tot * 2


while hit_ct < 5:
	conn, (ip, cport) = server_skt.accept()
	username = conn.recv(9999).decode('UTF-8').lower()
	print('\nConnected to ' + username)
	hit_ct += 1
	r = randint(100, 10000)
	conn.send(bytes(str(r), 'UTF-8'))
	key = OTP_Gen(r)
	print('Key generated:', key)

	client_key = int(conn.recv(9999).decode('UTF-8'))
	print('Key received:', client_key)

	if key == client_key:
		print(username + ' authentication successful.')
		conn.send(bytes('authentication successful', 'UTF-8'))
	else:
		print(username + ' authentication invalid.')
		conn.send(bytes('authentication invalid', 'UTF-8'))
		break
