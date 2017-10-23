from socket import *

class clientConnectSocket():
    def __init__(self):
        self.flag = False

    def setNumber(self, portNumber):
        HOST = '192.168.0.10'
        TCP_PORT = portNumber
        ADDR = (HOST, TCP_PORT)

        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind(ADDR)
        serverSocket.listen(5)

        return serverSocket

class unitConStatus():
    def __init__(self, name):
        self.isUsed = True
        self.name = name
        self.temperatureSensor = 0.0
        self.photoSensor1 = False
        self.photoSensor2 = False
        self.photoSensor3 = False
        self.photoSensor4 = False
        self.photoSensor5 = False


class roomStatus():
    def __init__(self, roomNumber):
        self.number = roomNumber
        self.isUsed = True

        self.controller1 = unitConStatus("ONE")
        self.controller2 = unitConStatus("TWO")
        self.controller3 = unitConStatus("THR")
        self.controller4 = unitConStatus("FOU")
        self.controller5 = unitConStatus("FIV")
        self.controller6 = unitConStatus("SIX")

        self.bed1_temperSensor = 0.0
        self.bed1_photoSensor1 = False
        self.bed1_photoSensor2 = False
        self.bed1_photoSensor3 = False
        self.bed1_photoSensor4 = False
        self.bed1_photoSensor5 = False

        self.bed2_temperSensor = 0.0
        self.bed2_photoSensor1 = False
        self.bed2_photoSensor2 = False
        self.bed2_photoSensor3 = False
        self.bed2_photoSensor4 = False
        self.bed2_photoSensor5 = False

        self.bed3_temperSensor = 0.0
        self.bed3_photoSensor1 = False
        self.bed3_photoSensor2 = False
        self.bed3_photoSensor3 = False
        self.bed3_photoSensor4 = False
        self.bed3_photoSensor5 = False

        self.bed4_temperSensor = 0.0
        self.bed4_photoSensor1 = False
        self.bed4_photoSensor2 = False
        self.bed4_photoSensor3 = False
        self.bed4_photoSensor4 = False
        self.bed4_photoSensor5 = False

        self.bed5_temperSensor = 0.0
        self.bed5_photoSensor1 = False
        self.bed5_photoSensor2 = False
        self.bed5_photoSensor3 = False
        self.bed5_photoSensor4 = False
        self.bed5_photoSensor5 = False

        self.bed6_temperSensor = 0.0
        self.bed6_photoSensor1 = False
        self.bed6_photoSensor2 = False
        self.bed6_photoSensor3 = False
        self.bed6_photoSensor4 = False
        self.bed6_photoSensor5 = False

