import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from getScreenRes import screenRes

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test")
        scrWidth, scrHeight = screenRes(app)
        self.setGeometry(100, 100, int(scrWidth / 4), int(scrHeight / 4))  # Set window geometry (x, y, width, height)

        self.label = QLabel("Wassup", self)
        self.label.setGeometry(50, 50, 200, 50)  # Set label geometry (x, y, width, height)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
