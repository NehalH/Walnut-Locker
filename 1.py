import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a button and connect it to the function that runs the script
        self.button = QPushButton("Run Script", self)
        self.button.setGeometry(50, 50, 200, 50)
        self.button.clicked.connect(self.run_script)

    def run_script(self):
        # Code to run the script goes here
        print("Running script...")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

