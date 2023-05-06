import os
import getpass
import shelve
from cryptography.fernet import Fernet
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys
from PyQt5.QtWidgets import QApplication

def pass_dialogue():
    app = QApplication(sys.argv)
    password_dialog = QDialog()
    password_dialog.setWindowTitle("Enter Password")
    layout = QVBoxLayout()

    label = QLabel("Password:")
    layout.addWidget(label)

    password_field = QLineEdit()
    password_field.setEchoMode(QLineEdit.Password)
    layout.addWidget(password_field)

    ok_button = QPushButton("OK")
    ok_button.clicked.connect(password_dialog.accept)
    layout.addWidget(ok_button)

    cancel_button = QPushButton("Cancel")
    cancel_button.clicked.connect(password_dialog.reject)
    layout.addWidget(cancel_button)

    password_dialog.setLayout(layout)

    if password_dialog.exec_() == QDialog.Accepted:
        password = password_field.text()
        return password

    return None


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
        return None


def validate_path(file_path):
    if not os.path.exists(file_path):
        print("Error: File path does not exist")
        exit()

    if os.access(file_path, os.W_OK):
        print("Error: File is already open")
        exit()


def fetch_pass(file_path):
    with shelve.open('accesscodes.db', 'r') as ac:

        stored_password = ac.get(file_path, None)
        ### For debugging
        if stored_password:
            print(f"Access code for {file_path}: {stored_password}")
        else:
            print(f"No Access mode found for {file_path}")
    #with open("password.txt", "rb") as file:
    #    stored_password = file.read()
    return stored_password


def decrypt(encrypted_password):
    # key = getpass.getpass("Enter the decryption key: ").encode()
    key = b'q6IDZLj0VHEgiYtn-5jejIEbMJyUnBi5cDLlOuyC3VU='
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_password).decode()


def auth(password, stored_password):
    if password == stored_password:
        # Restore permissions for the owner of the file
        os.chmod(file_path, fetch_stored_perm())
        print("File unlocked successfully!")
    else:
        print("Invalid password. File remains locked.")

def fetch_stored_perm():
	
	# Fetch previous permissions for the file
    #with open("perm.txt", "r") as file:
    #    stored_perm = file.read().strip()
    with shelve.open('accessmodes.db', 'r') as am:
          
        stored_perm = am.get(file_path, None)
        ### For debugging
        if stored_perm:
            print(f"Access mode for {file_path}: {stored_perm}")
        else:
            print(f"No Access mode found for {file_path}")
    return int(stored_perm, 8)

file_path = file_dialogue()
if file_path is None:
    exit()
validate_path(file_path)
password = pass_dialogue()
if password is None:
    exit()
stored_password = decrypt(fetch_pass(file_path))
auth(password, stored_password)

