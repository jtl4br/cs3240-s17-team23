import Crypto
from Crypto.Cipher import DES3
from Crypto.Cipher import AES
from Crypto import Random

def secret_string(stringToEncrypt, publicKey):
	enc_data = publicKey.encrypt(stringToEncrypt, 32)
	return enc_data


def encrypt_file(fileName, symKey):
	iv = b"12345678"
	chunk_size = 16
	des3 = DES3.new(symKey, DES3.MODE_CFB, IV = iv)
	outFileName = fileName + '.enc'

	with open(fileName, 'rb') as file:
		with open(outFileName, 'wb') as out_file:
			while True:
				chunk = file.read(chunk_size)
				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					chunk += b' ' * (16 - len(chunk) % 16)
				out_file.write(des3.encrypt(chunk))

def decrypt_file(fileName, symKey):
	iv = b"12345678"
	chunk_size = 16
	des3 = DES3.new(symKey, DES3.MODE_CFB, IV = iv)
	outFileName = fileName
	outFileName = 'DEC_' + outFileName.replace('.enc', '')
	with open(fileName, 'rb') as file:
		with open(outFileName, 'wb') as out_file:
			while True:
				chunk = file.read(chunk_size)
				if len(chunk) == 0:
					break
				out_file.write(des3.decrypt(chunk))