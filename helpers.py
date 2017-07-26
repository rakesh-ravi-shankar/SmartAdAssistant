from Crypto.Cipher import AES
import simplejson as json
import base64
import hashlib

# Create an instance of AES cipher
def get_cipher():
	key = raw_input('Enter the passcode: ')
	key = hashlib.sha256(key.encode()).digest()
	mode = AES.MODE_CBC
	IV = 16 * '\x00'
	cipher = AES.new(key, mode, IV=IV)
	return cipher

# Chunk the data in to blocks of 16
def get_chunks(data):
	while data:
		yield data[:16]
		data = data[16:]

# Add Padding to make the data size a multiple of 16
def pad_data(data):
	while (len(data) % 16) != 0:
		data += " "
	return data

# Encrypt the file
def encrypt_file(file_path):
	cipher = get_cipher()
	encrypted_data = ""
	raw_data = pad_data(open(file_path, 'r').read())
	for chunk in get_chunks(raw_data):
		encrypted_data += cipher.encrypt(chunk)
	encrypted_data = base64.b64encode(encrypted_data)
	with open(file_path+'.encoded', 'w') as file:
		file.write(encrypted_data)

# Decrypt the file
def decrypt_file(file_path):
	cipher = get_cipher()
	encrypted_data = open(file_path, 'r').read()
	encrypted_data = base64.b64decode(encrypted_data)
	decrypted_data = ""
	for chunk in get_chunks(encrypted_data):
		decrypted_data += cipher.decrypt(chunk)
	return eval(decrypted_data.strip().decode("utf8"))
