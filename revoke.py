import os
import getpass
from cryptography.fernet import Fernet
from PyQt5.QtWidgets import QApplication, QFileDialog
import shelve

'''
test file path:
/home/hosalikar/walnut/testfile.txt

TODO:
-Lock pass file
-Encryption key
- .password file
-Dict for pass and current permissions

import shelve

# Open the shelf file in read-write mode
with shelve.open('passwords.db', 'c') as db:
    # Add a new entry to the dictionary
    db['/home/user/file1.txt'] = 'password1'
    db['/home/user/file2.txt'] = 'password2'

    # Retrieve a password for a specific file path
    password = db.get('/home/user/file1.txt', None)
    if password:
        print(f"Password for /home/user/file1.txt: {password}")
    else:
        print("No password found for /home/user/file1.txt")

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
	print("Current permissions: ",oct_perm)	### For debugging

	with shelve.open('accessmodes.db', 'c') as am: # Change to 'w' for production
		# Add a new entry to the dictionary
		am[file_path] = oct_perm
  
		### For debugging
		perms = am.get(file_path, None)
		if perms:
			print(f"Access mode for {file_path}: {perms}")
		else:
			print(f"No Access mode found for {file_path}")

def store_pass(file_path,encrypted_password):
	
	# Store the encrypted password
	with shelve.open('accesscodes.db', 'c') as ac: # Change to 'w' for production
		# Add a new entry to the dictionary
		ac[file_path] = encrypted_password
  
		### For debugging
		code = ac.get(file_path, None)
		if code:
			print(f"Access code for {file_path}: {code}")
		else:
			print(f"No Access mode found for {file_path}")
		
def lock(file_path):

	# Change the file permissions to remove all access for all users
	os.chmod(file_path, 0)
	print("File locked successfully!")

file_path = file_dialogue()
validate_path(file_path)
password = getpass.getpass("Set a password to lock the file: ")
store_curr_per(file_path)
store_pass(file_path,encrypt(password))
lock(file_path)

