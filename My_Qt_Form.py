from PySide2.QtWidgets import QWidget, QApplication, \
    QVBoxLayout, QPushButton, QLineEdit, QMessageBox
import sys


class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Registration Form")
        self.resize(500, 0)

        # create message window
        self.message_box = QMessageBox()
        self.message_box.setIcon(QMessageBox.Critical)
        self.message_box.setWindowTitle("Error")

        # create root layout for other widgets
        main_layout = QVBoxLayout(self)

        # name field
        self.user_name = QLineEdit()
        self.user_name.setPlaceholderText("Name")
        main_layout.addWidget(self.user_name)

        # email field
        self.email_field = QLineEdit()
        self.email_field.setPlaceholderText("Email")
        main_layout.addWidget(self.email_field)

        # address field
        self.address_field = QLineEdit()
        self.address_field.setPlaceholderText("Address")
        main_layout.addWidget(self.address_field)

        # create a simple button
        self.save_user_data_bttn = QPushButton("Save User Data")

        # connect to clicked event
        self.save_user_data_bttn.clicked.connect(self.button_clicked)

        # add button to main_layout
        main_layout.addWidget(self.save_user_data_bttn)

    def button_clicked(self):
        # check empty fields
        if not self.user_name.text():
            self.message_box.setText("Name must be filled")
            self.message_box.show()
            return

        if not self.email_field.text():
            self.message_box.setText("Email must be filled")
            self.message_box.show()
            return

        if not self.address_field.text():
            self.message_box.setText("Address must be filled")
            self.message_box.show()
            return


        print(f"Hello {self.user_name.text()}")
        print(f"Email: {self.email_field.text()}")
        print(f"Address: {self.address_field.text()}")

        self.user_name.clear()
        self.email_field.clear()
        self.address_field.clear()


app = QApplication(sys.argv)
my_window = RegistrationForm()
my_window.show()
app.exec_()