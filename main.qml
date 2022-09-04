import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtQuick.Controls.Material 2.12


ApplicationWindow{
    title: "Registration form"
    visible: true
    width: 500
    height: 300

    Material.theme: Material.Dark
    Material.accent: Material.LightBlue

    ColumnLayout{
        spacing: 10
        anchors.fill: parent
        anchors.margins: 10


        TextField{
            id: name_field
            placeholderText: "Name"
            font.pixelSize: 16
            Layout.fillWidth: true
        }

        TextField{
            id: email_field
            placeholderText: "Email"
            font.pixelSize: 16
            Layout.fillWidth: true
        }

        TextField{
            id: address_field
            placeholderText: "Address"
            font.pixelSize: 16
            Layout.fillWidth: true
        }

        TextField{
            id: phone_field
            placeholderText: "Phone: +36 20 123 4567"
            font.pixelSize: 16
            Layout.fillWidth: true
            validator: RegExpValidator{regExp:/\+\d{2} \d{2} \d{3} \d{4}/}
        }


        Button {
            text: "Save User Data"
            Layout.alignment: Qt.AlignHCenter

            onClicked: {
                if(name_field.text.length == 0){
                    print("WARNING: Name field is empty")
                    return
                }

                if(email_field.text.length == 0){
                    print("WARNING: Email field is empty")
                    return
                }

                if(address_field.text.length == 0){
                    print("WARNING: Address field is empty")
                    return
                }

                if(phone_field.text.length == 0){
                    print("WARNING: Phone field is empty")
                    return
                }

                UserDataSaver.save_data(
                    name_field.text,
                    email_field.text,
                    address_field.text,
                    phone_field.text
                )

                name_field.text = ""
                email_field.text = ""
                address_field.text = ""
                phone_field.text = ""
            }
        }
    }
}