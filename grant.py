import os
import getpass
from cryptography.fernet import Fernet
from PyQt5.QtWidgets import QApplication, QFileDialog

"""
TODO:
-Encryption key

"""

def file_dialogue():

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
		os.chmod(file_path, 0o100700)
		print("File unlocked successfully!")
	else:
		print("Invalid password. File remains locked.")
    
file_path = file_dialogue()
validate_path(file_path)
password = getpass.getpass("Enter the password to unlock the file: ")
stored_password = decrypt(fetch_pass())
auth(password, stored_password)
