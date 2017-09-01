import hashlib
import socket

# Configure client socket and connection info
client_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9000
mode = "auth"

print("\nMD5 Login Credential Authenticator\n")

username = input("Enter username : ")
password = input("Enter password : ")

if username == "admin" and password == "admin":
	mode = "admin"
	print("\nNew user registration :-")
	username = input("Enter username : ")
	password = input("Enter password : ")

# Obtain md5 hash checksum for credentials
mode_hash = hashlib.md5(mode.encode()).hexdigest()

user_hash = hashlib.md5(username.encode()).hexdigest()

pass_hash = hashlib.md5(password.encode()).hexdigest()

# Connect to authentication server
client_skt.connect((host, port))
payload = mode_hash + "/" + user_hash + "/" + pass_hash

print(payload)

# Send auth request to server with credentials
client_skt.send(payload.encode())

print("\n" + client_skt.recv(9999).decode())

print("Closing connection. Server out.")
client_skt.close()
