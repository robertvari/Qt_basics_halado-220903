from PySide2.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit


class NameField(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QHBoxLayout(self)

        label = QLabel("Name:")
        main_layout.addWidget(label)

        self.text_field = QLineEdit()
        main_layout.addWidget(self.text_field)