from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton
import sys


class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Registration Form")

        # create root layout for other widgets
        main_layout = QVBoxLayout(self)

        # create a simple button
        save_user_data_bttn = QPushButton("Save User Data")

        # add button to main_layout
        main_layout.addWidget(save_user_data_bttn)


app = QApplication(sys.argv)
my_window = RegistrationForm()
my_window.show()
app.exec_()