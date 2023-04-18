import os
import getpass
from cryptography.fernet import Fernet

'''
test file path:
/home/hosalikar/walnut/testfile.txt

TODO:
-Acquire current permissions before locking
-Lock pass file
-Encryption key
- .password file

'''

def validate_path(file_path):
	
	if not os.path.exists(file_path):
		print("Error: File path does not exist")
		exit()

	if not os.access(file_path, os.R_OK):
		print("Error: Permission denied")
		exit()

def encrypt(password):

	# Generate a key for encryption, Create a Fernet object with the key, encrypt
	#key = Fernet.generate_key()
	key = b'q6IDZLj0VHEgiYtn-5jejIEbMJyUnBi5cDLlOuyC3VU='
	fernet = Fernet(key)
	return fernet.encrypt(password.encode())

def store_pass(encrypted_password):

	with open('password.txt', 'wb') as f:
    		f.write(encrypted_password)
		
def lock(file_path):

	# Change the file permissions to remove all access for all users
	os.chmod(file_path, 0)

	print("File locked successfully!")

file_path = input("Enter the path of the file you want to lock: ")
validate_path(file_path)
password = getpass.getpass("Set a password to lock the file: ")
store_pass(encrypt(password))
lock(file_path)

