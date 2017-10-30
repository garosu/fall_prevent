from socket import *


class globalVariable():
    def __init__(self):
        self.isconnectedToServer = False
        self.isconnectedToRoom1 = False
        self.isconnectedToRoom2 = False
        self.isconnectedBluetooth1 = False
        self.isconnectedBluetooth2 = False
        self.isconnectedBluetooth3 = False
        self.isconnectedBluetooth4 = False
        self.isconnectedBluetooth5 = False
        self.isconnectedBluetooth6 = False

        self.rcvData_fromCon1 = ""
        self.rcvData_fromCon2 = ""
        self.rcvData_fromCon3 = ""
        self.rcvData_fromCon4 = ""
        self.rcvData_fromCon5 = ""
        self.rcvData_fromCon6 = ""
        self.rcvData_fromMyRoom = ""
        self.rcvData_fromSubRoom1 = ""
        self.rcvData_fromSubRoom2 = ""
        self.rcvData_fromSubRoom3 = ""
        self.rcvData_fromSubRoom4 = ""
        self.rcvData_fromSubRoom5 = ""
        self.rcvData_fromSubRoom6 = ""
        self.rcvData_fromSubRoom7 = ""
        self.rcvData_fromSubRoom8 = ""
        self.sndData_toServer = ""

        self.serverSocket = ""


class clientConnectSocket():
    def __init__(self):
        self.flag = False

    def setPortNumber(self, portNumber):
        HOST = '192.168.1.31'
        TCP_PORT = portNumber
        ADDR = (HOST, TCP_PORT)

        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind(ADDR)
        serverSocket.listen(5)

        return serverSocket


class unitConStatus():
    def __init__(self):
        self.isUsed = True
        self.temperatureSensor = 0.0
        self.photoSensor1 = False
        self.photoSensor2 = False
        self.photoSensor3 = False
        self.photoSensor4 = False
        self.photoSensor5 = False

