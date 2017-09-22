import socket

def OTP_fx(x):
	return

# Configure client socket and connection info
client_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9000
mode = "auth"

print("\n -- OTP Authenticator -- \n")


# Connect to authentication server
client_skt.connect((host, port))
payload = mode_hash + "/" + user_hash + "/" + pass_hash

print(payload)

# Send auth request to server with credentials
client_skt.send(payload.encode())

print("\n" + client_skt.recv(9999).decode())

print("Closing connection. Server out.")
client_skt.close()
