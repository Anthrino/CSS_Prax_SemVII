import hashlib
import socket

md5_hasher = hashlib.md5()

print("MD5 Login Credential Authenticator")

username = input("Enter username : ")
passwd = input("Enter password : ")

md5_hasher.update(username.encode('utf-8'))
user_hash = md5_hasher.hexdigest()

md5_hasher.update(username.encode('utf-8'))
pass_hash = md5_hasher.hexdigest()