class roomStatus():
    def __init__(self, roomNumber):
        self.number = roomNumber

        self.Bed1 = unitConStatus()
        self.Bed2 = unitConStatus()
        self.Bed3 = unitConStatus()
        self.Bed4 = unitConStatus()
        self.Bed5 = unitConStatus()
        self.Bed6 = unitConStatus()

    def parseRoomData_saveData(self, roomNumber, rcvData):
        print rcvData
        data_start = rcvData.find(",ONE")
        if( data_start != -1 ):
            real_data = rcvData[data_start+4:data_start+10]
            self.saveUnitBedData(roomNumber, 1, real_data)

        data_start = rcvData.find(",TWO")
        if( data_start != -1 ):
            real_data = rcvData[data_start+4:data_start+10]
            self.saveUnitBedData(roomNumber, 2, real_data)

        data_start = rcvData.find(",THR")
        if( data_start != -1 ):
            real_data = rcvData[data_start+4:data_start+10]
            self.saveUnitBedData(roomNumber, 3, real_data)

        data_start = rcvData.find(",FOU")
        if( data_start != -1 ):
            real_data = rcvData[data_start+4:data_start+10]
            self.saveUnitBedData(roomNumber, 4, real_data)

        data_start = rcvData.find(",FIV")
        if( data_start != -1 ):
            real_data = rcvData[data_start+4:data_start+10]
            self.saveUnitBedData(roomNumber, 5, real_data)

        data_start = rcvData.find(",SIX")
        if( data_start != -1 ):
            real_data = rcvData[data_start+4:data_start+10]
            if( real_data[0] == 'e' ):
                print real_data
            else:
                self.saveUnitBedData(roomNumber, 6, real_data)


    def saveUnitBedData(self, roomNumber, conNumber, real_data):
        if( roomNumber == 501 ):
            if( conNumber == 1 ):
                statusRoom_501.Bed1.temperatureSensor = float(real_data[0])*10 + float(real_data[1]) + float(real_data[2])*0.1
                statusRoom_501.Bed1.photoSensor1 = real_data[3]
                statusRoom_501.Bed1.photoSensor2 = real_data[4]
                statusRoom_501.Bed1.photoSensor3 = real_data[5]
            elif( conNumber == 2 ):
                statusRoom_501.Bed2.temperatureSensor = float(real_data[0])*10 + float(real_data[1]) + float(real_data[2])*0.1
                statusRoom_501.Bed2.photoSensor1 = real_data[3]
                statusRoom_501.Bed2.photoSensor2 = real_data[4]
                statusRoom_501.Bed2.photoSensor3 = real_data[5]
            elif( conNumber == 3 ):
                statusRoom_501.Bed3.temperatureSensor = float(real_data[0])*10 + float(real_data[1]) + float(real_data[2])*0.1
                statusRoom_501.Bed3.photoSensor1 = real_data[3]
                statusRoom_501.Bed3.photoSensor2 = real_data[4]
                statusRoom_501.Bed3.photoSensor3 = real_data[5]
            elif( conNumber == 4 ):
                statusRoom_501.Bed4.temperatureSensor = float(real_data[0])*10 + float(real_data[1]) + float(real_data[2])*0.1
                statusRoom_501.Bed4.photoSensor1 = real_data[3]
                statusRoom_501.Bed4.photoSensor2 = real_data[4]
                statusRoom_501.Bed4.photoSensor3 = real_data[5]
            elif( conNumber == 5 ):
                statusRoom_501.Bed5.temperatureSensor = float(real_data[0])*10 + float(real_data[1]) + float(real_data[2])*0.1
                statusRoom_501.Bed5.photoSensor1 = real_data[3]
                statusRoom_501.Bed5.photoSensor2 = real_data[4]
                statusRoom_501.Bed5.photoSensor3 = real_data[5]
            elif( conNumber == 6 ):
                statusRoom_501.Bed6.temperatureSensor = float(real_data[0])*10 + float(real_data[1]) + float(real_data[2])*0.1
                statusRoom_501.Bed6.photoSensor1 = real_data[3]
                statusRoom_501.Bed6.photoSensor2 = real_data[4]
                statusRoom_501.Bed6.photoSensor3 = real_data[5]
        elif( roomNumber == 502 ):
            if( conNumber == 1 ):
                statusRoom_502.Bed1.temperatureSensor = float(real_data[0])*10 + float(real_data[1]) + float(real_data[2])*0.1
                statusRoom_502.Bed1.photoSensor1 = real_data[3]
                statusRoom_502.Bed1.photoSensor2 = real_data[4]
                statusRoom_502.Bed1.photoSensor3 = real_data[5]
            elif( conNumber == 2 ):
                statusRoom_502.Bed2.temperatureSensor = float(real_data[0])*10 + float(real_data[1]) + float(real_data[2])*0.1
                statusRoom_502.Bed2.photoSensor1 = real_data[3]
                statusRoom_502.Bed2.photoSensor2 = real_data[4]
                statusRoom_502.Bed2.photoSensor3 = real_data[5]
            elif( conNumber == 3 ):
                statusRoom_502.Bed3.temperatureSensor = float(real_data[0])*10 + float(real_data[1]) + float(real_data[2])*0.1
                statusRoom_502.Bed3.photoSensor1 = real_data[3]
                statusRoom_502.Bed3.photoSensor2 = real_data[4]
                statusRoom_502.Bed3.photoSensor3 = real_data[5]
            elif( conNumber == 4 ):
                statusRoom_502.Bed4.temperatureSensor = float(real_data[0])*10 + float(real_data[1]) + float(real_data[2])*0.1
                statusRoom_502.Bed4.photoSensor1 = real_data[3]
                statusRoom_502.Bed4.photoSensor2 = real_data[4]
                statusRoom_502.Bed4.photoSensor3 = real_data[5]
            elif( conNumber == 5 ):
                statusRoom_502.Bed5.temperatureSensor = float(real_data[0])*10 + float(real_data[1]) + float(real_data[2])*0.1
                statusRoom_502.Bed5.photoSensor1 = real_data[3]
                statusRoom_502.Bed5.photoSensor2 = real_data[4]
                statusRoom_502.Bed5.photoSensor3 = real_data[5]
            elif( conNumber == 6 ):
                statusRoom_502.Bed6.temperatureSensor = float(real_data[0])*10 + float(real_data[1]) + float(real_data[2])*0.1
                statusRoom_502.Bed6.photoSensor1 = real_data[3]
                statusRoom_502.Bed6.photoSensor2 = real_data[4]
                statusRoom_502.Bed6.photoSensor3 = real_data[5]
        elif( roomNumber == 503 ):
            if( conNumber == 1 ):
                statusRoom_503.Bed1.temperatureSensor = float(real_data[0])*10 + float(real_data[1]) + float(real_data[2])*0.1
                statusRoom_503.Bed1.photoSensor1 = real_data[3]
                statusRoom_503.Bed1.photoSensor2 = real_data[4]
                statusRoom_503.Bed1.photoSensor3 = real_data[5]
            elif( conNumber == 2 ):
                statusRoom_503.Bed2.temperatureSensor = float(real_data[0])*10 + float(real_data[1]) + float(real_data[2])*0.1
                statusRoom_503.Bed2.photoSensor1 = real_data[3]
                statusRoom_503.Bed2.photoSensor2 = real_data[4]
                statusRoom_503.Bed2.photoSensor3 = real_data[5]
            elif( conNumber == 3 ):
                statusRoom_503.Bed3.temperatureSensor = float(real_data[0])*10 + float(real_data[1]) + float(real_data[2])*0.1
                statusRoom_503.Bed3.photoSensor1 = real_data[3]
                statusRoom_503.Bed3.photoSensor2 = real_data[4]
                statusRoom_503.Bed3.photoSensor3 = real_data[5]
            elif( conNumber == 4 ):
                statusRoom_503.Bed4.temperatureSensor = float(real_data[0])*10 + float(real_data[1]) + float(real_data[2])*0.1
                statusRoom_503.Bed4.photoSensor1 = real_data[3]
                statusRoom_503.Bed4.photoSensor2 = real_data[4]
                statusRoom_503.Bed4.photoSensor3 = real_data[5]
            elif( conNumber == 5 ):
                statusRoom_503.Bed5.temperatureSensor = float(real_data[0])*10 + float(real_data[1]) + float(real_data[2])*0.1
                statusRoom_503.Bed5.photoSensor1 = real_data[3]
                statusRoom_503.Bed5.photoSensor2 = real_data[4]
                statusRoom_503.Bed5.photoSensor3 = real_data[5]
            elif( conNumber == 6 ):
                statusRoom_503.Bed6.temperatureSensor = float(real_data[0])*10 + float(real_data[1]) + float(real_data[2])*0.1
                statusRoom_503.Bed6.photoSensor1 = real_data[3]
                statusRoom_503.Bed6.photoSensor2 = real_data[4]
                statusRoom_503.Bed6.photoSensor3 = real_data[5]

globalVar = globalVariable()
statusRoom_501 = roomStatus(501)
statusRoom_502 = roomStatus(502)
statusRoom_503 = roomStatus(503)
