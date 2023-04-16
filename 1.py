import os
import getpass

'''
test file path:
"/home/hosalikar/walnut/testfile.txt"
'''

file_path = input("Enter the path of the file you want to lock: ")
if not os.path.exists(file_path):
    print("Error: File path does not exist")
    exit()

if not os.access(file_path, os.R_OK):
    print("Error: Permission denied")
    exit()

password = getpass.getpass("Set a password to lock the file: ")

# Store the password in a file
password_file_path = os.path.join(os.path.dirname(file_path), ".locked_file_password")
with open(password_file_path, "w") as f:
    f.write(password)
    
# Change the file permissions to remove all access for all users
os.chmod(file_path, 0)

print("File locked successfully!")

