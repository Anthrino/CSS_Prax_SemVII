# Symmetric Key Ciphers

key = int(input('Enter encryption key : '))
inp_text = input('Enter your plaintext : ')
choice = int(input(
	'\nChoose encryption Method : \n1. Substitution Cipher \n2. Rail Fence Cipher \n3. Columnar Cipher \nEnter option : '))
cipher_text = ''
decryp_text = ''

if choice == 1:
	for x in inp_text:
		asc_val = ord(x)

		for i in range(key):
			asc_val += 1
			if asc_val == 58:
				asc_val = 48
			elif asc_val == 91:
				asc_val = 65
			elif asc_val == 123:
				asc_val = 97

		cipher_text += chr(asc_val)

elif choice == 2:
	rails = [''] * key
	flag, index = 1, 0

	# Encryption
	for x in inp_text:
		rails[index] += x
		index += flag
		if index == key - 1:
			flag = -1
		elif index == 0:
			flag = 1
	# print(rails)
	for x in rails:
		cipher_text += x

	# Decryption
	rails = [''] * key

	x, xdir, y, count = 0, 0, 0, 0
	# while count < len(cipher_text):
	# 	if y == key:

	# for j in range(len(
	#
	# for i in range(key):
	# 		rails[]

	decryp_text = 'Under construction'


elif choice == 3:
	columns = [''] * key
	rows = [''] * key
	index = 0

	# Encryption
	for x in inp_text:
		rows[index] += x
		index += 1
		if index == key:
			index = 0
	while index < key:
		rows[index] += '@'
		index += 1
	# print(columns)
	for x in rows:
		cipher_text += x

	# Decryption
	curr, index = 0, 0
	length = int(len(cipher_text) / key)
	for i in range(key):
		while index < length and cipher_text[curr] != '@':
			columns[index] += cipher_text[curr]
			curr += 1
			index += 1
		index = 0

	for x in columns:
		decryp_text += x

print('\nCipher Text: ' + cipher_text + '\n')
print('\nDecrypted Text: ' + decryp_text + '\n')
