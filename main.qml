import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow{
    title: "Registration form"
    visible: true
    width: 500
    height: 300

    ColumnLayout{
        spacing: 10
        anchors.fill: parent

        Rectangle{
            id: navbar
            color: "red"
            height: 50
            Layout.fillWidth: true

            Text{
                text: "Navbar"
                font.pixelSize: 30
                color: "white"
            }
        }

        Rectangle{
            id: content_container
            color: "blue"
            Layout.fillHeight: true
            Layout.fillWidth: true

            Text{
                text: "Content..."
                font.pixelSize: 30
                color: "white"
            }
        }

        Rectangle{
            id: footer
            color: "gray"
            height: 100
            Layout.fillWidth: true

            Text{
                text: "Footer"
                font.pixelSize: 30
                color: "white"
            }
        }

    }


    // TextField{
    //     placeholderText: "Name"
    //     font.pixelSize: 16
    // }
}