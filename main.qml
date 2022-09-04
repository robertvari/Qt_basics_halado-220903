import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow{
    title: "Registration form"
    visible: true
    width: 500
    height: 250

    ColumnLayout{
        spacing: 10
        anchors.fill: parent
        anchors.margins: 10


        TextField{
            placeholderText: "Name"
            font.pixelSize: 16
            Layout.fillWidth: true
        }

        TextField{
            placeholderText: "Email"
            font.pixelSize: 16
            Layout.fillWidth: true
        }

        TextField{
            placeholderText: "Address"
            font.pixelSize: 16
            Layout.fillWidth: true
        }

        Button{
            text: "Save User Data"
            Layout.alignment: Qt.AlignHCenter
        }
    }
}