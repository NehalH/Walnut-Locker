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


password = getpass.getpass("Enter a password to lock the file: ")

# Change the file permissions to remove all access for all users
os.chmod(file_path, 0)

