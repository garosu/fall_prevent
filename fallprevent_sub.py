import bluetooth
import time
import sys
import datetime
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from socket import *
from protocolRHIN import *

#========= connection to CONTROLLER with BlueTooth =========
port = 1

try:
    bd_addr1 = "00:21:13:01:3C:B6"#"98:D3:37:00:8D:49"
    sock1 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock1.connect((bd_addr1, port))
    print "connected with BlueTooth1"
    globalVar.isconnectedBluetooth1 = True
except Exception as e:
    print "dont connected by BlueTooth1"
    globalVar.isconnectedBluetooth1 = False

try:
    bd_addr2 = "00:21:13:01:3A:B9"#"98:D3:31:FC:57:46"
    sock2 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock2.connect((bd_addr2, port))
    print "connected with BlueTooth2"
    globalVar.isconnectedBluetooth2 = True
except Exception as e:
    print "dont connected by BlueTooth2"
    globalVar.isconnectedBluetooth2 = False

try:
    bd_addr3 = "00:21:13:01:3C:A1"#"00:21:13:01:38:9C"
    sock3 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock3.connect((bd_addr3, port))
    print "connected with BlueTooth3"
    globalVar.isconnectedBluetooth3 = True
except Exception as e:
    print "dont connected by BlueTooth3"
    globalVar.isconnectedBluetooth3 = False

try:
    bd_addr4 = "77:77:77:77:77:77"#"00:21:13:01:38:CD"#"00:21:13:01:36:A9"
    sock4 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock4.connect((bd_addr4, port))
    print "connected with BlueTooth4"
    globalVar.isconnectedBluetooth4 = True
except Exception as e:
    print "dont connected by BlueTooth4"
    globalVar.isconnectedBluetooth4 = False

try:
    bd_addr5 = "00:21:13:01:3F:91"
    sock5 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock5.connect((bd_addr5, port))
    print "connected with BlueTooth5"
    globalVar.isconnectedBluetooth5 = True
except Exception as e:
    print "dont connected by BlueTooth5"
    globalVar.isconnectedBluetooth5 = False

try:
    bd_addr6 = "00:21:13:01:3F:81"
    sock6 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock6.connect((bd_addr6, port))
    print "connected with BlueTooth6"
    globalVar.isconnectedBluetooth6 = True
except Exception as e:
    print "dont connected by BlueTooth6"
    globalVar.isconnectedBluetooth6 = False

time.sleep(1)
#=========================================================================================

#=========================================================================================
#=========================== connection to SERVER with TCP_IP ============================
#=========================================================================================
#HOST = '192.168.1.5'
#TCP_PORT = 8901
#BUFSIZE = 1024
#ADDR = (HOST, TCP_PORT)

#globalVariable.serverSocket = socket(AF_INET, SOCK_STREAM)

#def checkServerConnection():
#    while True:
#        try:
#            if( globalVar.isconnectedToServer == False ):
#                globalVariable.serverSocket.connect(ADDR)
#                print "connected to server"
#                globalVar.isconnectedToServer = True
#                break
#        except IOError, err:
#            print '{}{}{}'.format("dont connected to server", err, errno)
#            globalVar.isconnectedToServer = False

#        time.sleep(1)


#try:
#    globalVariable.serverSocket.connect(ADDR)
#    print "connected to server"
#    globalVar.isconnectedToServer = True
#except Exception as e:
#    print "dont connected to server"
#    globalVar.isconnectedToServer = False

#===========================================================

#======== connection to SUB_CONTROLLER with TCP_IP =========
#tempSocket = clientConnectSocket()
#subServerSocket1 = tempSocket.setPortNumber(9502)
#subServerSocket2 = tempSocket.setPortNumber(9503)

#===========================================================

#=========================================================================================
#=============================== receive Data from subRoom1 ==============================
#=========================================================================================
#def rcvData_subRoom1():
#    while True:
#        print 'waiting for connection subRoom1'
#        global sockForRoom1, room1Addr
#        sockForRoom1, room1Addr = subServerSocket1.accept()
#        print '...connected from subRoom1', room1Addr

#        while True:
#            try:
#                globalVar.isconnectedToRoom1 = True
#                globalVar.rcvData_fromSubRoom1 = sockForRoom1.recv(74*2)
#                if not globalVar.rcvData_fromSubRoom1:
#                    break
#                #globalVar.rcvData_fromSubRoom1 = ""
#                time.sleep(1.5)

#            except IOError, err:
#                globalVar.isconnectedToRoom1 = False
#                print err.errno
#                if(err.errno == 10054):
#                    print 'forcely disconnected socked from client'
#                    break
#                time.sleep(5)

