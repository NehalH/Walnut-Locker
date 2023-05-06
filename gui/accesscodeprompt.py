from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys
from PyQt5.QtWidgets import QApplication


def grant_pass_prompt():
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

def setpass_prompt():
    app = QApplication(sys.argv)
    password_dialog = QDialog()
    password_dialog.setWindowTitle("Set Password")
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