import serial
import time
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import threading
from socket import *
from rhinRoom import *
import cPickle as pickle


tempSocket = clientConnectSocket()
serverSocket1 = tempSocket.setNumber(8901)
serverSocket2 = tempSocket.setNumber(8902)


clsFloorFive = floorStatus(5)

class fallPreventSystem(QTabWidget):
    def __init__(self, parent=None):
        super(fallPreventSystem, self).__init__(parent)

        self.widthGap = 30
        self.heightGap = 5

        self.initX = 10
        self.initY = 10
        self.initW = 105
        self.initH = 85
        self.initX1 = self.initX + self.initW*2 + self.widthGap + 150
        self.initY1 = self.initY + self.initH*3 + self.heightGap*2
        self.initW1 = 85
        self.initH1 = 105

        #self.tmrRoom501 = QTimer()
        #self.tmrRoom501.timeout.connect(self.updateStatus_501)
        #self.tmrRoom501.start(2000)

        self.setGeometry(100, 100, 780, 530)
        self.setWindowTitle("RHIN HOSPITAL :: ANGEL SYSTEM")

        self.tabThree = QWidget()
        self.tabFour = QWidget()
        self.tabFive = QWidget()
        self.tabSeven = QWidget()

        self.addTab(self.tabThree, "THREE FLOOR")
        self.addTab(self.tabFour, "FOUR FLOOR")
        self.addTab(self.tabFive, "FIVE FLOOR")
        self.addTab(self.tabSeven, "SEVEN FLOOR")
        #self.tabThreeUI()
        #self.tabFourUI()
        self.tabFiveUI()
        #self.tabSevenUI()

    def tabFiveUI(self):
        self.drawFiveRoom()

    def drawFiveRoom(self):
        self.btnRoom_Number501 = QToolButton(self.tabFive)
        self.btnRoom_Number501.setText("ROOM_501")
        self.btnRoom_Number501.setGeometry(self.initX, self.initY, self.initW, self.initH)

        self.btnRoom_Number501.clicked.connect(self.btnRoom_NumberClicked)

    def btnRoom_NumberClicked(self):
        print "button pressed"
        #global roomNumber
        #sender = self.sender()
        #if( sender.text() == "ROOM_501" ):
        #    roomNumber = 501

        #d = Dialog()
        #d.exec_()

    def updateStatus_501(self):
        str = "garosu"
        patientStatus = str.split(",")
        print'{}{}{}{}'.format('TEMPERTURE :: ', int(patientStatus[0]), '.', int(patientStatus[1]))
        strTemp = patientStatus[0] + "." + patientStatus[1]
        self.btnRoom_Number501.setText(strTemp)


def commSubController1():
    while True:
        print 'waiting for connection sub1'
        global sockForClient1, clientAddr1
        sockForClient1, clientAddr1 = serverSocket1.accept()
        print '...connected from sub1', clientAddr1

        while True:
            try:
                rcvPack = sockForClient1.recv(1024)
                if not rcvPack:
                    break
                #print rcvPack

                data_start = rcvPack.find("RHIN_")
                if (data_start != -1):
                    rcvPack = rcvPack[data_start + 5:data_start + 512]

                    data_start = rcvPack.find("FIVEONE")
                    if( data_start != -1 ):
                        tempRoomNumber = 501
                        print "ROOM NUMBER - 501"
                        tempData = rcvPack[data_start+7:data_start+73]
                        clsFloorFive.parsePackage(clsFloorFive, tempRoomNumber, tempData)
                        tempData = ""

                    data_start = rcvPack.find("FIVETWO")
                    if( data_start != -1 ):
                        tempRoomNumber = 502
                        print "ROOM NUMBER - 502"
                        tempData = rcvPack[data_start+7:data_start+73]
                        clsFloorFive.parsePackage(clsFloorFive, tempRoomNumber, tempData)
                        tempData = ""

                    data_start = rcvPack.find("FIVETHR")
                    if( data_start != -1 ):
                        tempRoomNumber = 503
                        print "ROOM NUMBER - 503"
                        tempData = rcvPack[data_start+7:data_start+73]
                        clsFloorFive.parsePackage(clsFloorFive, tempRoomNumber, tempData)
                        tempData = ""
                rcvPack = ""
                time.sleep(1.5)

            except IOError, err:
                print err.errno
                if( err.errno == 10054 ):
                    print 'forcely disconnected socket from client'
                    break
                time.sleep(5)

def commSubController2():
    while True:
        print 'waiting for connection sub2'
        global sockForClient2, clientAddr2
        sockForClient2, clientAddr2 = serverSocket2.accept()
        print '...connected from sub1', clientAddr2

        while True:
            try:
                data = sockForClient2.recv((72+12)*2)
                if not data:
                    break
                print data
                clsFloorFive.parsePackage(clsFloorFive, data)
                data = ""
                time.sleep(1.5)
            except IOError, err:
                print err.errno
                if( err.errno == 10054 ):
                    print 'forcely disconnected socket from client'
                    break
                time.sleep(5)


commSUB1 = threading.Thread(target=commSubController1)
commSUB1.start()
commSUB2 = threading.Thread(target=commSubController2)
commSUB2.start()


def main():
    app = QApplication(sys.argv)
    ex = fallPreventSystem()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()