import os
import getpass
from cryptography.fernet import Fernet
from PyQt5.QtWidgets import QApplication, QFileDialog

'''
test file path:
/home/hosalikar/walnut/testfile.txt

TODO:
-Acquire current permissions before locking
-Lock pass file
-Encryption key
- .password file
-Dict for pass and current permissions

'''

def file_dialogue():

	# Show password dialogue
	app = QApplication([])
	file_dialog = QFileDialog()
	file_dialog.setFileMode(QFileDialog.ExistingFile)
	if file_dialog.exec_() == QFileDialog.Accepted:
		file_path = file_dialog.selectedFiles()[0]
		print(f"Selected file: {file_path}")
		return file_path
	else:
		print("File selection cancelled")

def validate_path(file_path):
	
	# Validate entered password
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
	
def store_curr_per(file_path):
	
	# Store the permissions of the file before removing them
	st = os.stat(file_path)
	oct_perm = oct(st.st_mode)
	print(oct_perm)
	with open('perm.txt', 'w') as f:
    		f.write(oct_perm)

def store_pass(encrypted_password):
	
	# Store the encrypted password
	with open('password.txt', 'wb') as f:
    		f.write(encrypted_password)
		
def lock(file_path):

	# Change the file permissions to remove all access for all users
	os.chmod(file_path, 0)
	print("File locked successfully!")

file_path = file_dialogue()
validate_path(file_path)
password = getpass.getpass("Set a password to lock the file: ")
store_curr_per(file_path)
store_pass(encrypt(password))
lock(file_path)

