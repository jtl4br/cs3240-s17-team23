import Crypto
from Crypto.Cipher import DES3
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.PublicKey import RSA

def secret_string(stringToEncrypt, publicKey):
	if not isinstance(publicKey, RSA._RSAobj):
		return False

	enc_data = publicKey.encrypt(stringToEncrypt, 32)
	print(enc_data)
	return enc_data[0]

def encrypt_file(fileName, symKey):
	iv = b"12345678"
	chunk_size = 8192
	des3 = DES3.new(symKey, DES3.MODE_CFB, IV = iv)
	outFileName = fileName + '.enc'

	try:
		with open(fileName, 'rb') as file:
			with open(outFileName, 'wb') as out_file:
				while True:
					chunk = file.read(chunk_size)
					if len(chunk) == 0:
						break
					elif len(chunk) % 16 != 0:
						chunk += b' ' * (16 - len(chunk) % 16)
					out_file.write(des3.encrypt(chunk))
		return True

	except IOError:
		print("file not found")
		return False

def decrypt_file(fileName, symKey):
	if '.enc' not in fileName:
		return False

	iv = b"12345678"
	chunk_size = 8192
	des3 = DES3.new(symKey, DES3.MODE_CFB, IV = iv)
	outFileName = fileName
	outFileName = 'DEC_' + outFileName.replace('.enc', '')

	try:
		with open(fileName, 'rb') as file:
			with open(outFileName, 'wb') as out_file:
				while True:
					chunk = file.read(chunk_size)
					if len(chunk) == 0:
						break
					out_file.write(des3.decrypt(chunk))
		return True

	except IOError:
		print("File not found")
		return False

		