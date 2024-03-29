import os
import getpass
from cryptography.fernet import Fernet
import shelve
from gui import pathdialogue
from gui import accesscodeprompt as passprompt

'''
test file path:
/home/hosalikar/walnut/test/*

TODO:
-Lock pass file
-Encryption key
- .password file
-Accept Directories

'''

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

	with shelve.open('data/accessmodes.db', 'c') as am: # Change to 'w' for production
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
	with shelve.open('data/accesscodes.db', 'c') as ac: # Change to 'w' for production
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

file_path = pathdialogue.file_dialogue()
validate_path(file_path)
password = passprompt.setpass_prompt()
store_curr_per(file_path)
store_pass(file_path,encrypt(password))
lock(file_path)

