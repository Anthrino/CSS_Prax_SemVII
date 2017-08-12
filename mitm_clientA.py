import socket

client_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
index = 0
resp = ''

P_pkey = 11
G_pkey = 15
priv_x = 13


def diff_hellman(opt):
	if opt != G_pkey and opt != 255:
		print("\nRunning Diffie-Hellman on received <R3> at Client A...")
		R = (opt ** priv_x) % P_pkey
		print("\nPrivate Key <K1> : ", R)
	elif opt != 255:
		R = (G_pkey ** priv_x) % P_pkey
		print("\nDiffie-Hellman at A > R1 = ", R)
		return R


client_skt.connect((host, port))
print("\nClient", host, " - A on port : ", port)

# client_skt.send(bytes([255]))
client_skt.send(bytes([diff_hellman(G_pkey)]))
# time.sleep(2)

while resp != 255:
	# resp = client_skt.recv(port)
	resp = int.from_bytes(client_skt.recv(9999), byteorder='big')
	print("\nServer Response : ", resp)
	diff_hellman(resp)
	client_skt.send(bytes([255]))

# client_skt.close()
print("\nConnection terminated.")
