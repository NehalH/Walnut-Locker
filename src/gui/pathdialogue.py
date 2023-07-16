from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtWidgets import QApplication

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