class floorStatus():
    def __init__(self, floorNumber):
        self.number = floorNumber
        self.roomNumber = 0

        if(self.number == 3):
            self.room_301 = roomStatus(301)
            self.room_302 = roomStatus(302)
            self.room_303 = roomStatus(303)
            self.room_304 = roomStatus(304)
            self.room_305 = roomStatus(305)
            self.room_306 = roomStatus(306)
            self.room_307 = roomStatus(307)
            self.room_308 = roomStatus(308)
            self.room_309 = roomStatus(309)
            self.room_310 = roomStatus(310)
            self.room_311 = roomStatus(311)
            self.room_312 = roomStatus(312)
            self.room_313 = roomStatus(313)
            self.room_314 = roomStatus(314)
        elif(self.number == 4):
            self.room_401 = roomStatus(401)
            self.room_402 = roomStatus(402)
            self.room_403 = roomStatus(403)
            self.room_404 = roomStatus(404)
            self.room_405 = roomStatus(405)
            self.room_406 = roomStatus(406)
            self.room_407 = roomStatus(407)
            self.room_408 = roomStatus(408)
            self.room_409 = roomStatus(409)
            self.room_410 = roomStatus(410)
            self.room_411 = roomStatus(411)
            self.room_412 = roomStatus(412)
            self.room_413 = roomStatus(413)
            self.room_414 = roomStatus(414)
        elif(self.number == 5):
            self.room_501 = roomStatus(501)
            self.room_502 = roomStatus(502)
            self.room_503 = roomStatus(503)
            self.room_504 = roomStatus(504)
            self.room_505 = roomStatus(505)
            self.room_506 = roomStatus(506)
            self.room_507 = roomStatus(507)
            self.room_508 = roomStatus(508)
            self.room_509 = roomStatus(509)
            self.room_510 = roomStatus(510)
            self.room_511 = roomStatus(511)
            self.room_512 = roomStatus(512)
            self.room_513 = roomStatus(513)
            self.room_514 = roomStatus(514)
        elif(self.number == 7):
            self.room_701 = roomStatus(701)
            self.room_702 = roomStatus(702)
            self.room_703 = roomStatus(703)
            self.room_704 = roomStatus(704)
            self.room_705 = roomStatus(705)
            self.room_706 = roomStatus(706)
            self.room_707 = roomStatus(707)
            self.room_708 = roomStatus(708)
            self.room_709 = roomStatus(709)
            self.room_710 = roomStatus(710)
            self.room_711 = roomStatus(711)
            self.room_712 = roomStatus(712)
            self.room_713 = roomStatus(713)
            self.room_714 = roomStatus(714)
            self.room_715 = roomStatus(715)
            self.room_716 = roomStatus(716)

    def parsePackage(self, clsFloor, RoomNumber, rcvPack):

        data_start = rcvPack.find("ONE")
        if ( data_start != -1):
            Bed1 = rcvPack[data_start+3:data_start+9]
            if( Bed1[0] == 'e' ):
                print Bed1
            else:
                if( RoomNumber == 501 ):
                    clsFloor.room_501.bed1_temperSensor = float(Bed1[0])*10 + float(Bed1[1]) + float(Bed1[2])*0.1
                    clsFloor.room_501.bed1_photoSensor1 = Bed1[3]
                    clsFloor.room_501.bed1_photoSensor2 = Bed1[4]
                    clsFloor.room_501.bed1_photoSensor3 = Bed1[5]
                    print '{}{}{}{}{}{}{}{}'.format("BED_1 :: ", clsFloor.room_501.bed1_temperSensor, " ",
                                            clsFloor.room_501.bed1_photoSensor1," ",clsFloor.room_501.bed1_photoSensor2," ",clsFloor.room_501.bed1_photoSensor3)
                elif( RoomNumber == 502 ):
                    clsFloor.room_502.bed1_temperSensor = float(Bed1[0])*10 + float(Bed1[1]) + float(Bed1[2])*0.1
                    clsFloor.room_502.bed1_photoSensor1 = Bed1[3]
                    clsFloor.room_502.bed1_photoSensor2 = Bed1[4]
                    clsFloor.room_502.bed1_photoSensor3 = Bed1[5]
                    print '{}{}{}{}{}{}{}{}'.format("BED_1 :: ", clsFloor.room_502.bed1_temperSensor, " ",
                                            clsFloor.room_502.bed1_photoSensor1," ",clsFloor.room_502.bed1_photoSensor2," ",clsFloor.room_502.bed1_photoSensor3)
                elif( RoomNumber == 503 ):
                    clsFloor.room_503.bed1_temperSensor = float(Bed1[0])*10 + float(Bed1[1]) + float(Bed1[2])*0.1
                    clsFloor.room_503.bed1_photoSensor1 = Bed1[3]
                    clsFloor.room_503.bed1_photoSensor2 = Bed1[4]
                    clsFloor.room_503.bed1_photoSensor3 = Bed1[5]
                    print '{}{}{}{}{}{}{}{}'.format("BED_1 :: ", clsFloor.room_503.bed1_temperSensor, " ",
                                            clsFloor.room_503.bed1_photoSensor1," ",clsFloor.room_503.bed1_photoSensor2," ",clsFloor.room_503.bed1_photoSensor3)

        data_start = rcvPack.find("TWO")
        if ( data_start != -1):
            Bed2 = rcvPack[data_start+3:data_start+9]
            if( Bed2[0] == 'e' ):
                print Bed2
            else:
                if( RoomNumber == 501 ):
                    clsFloor.room_501.bed2_temperSensor = float(Bed2[0])*10 + float(Bed2[1]) + float(Bed2[2])*0.1
                    clsFloor.room_501.bed2_photoSensor1 = Bed2[3]
                    clsFloor.room_501.bed2_photoSensor2 = Bed2[4]
                    clsFloor.room_501.bed2_photoSensor3 = Bed2[5]
                    print '{}{}{}{}{}{}{}{}'.format("BED_2 :: ", clsFloor.room_501.bed2_temperSensor, " ",
                                            clsFloor.room_501.bed2_photoSensor1," ",clsFloor.room_501.bed2_photoSensor2," ",clsFloor.room_501.bed2_photoSensor3)
                elif( RoomNumber == 502 ):
                    clsFloor.room_502.bed2_temperSensor = float(Bed2[0])*10 + float(Bed2[1]) + float(Bed2[2])*0.1
                    clsFloor.room_502.bed2_photoSensor1 = Bed2[3]
                    clsFloor.room_502.bed2_photoSensor2 = Bed2[4]
                    clsFloor.room_502.bed2_photoSensor3 = Bed2[5]
                    print '{}{}{}{}{}{}{}{}'.format("BED_2 :: ", clsFloor.room_502.bed2_temperSensor, " ",
                                            clsFloor.room_502.bed2_photoSensor1," ",clsFloor.room_502.bed2_photoSensor2," ",clsFloor.room_502.bed2_photoSensor3)
                elif( RoomNumber == 503 ):
                    clsFloor.room_503.bed2_temperSensor = float(Bed2[0])*10 + float(Bed2[1]) + float(Bed2[2])*0.1
                    clsFloor.room_503.bed2_photoSensor1 = Bed2[3]
                    clsFloor.room_503.bed2_photoSensor2 = Bed2[4]
                    clsFloor.room_503.bed2_photoSensor3 = Bed2[5]
                    print '{}{}{}{}{}{}{}{}'.format("BED_2 :: ", clsFloor.room_503.bed2_temperSensor, " ",
                                            clsFloor.room_503.bed2_photoSensor1," ",clsFloor.room_503.bed2_photoSensor2," ",clsFloor.room_503.bed2_photoSensor3)

        data_start = rcvPack.find("THR")
        if ( data_start != -1):
            Bed3 = rcvPack[data_start+3:data_start+9]
            if( Bed3[0] == 'e' ):
                print Bed3
            else:
                if( RoomNumber == 501 ):
                    clsFloor.room_501.bed3_temperSensor = float(Bed3[0])*10 + float(Bed3[1]) + float(Bed3[2])*0.1
                    clsFloor.room_501.bed3_photoSensor1 = Bed3[3]
                    clsFloor.room_501.bed3_photoSensor2 = Bed3[4]
                    clsFloor.room_501.bed3_photoSensor3 = Bed3[5]
                    print '{}{}{}{}{}{}{}{}'.format("BED_3 :: ", clsFloor.room_501.bed3_temperSensor, " ",
                                            clsFloor.room_501.bed3_photoSensor1," ",clsFloor.room_501.bed3_photoSensor2," ",clsFloor.room_501.bed3_photoSensor3)
                elif( RoomNumber == 502 ):
                    clsFloor.room_502.bed3_temperSensor = float(Bed3[0])*10 + float(Bed3[1]) + float(Bed3[2])*0.1
                    clsFloor.room_502.bed3_photoSensor1 = Bed3[3]
                    clsFloor.room_502.bed3_photoSensor2 = Bed3[4]
                    clsFloor.room_502.bed3_photoSensor3 = Bed3[5]
                    print '{}{}{}{}{}{}{}{}'.format("BED_3 :: ", clsFloor.room_502.bed3_temperSensor, " ",
                                            clsFloor.room_502.bed3_photoSensor1," ",clsFloor.room_502.bed3_photoSensor2," ",clsFloor.room_502.bed3_photoSensor3)
                elif( RoomNumber == 503 ):
                    clsFloor.room_503.bed3_temperSensor = float(Bed3[0])*10 + float(Bed3[1]) + float(Bed3[2])*0.1
                    clsFloor.room_503.bed3_photoSensor1 = Bed3[3]
                    clsFloor.room_503.bed3_photoSensor2 = Bed3[4]
                    clsFloor.room_503.bed3_photoSensor3 = Bed3[5]
                    print '{}{}{}{}{}{}{}{}'.format("BED_3 :: ", clsFloor.room_503.bed3_temperSensor, " ",
                                            clsFloor.room_503.bed3_photoSensor1," ",clsFloor.room_503.bed3_photoSensor2," ",clsFloor.room_503.bed3_photoSensor3)

        data_start = rcvPack.find("FOU")
        if ( data_start != -1):
            Bed4 = rcvPack[data_start+3:data_start+9]
            if( Bed4[0] == 'e' ):
                print Bed4
            else:
                if( RoomNumber == 501 ):
                    clsFloor.room_501.bed4_temperSensor = float(Bed4[0])*10 + float(Bed4[1]) + float(Bed4[2])*0.1
                    clsFloor.room_501.bed4_photoSensor1 = Bed4[3]
                    clsFloor.room_501.bed4_photoSensor2 = Bed4[4]
                    clsFloor.room_501.bed4_photoSensor3 = Bed4[5]
                    print '{}{}{}{}{}{}{}{}'.format("BED_4 :: ", clsFloor.room_501.bed4_temperSensor, " ",
                                            clsFloor.room_501.bed4_photoSensor1," ",clsFloor.room_501.bed4_photoSensor2," ",clsFloor.room_501.bed4_photoSensor3)
                elif( RoomNumber == 502 ):
                    clsFloor.room_502.bed4_temperSensor = float(Bed4[0])*10 + float(Bed4[1]) + float(Bed4[2])*0.1
                    clsFloor.room_502.bed4_photoSensor1 = Bed4[3]
                    clsFloor.room_502.bed4_photoSensor2 = Bed4[4]
                    clsFloor.room_502.bed4_photoSensor3 = Bed4[5]
                    print '{}{}{}{}{}{}{}{}'.format("BED_4 :: ", clsFloor.room_502.bed4_temperSensor, " ",
                                            clsFloor.room_502.bed4_photoSensor1," ",clsFloor.room_502.bed4_photoSensor2," ",clsFloor.room_502.bed4_photoSensor3)
                elif( RoomNumber == 503 ):
                    clsFloor.room_503.bed4_temperSensor = float(Bed4[0])*10 + float(Bed4[1]) + float(Bed4[2])*0.1
                    clsFloor.room_503.bed4_photoSensor1 = Bed4[3]
                    clsFloor.room_503.bed4_photoSensor2 = Bed4[4]
                    clsFloor.room_503.bed4_photoSensor3 = Bed4[5]
                    print '{}{}{}{}{}{}{}{}'.format("BED_4 :: ", clsFloor.room_503.bed4_temperSensor, " ",
                                            clsFloor.room_503.bed4_photoSensor1," ",clsFloor.room_503.bed4_photoSensor2," ",clsFloor.room_503.bed4_photoSensor3)

        data_start = rcvPack.find("FIV")
        if ( data_start != -1):
            Bed5 = rcvPack[data_start+3:data_start+9]
            if( Bed5[0] == 'e' ):
                print Bed5
            else:
                if( RoomNumber == 501 ):
                    clsFloor.room_501.bed5_temperSensor = float(Bed5[0])*10 + float(Bed5[1]) + float(Bed5[2])*0.1
                    clsFloor.room_501.bed5_photoSensor1 = Bed5[3]
                    clsFloor.room_501.bed5_photoSensor2 = Bed5[4]
                    clsFloor.room_501.bed5_photoSensor3 = Bed5[5]
                    print '{}{}{}{}{}{}{}{}'.format("BED_5 :: ", clsFloor.room_501.bed5_temperSensor, " ",
                                            clsFloor.room_501.bed5_photoSensor1," ",clsFloor.room_501.bed5_photoSensor2," ",clsFloor.room_501.bed5_photoSensor3)
                elif( RoomNumber == 502 ):
                    clsFloor.room_502.bed5_temperSensor = float(Bed5[0])*10 + float(Bed5[1]) + float(Bed5[2])*0.1
                    clsFloor.room_502.bed5_photoSensor1 = Bed5[3]
                    clsFloor.room_502.bed5_photoSensor2 = Bed5[4]
                    clsFloor.room_502.bed5_photoSensor3 = Bed5[5]
                    print '{}{}{}{}{}{}{}{}'.format("BED_5 :: ", clsFloor.room_502.bed5_temperSensor, " ",
                                            clsFloor.room_502.bed5_photoSensor1," ",clsFloor.room_502.bed5_photoSensor2," ",clsFloor.room_502.bed5_photoSensor3)
                elif( RoomNumber == 503 ):
                    clsFloor.room_503.bed5_temperSensor = float(Bed5[0])*10 + float(Bed5[1]) + float(Bed5[2])*0.1
                    clsFloor.room_503.bed5_photoSensor1 = Bed5[3]
                    clsFloor.room_503.bed5_photoSensor2 = Bed5[4]
                    clsFloor.room_503.bed5_photoSensor3 = Bed5[5]
                    print '{}{}{}{}{}{}{}{}'.format("BED_5 :: ", clsFloor.room_503.bed5_temperSensor, " ",
                                            clsFloor.room_503.bed5_photoSensor1," ",clsFloor.room_503.bed5_photoSensor2," ",clsFloor.room_503.bed5_photoSensor3)

        data_start = rcvPack.find("SIX")
        if ( data_start != -1):
            Bed6 = rcvPack[data_start+3:data_start+9]
            if( Bed6[0] == 'e' ):
                print Bed6

                
            else:
                if( RoomNumber == 501 ):
                    clsFloor.room_501.bed6_temperSensor = float(Bed6[0])*10 + float(Bed6[1]) + float(Bed6[2])*0.1
                    clsFloor.room_501.bed6_photoSensor1 = Bed6[3]
                    clsFloor.room_501.bed6_photoSensor2 = Bed6[4]
                    clsFloor.room_501.bed6_photoSensor3 = Bed6[5]
                    print '{}{}{}{}{}{}{}{}'.format("BED_6 :: ", clsFloor.room_501.bed6_temperSensor, " ",
                                            clsFloor.room_501.bed6_photoSensor1," ",clsFloor.room_501.bed6_photoSensor2," ",clsFloor.room_501.bed6_photoSensor3)
                elif( RoomNumber == 502 ):
                    clsFloor.room_502.bed6_temperSensor = float(Bed6[0])*10 + float(Bed6[1]) + float(Bed6[2])*0.1
                    clsFloor.room_502.bed6_photoSensor1 = Bed6[3]
                    clsFloor.room_502.bed6_photoSensor2 = Bed6[4]
                    clsFloor.room_502.bed6_photoSensor3 = Bed6[5]
                    print '{}{}{}{}{}{}{}{}'.format("BED_6 :: ", clsFloor.room_502.bed6_temperSensor, " ",
                                            clsFloor.room_502.bed6_photoSensor1," ",clsFloor.room_502.bed6_photoSensor2," ",clsFloor.room_502.bed6_photoSensor3)
                elif( RoomNumber == 503 ):
                    clsFloor.room_503.bed6_temperSensor = float(Bed6[0])*10 + float(Bed6[1]) + float(Bed6[2])*0.1
                    clsFloor.room_503.bed6_photoSensor1 = Bed6[3]
                    clsFloor.room_503.bed6_photoSensor2 = Bed6[4]
                    clsFloor.room_503.bed6_photoSensor3 = Bed6[5]
                    print '{}{}{}{}{}{}{}{}'.format("BED_6 :: ", clsFloor.room_503.bed6_temperSensor, " ",
                                            clsFloor.room_503.bed6_photoSensor1," ",clsFloor.room_503.bed6_photoSensor2," ",clsFloor.room_503.bed6_photoSensor3)

