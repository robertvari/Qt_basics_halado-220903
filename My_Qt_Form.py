from PySide2.QtWidgets import QWidget, QApplication, \
    QVBoxLayout, QPushButton, QLineEdit
import sys


class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Registration Form")
        self.resize(500, 500)

        # create root layout for other widgets
        main_layout = QVBoxLayout(self)

        # name field
        self.user_name = QLineEdit()
        self.user_name.setPlaceholderText("Name")
        main_layout.addWidget(self.user_name)

        # create a simple button
        self.save_user_data_bttn = QPushButton("Save User Data")

        # connect to clicked event
        self.save_user_data_bttn.clicked.connect(self.button_clicked)

        # add button to main_layout
        main_layout.addWidget(self.save_user_data_bttn)

    def button_clicked(self):
        print(f"Hello {self.user_name.text()}")


app = QApplication(sys.argv)
my_window = RegistrationForm()
my_window.show()
app.exec_()