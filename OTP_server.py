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
client_id = conn.recv(port).decode()
print("\nConnected to :", client_id)


# Send auth status as response to client
conn.send(auth_status.encode())

print("Closing connection.")
conn.close()
server_skt.close()
