print('OTP Server')

import socket
from random import randint
from threading import Thread
from queue import Queue

s = None
clients = Queue()


def sum_of_digits(num):
	num = str(num)
	tot = 0
	for n in num:
		tot += int(n)
	return tot


def square(num):
	return num*num


def reverse(num):
	return int(''.join(reversed(str(num))))


func_list = {'hasti': sum_of_digits, 'vivek': square, 'sagar': reverse}
def create_socket():
	global s
	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	print('Socket Created')
	return


def socket_bind():
	global s
	try:
		print('Binding socket...')
		s.bind(('127.0.0.1', 12345))
		s.listen(5)
		print('Socket binded')
	except Exception as e:
		print('Socket binding error: ' + str(e))
		print('binding again')
		socket_bind()
	return



def client_handler(c):
	while True:
		try:
			c.send(bytes('Username: ', 'UTF-8'))
			cl_name = c.recv(20480).decode('UTF-8').lower()
			r = randint(100, 10000)
			c.send(bytes(str(r), 'UTF-8'))
			key = func_list[cl_name](r)
			print('Key generated:', key)
			cl_key = int(c.recv(20480).decode('UTF-8'))
			print('Key received:', cl_key)
			if key == cl_key:
				print('Access Granted!')
			else:
				print('Access Denied!')
				break
		except:
			continue


def accept_connections():
	global s
	global clients
	while True:
		try:
			c, address = s.accept()
			c.setblocking(1)
		except Exception as e:
			print('Error accepting connections: %s' % str(e))
			continue
		clients.put(c)
	return


def do_init():
	global s
	create_socket()
	socket_bind()
	accept_connections()


server_thread = Thread(target=do_init)
# server_thread.daemon = True
server_thread.start()


def otp():
	while True:
		c = clients.get()
		Thread(target=client_handler, args=(c,)).start()


multiclient_thread = Thread(target=otp)
multiclient_thread.daemon = True
multiclient_thread.start()
