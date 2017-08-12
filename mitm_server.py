import socket
import time
from threading import Thread

server_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
clients = []

P_pkey = 11
G_pkey = 15
priv_z = 17

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):
	def __init__(self, ip, port):
		Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.req_data = -1
		print("\n[+] Connected to client : "+ ip + " : " + str(port))

	def run(self):
		while True:
			self.req_data = int.from_bytes(conn.recv(9999), byteorder='little')
			if self.req_data != 255:
				break
			print("\nClient"+str(self.port)+"request :", str(self.req_data))
			conn.send(bytes([diff_hellman()]))
			time.sleep(2)
			conn.send(bytes([255]))


def diff_hellman():
	R = (G_pkey ** priv_z) % P_pkey
	print("\nSending computation from Diffie-Hellman algorithm > R = ", R)
	return R

print("\nServer running on port : ", port)
server_skt.bind((host, port))
server_skt.listen(5)

while True:
	conn, (ip, cport) = server_skt.accept()
	client_thread = ClientThread(ip, cport)
	clients.append(client_thread)
	client_thread.start()
	for clt in clients:
		clt.join()

# server_skt.close()
# print("\nServer closed.")
