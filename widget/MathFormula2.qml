import QtQuick 2.2
import QtQuick.Controls 2.2

ApplicationWindow {
    visible: true
    width: 360
    height: 600
    x: screen.desktopAvailableWidth - width - 12
    y: screen.desktopAvailableHeight - height - 48
    title: "HelloApp"
    
    flags: Qt.FramelessWindowHint | Qt.Window    
    
    property string currTime: "00:00:00"

    property QtObject backend
    
    Rectangle {
        anchors.fill: parent

        Image {
            sourceSize.width: parent.width
            sourceSize.height: parent.height
            source: "./003.jpg"
            fillMode: Image.PreserveAspectFit
        }
        Text {
            anchors {
                bottom: parent.bottom
                bottomMargin: 12
                left: parent.left
                leftMargin: 12
            }
            text: currTime
            font.pixelSize: 48
            color: "black"
        }    
    }
    Connections {
        target: backend        
        
        function onUpdated(msg) {
            currTime = msg;
        }
    }}