#=========================================================================================
#=============================== receive Data from subRoom2 ==============================
#=========================================================================================
#def rcvData_subRoom2():
#    while True:
#        print 'waiting for connection subRoom2'
#        global sockForRoom2, room2Addr
#        sockForRoom2, room2Addr = subServerSocket2.accept()
#        print '...connected from subRoom2', room2Addr

#        while True:
#            try:
#                globalVar.isconnectedToRoom2 = True
#                globalVar.rcvData_fromSubRoom2 = sockForRoom2.recv(74*2)
#                if not globalVar.rcvData_fromSubRoom2:
#                    break
                #globalVar.rcvData_fromSubRoom2 = ""
#                time.sleep(1.5)

#            except IOError, err:
#                globalVar.isconnectedToRoom2 = False
#                print err.errno
#                if(err.errno == 10054):
#                    print 'forcely disconnected socked from client'
#                    break

#                time.sleep(5)

#===============================================================================
def readDataByController(conNumber, rcvData_fromController):
    data_start = rcvData_fromController.find("RHIN")
    if data_start != -1:
        rcvData_fromController = rcvData_fromController[data_start + 4:data_start + 19 + 4]
        rcvData_fromController = rcvData_fromController.split(",")
        if (len(rcvData_fromController) == 10):
            print '{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(conNumber, " :: ",
                                                  rcvData_fromController[0], rcvData_fromController[1], ".", rcvData_fromController[2], " ",
                                                  rcvData_fromController[3], " ", rcvData_fromController[4], " ", rcvData_fromController[5], " ",
                                                  rcvData_fromController[6], " ", rcvData_fromController[7], " ", rcvData_fromController[8], " ",
                                                    rcvData_fromController[9] )
        else:
            rcvData_fromController = "0000000000"
    else:
        rcvData_fromController = "0000000000"

    strTemp = ''.join(str(e) for e in rcvData_fromController)
    strTemp = strTemp.rstrip()
    globalVar.rcvData_fromMyRoom += conNumber + strTemp + ","


def rcvMyRoomData():
    while True:
        try:
            now = datetime.datetime.now()
            print now.strftime('%Y-%m-%d %H:%M:%S')

            globalVar.rcvData_fromMyRoom = "RHIN_FIVEONE,"

            if( globalVar.isconnectedBluetooth1 == True ):
                globalVar.rcvData_fromCon1 = sock1.recv(23*2)
                readDataByController("ONE", globalVar.rcvData_fromCon1)
            else:
                globalVar.rcvData_fromMyRoom += "ONE" + "0000000000" + ","
            globalVar.rcvData_fromCon1 = ""

            if( globalVar.isconnectedBluetooth2 == True ):
                globalVar.rcvData_fromCon2 = sock2.recv(23*2)
                readDataByController("TWO", globalVar.rcvData_fromCon2)
            else:
                globalVar.rcvData_fromMyRoom += "TWO" + "0000000000" + ","
            globalVar.rcvData_fromCon2 = ""

            if( globalVar.isconnectedBluetooth3 == True ):
                globalVar.rcvData_fromCon3 = sock3.recv(23*2)
                readDataByController("THR", globalVar.rcvData_fromCon3)
            else:
                globalVar.rcvData_fromMyRoom += "THR" + "0000000000" + ","
            globalVar.rcvData_fromCon3 = ""

            if( globalVar.isconnectedBluetooth4 == True ):
                globalVar.rcvData_fromCon4 = sock4.recv(23*2)
                readDataByController("FOU", globalVar.rcvData_fromCon4)
            else:
                globalVar.rcvData_fromMyRoom += "FOU" + "0000000000" + ","
            globalVar.rcvData_fromCon4 = ""

            if( globalVar.isconnectedBluetooth5 == True ):
                globalVar.rcvData_fromCon5 = sock5.recv(23*2)
                readDataByController("FIV", globalVar.rcvData_fromCon5)
            else:
                globalVar.rcvData_fromMyRoom += "FIV" + "0000000000" + ","
            globalVar.rcvData_fromCon5 = ""

            if( globalVar.isconnectedBluetooth6 == True ):
                globalVar.rcvData_fromCon6 = sock6.recv(23*2)
                readDataByController("SIX", globalVar.rcvData_fromCon6)
            else:
                globalVar.rcvData_fromMyRoom += "SIX" + "0000000000" + ","
            globalVar.rcvData_fromCon6 = ""

            globalVar.sndData_toServer += globalVar.rcvData_fromMyRoom
            statusRoom_501.parseRoomData_saveData(501, globalVar.rcvData_fromMyRoom)
            globalVar.rcvData_fromMyRoom = ""

            if( globalVar.isconnectedToRoom1 == True ):
                strTemp = ''.join(str(e) for e in globalVar.rcvData_fromSubRoom1)
                strTemp = strTemp.rstrip()
                globalVar.rcvData_fromSubRoom1 = strTemp
                statusRoom_502.parseRoomData_saveData(502, globalVar.rcvData_fromSubRoom1)
                globalVar.sndData_toServer += globalVar.rcvData_fromSubRoom1
                globalVar.rcvData_fromSubRoom1 = ""

            if( globalVar.isconnectedToRoom2 == True ):
                strTemp = ''.join(str(e) for e in globalVar.rcvData_fromSubRoom2)
                strTemp = strTemp.rstrip()
                globalVar.rcvData_fromSubRoom2 = strTemp
                statusRoom_503.parseRoomData_saveData(503, globalVar.rcvData_fromSubRoom2)
                globalVar.sndData_toServer += globalVar.rcvData_fromSubRoom2
                globalVar.rcvData_fromSubRoom1 = ""

            if( globalVar.isconnectedToServer == True ):
                globalVariable.serverSocket.send(globalVar.sndData_toServer)

            globalVar.sndData_toServer = ""

        except KeyboardInterrupt:
            break

        time.sleep(1)

    if (globalVar.isconnectedBluetooth1 == True):
        sock1.close()
    if (globalVar.isconnectedBluetooth2 == True):
        sock2.close()
    if (globalVar.isconnectedBluetooth3 == True):
        sock3.close()
    if (globalVar.isconnectedBluetooth4 == True):
        sock4.close()
    if (globalVar.isconnectedBluetooth5 == True):
        sock5.close()
    if (globalVar.isconnectedBluetooth6 == True):
        sock6.close()


