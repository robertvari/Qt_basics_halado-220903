import sys, os, json
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtGui import QGuiApplication
from PySide2.QtQuickControls2 import QQuickStyle
from PySide2.QtCore import QObject, Slot


APP_ROOT = os.path.dirname(__file__)
MAIN_QML = os.path.join(APP_ROOT, "main.qml")
QQuickStyle.setStyle("Material")


class UserDataSaver(QObject):
    @Slot(str, str, str, str)
    def save_data(self, name, email, address, phone):
        with open("user_data.json", "w") as f:
            json.dump({
                "name": name,
                "email": email,
                "address": address,
                "phone": phone
            }, f)

            print("User data saved!")


class RegistrationForm:
    def __init__(self):
        # create an instance from QGuiApplication
        self.app = QGuiApplication(sys.argv)

        # instance from QtQuick engine
        self.engine = QQmlApplicationEngine()
        self.engin_context = self.engine.rootContext()

        # insert our class into rootContext
        self.user_data_saver = UserDataSaver()
        self.engin_context.setContextProperty("UserDataSaver", self.user_data_saver)

        # load .qml file
        self.engine.load(MAIN_QML)
        
        # check if there is a root object in the QML file
        if not self.engine.rootObjects():
            sys.exit(-1)
        
        sys.exit(self.app.exec_())

RegistrationForm()