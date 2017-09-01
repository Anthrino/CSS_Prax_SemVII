import hashlib
import pickle
import socket

# Configure server socket and connection info
server_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9000
auth_status = ''

# Connect to port and listen to client requests
server_skt.bind((host, port))
server_skt.listen(5)
print("\nAuthentication Server running on port :", port)

# Accept and process client requests
conn, (ip, cport) = server_skt.accept()
auth_req = conn.recv(port).decode()
mode, uname, passwd = auth_req.split('/')
print(mode+"/"+uname+"/"+passwd)

# Open credentials hash file
auth_creds = pickle.load(open('auth_cred.p', 'rb'))

# Check for authentication mode
if mode == hashlib.md5("admin".encode()).hexdigest():
	# Add user in admin mode
	if uname not in auth_creds.keys():
		auth_creds[uname] = passwd
		auth_status = "User created successfully."
	else:
		auth_status = "Operation failed. Duplicate username."
	pickle.dump(auth_creds, open('auth_cred.p', 'wb'))

# Validate credentials from hash file in auth mode
elif mode == hashlib.md5("auth".encode()).hexdigest():
	if uname not in auth_creds.keys():
		auth_status = "Operation failed. Username not found."
	else:
		if passwd != auth_creds[uname]:
			auth_status = "Operation failed. Incorrect Password."
		else:
			auth_status = "Authentication successful."

# Send auth status as response to client
conn.send(auth_status.encode())

print("Closing connection.")
conn.close()
server_skt.close()
