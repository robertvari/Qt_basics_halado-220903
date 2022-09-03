from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton
import sys


class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Registration Form")

        main_layout = QVBoxLayout(self)
        save_user_data_bttn = QPushButton("Save User Data")


app = QApplication(sys.argv)
my_window = RegistrationForm()
my_window.show()
app.exec_()