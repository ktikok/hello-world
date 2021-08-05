import QtQuick 2.2
import QtQuick.Controls 2.2

ApplicationWindow {
    visible: true
    width: 400
    height: 600
    x: screen.desktopAvailableWidth - width - 12
    y: screen.desktopAvailableHeight - height - 48
    title: "Clock"
    flags: Qt.FramelessWindowHint | Qt.Window
    property string currTime: "00:00:00"
    property QtObject backend

    Rectangle {
        anchors.fill: parent

        Image {
            sourceSize.width: parent.width
            sourceSize.height: parent.height
            source: "./images/background.png" srcset="https://ik.imagekit.io/mfitzp/pythonguis/tutorials/qml-qtquick-python-application/background.png?tr=w-100 100w, https://ik.imagekit.io/mfitzp/pythonguis/tutorials/qml-qtquick-python-application/background.png?tr=w-200 200w, https://ik.imagekit.io/mfitzp/pythonguis/tutorials/qml-qtquick-python-application/background.png?tr=w-400 400w, https://ik.imagekit.io/mfitzp/pythonguis/tutorials/qml-qtquick-python-application/background.png?tr=w-600 600w" loading="lazy" width="564" height="1003"
            fillMode: Image.PreserveAspectCrop
        }

        Rectangle {
            anchors.fill: parent
            color: "transparent"


            Text {
                anchors {
                    bottom: parent.bottom
                    bottomMargin: 12
                    left: parent.left
                    leftMargin: 12
                }
                text: currTime  // used to be; text: "16:38:33"
                font.pixelSize: 48
                color: "white"
            }

        }

    }

    Connections {
        target: backend

        function onUpdated(msg) {
            currTime = msg;
        }
    }

}