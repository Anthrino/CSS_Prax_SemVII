import hashlib

md5_hasher = hashlib.md5()

with open('cred_crypt.txt', 'rb') as cred_file:
	buf = cred_file.read()
	md5_hasher.update(buf)
print(md5_hasher.hexdigest())
