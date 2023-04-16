import os
import getpass
from cryptography.fernet import Fernet

"""
TODO:
-Encryption key

"""

def validate_path(file_path):

	if not os.path.exists(file_path):
		print("Error: File path does not exist")
		exit()
		
	if os.access(file_path, os.W_OK):
		print("Error: File is already open")
		exit()
		
def fetch_pass():

	with open("password.txt", "rb") as file:
		stored_password = file.read()
	return stored_password

def decrypt(encrypted_password):

	#key = getpass.getpass("Enter the decryption key: ").encode()
	key = b'q6IDZLj0VHEgiYtn-5jejIEbMJyUnBi5cDLlOuyC3VU='
	fernet = Fernet(key)
	return fernet.decrypt(encrypted_password).decode()

def auth(password, stored_password):

	if password == stored_password:
		# Restore permissions for the owner of the file
		os.chmod(file_path, 0o700)
		print("File unlocked successfully!")
	else:
		print("Invalid password. File remains locked.")
    
file_path = input("Enter the path of the file you want to unlock: ").strip()
validate_path(file_path)
password = getpass.getpass("Enter the password to unlock the file: ")
stored_password = decrypt(fetch_pass())
auth(password, stored_password)
