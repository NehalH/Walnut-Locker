import os
import getpass


def validate_path(file_path):
	if not os.path.exists(file_path):
		print("Error: File path does not exist")
		exit()
		
	if os.access(file_path, os.W_OK):
		print("Error: File is already open")
		exit()
		
	# Read the stored password
	password_file_path = os.path.join(os.path.dirname(file_path), ".locked_file_password")
	with open(password_file_path, "r") as f:
		stored_password = f.read().strip()

	# Prompt the user for the password
	password = getpass.getpass("Enter the password to unlock the file: ")

	if password == stored_password:
		# Restore permissions for the owner of the file
		os.chmod(file_path, 0o700)
		print("File unlocked successfully!")
	else:
		print("Invalid password. File remains locked.")
    
file_path = input("Enter the path of the file you want to unlock: ").strip()
validate_path(file_path)