#commThread2 = threading.Thread(target=rcvData_subRoom1)
#commThread2.start()
#commThread3 = threading.Thread(target=rcvData_subRoom2)
#commThread3.start()
commThread1 = threading.Thread(target=rcvMyRoomData)
commThread1.start()
#commThread4 = threading.Thread(target=checkServerConnection)
#commThread4.start()


class rhinAngelSystem(QMainWindow):
    def __init__(self, parent=None):
        super(rhinAngelSystem, self).__init__()

        self.initUI()

        #self.tmrRoom501 = QTimer()
        #self.tmrRoom501.timeout.connect(self.updataStatus_Room501)
        #self.tmrRoom501.start(3000)

        #self.tmrRoom502 = QTimer()
        #self.tmrRoom502.timeout.connect(self.updataStatus_Room502)
        #self.tmrRoom502.start(1500)

    def initUI(self):
        self.statusBar().showMessage('Ready')
        self.setGeometry(50, 50, 400, 200)
        self.setWindowTitle("RHIN HOSPITAL :: ANGEL SYSTEM")

        self.btnStatusCon1 = QToolButton(self)
        self.btnStatusCon1.setGeometry(0,0,100,30)
        self.btnStatusCon2 = QToolButton(self)
        self.btnStatusCon2.setGeometry(0,0+40*1,100,30)
        self.btnStatusCon3 = QToolButton(self)
        self.btnStatusCon3.setGeometry(0,0+40*2,100,30)

#        self.btnStatusCon1.clicked.connect(self.btnStatus_Clicked)

#    def updataStatus_Room501(self):
#        print "update 501 room"

#    def updataStatus_Room502(self):
#        if( statusRoom_502.Bed5.temperatureSensor > 30 ):
#            self.btnStatusCon2.setStyleSheet("background-color: white")
#            self.btnStatusCon2.setText(str(statusRoom_502.Bed5.temperatureSensor))
#        elif( statusRoom_502.Bed5.temperatureSensor <= 30 and statusRoom_502.Bed5.temperatureSensor > 15 ):
#            self.btnStatusCon2.setStyleSheet("background-color: yellow")
#            self.btnStatusCon2.setText(str(statusRoom_502.Bed5.temperatureSensor))
#        elif( statusRoom_502.Bed5.temperatureSensor <= 15 ):
#            self.btnStatusCon2.setStyleSheet("background-color: red")
#            self.btnStatusCon2.setText(str(statusRoom_502.Bed5.temperatureSensor))


#    def btnStatus_Clicked(self):
#        print "press the button"
#        self.btnStatusCon1.setStyleSheet("background-color: white")


def main():
    app = QApplication(sys.argv)
    ex = rhinAngelSystem()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
