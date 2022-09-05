from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel
from PySide2.QtGui import QFont
import sys

class TitleText(QLabel):
    def __init__(self, *args):
        super().__init__(*args)
        self.setWordWrap(True)
        self.setFont(QFont("Times", 60))

class ParagraphText(QLabel):
    def __init__(self, *args):
        super().__init__(*args)
        self.setFont(QFont("Times", 18))
        self.setWordWrap(True)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)
        title_text = TitleText("Hello World")
        main_layout.addWidget(title_text)

        paragraph = ParagraphText("When you create a QFont object you specify various attributes that you want the font to have.")
        main_layout.addWidget(paragraph)



app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()