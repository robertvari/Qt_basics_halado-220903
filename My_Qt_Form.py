from PySide2.QtWidgets import QWidget, QApplication
import sys


class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()


app = QApplication(sys.argv)
my_window = RegistrationForm()
my_window.show()
app.exec_()