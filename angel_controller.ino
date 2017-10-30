#include <SoftwareSerial.h>
#include "MsTimer2.h"

#define READ_TIME       (1000-50)  // 1.5 second
#define THRESHOLD_VALUE (20)

#define STATUS_NORMAL   (0) // tSensor == 0, pSensor == 0
#define STATUS_WARNNING (1) // tSensor == 1, pSensor == 0
#define STATUS_ERROR    (1) // tSensor == 1, pSensor == 0
#define STATUS_URGENT   (2) // tSensor == 1, pSensor == 1
// laterly it need to check time0, time1, time2

int blueTx=6;
int blueRx=7;

SoftwareSerial bluetooth(blueTx, blueRx);

int patientStatus = STATUS_NORMAL;
int tSensor = 0;
int tempSensor1 = 0;
int tempSensor2 = 0;
int tempSensor3 = 0;

bool pSensor1 = false;
bool pSensor2 = false;
bool pSensor3 = false;
bool PAST1_pSensor1 = false;
bool PAST1_pSensor2 = false;
bool PAST1_pSensor3 = false;
bool PAST2_pSensor1 = false;
bool PAST2_pSensor2 = false;
bool PAST2_pSensor3 = false;

int changedData = 0;
int tempData = 0;
int sndFirstBit = 0;
int sndSecondBit = 0;
int sndThirdBit = 0;

void setup() 
{
    //Serial.begin(9600);
    bluetooth.begin(9600);
    MsTimer2::set(READ_TIME, readSensorValue_checkStatus);
    MsTimer2::start();
}

unsigned long pastMillis = 0;
unsigned long currentMillis = 0;

void loop()
{  
    delay(READ_TIME);  

    pastMillis = millis();
    
    float changedCurrent = 0;
    float tempValue = 0;
    float chanTemper = 0;

    /* from Voltage to Current */
    //changedCurrent = (float(tSensor) + 45) / 81;
    changedCurrent = (float(tSensor) + 48) / 71;

    /* change to Temperature, it is only 17.5~40 */
    tempValue = changedCurrent*100;
    chanTemper = 17.5 + (tempValue - 900) * 0.075;
    //chanTemper = 25 + (tempValue - 1000) * 0.075;
    //Serial.print("Temperature :: ");
    //Serial.println(chanTemper);
    //Serial.print("     ");

    //screenView();  
    sendBlueTooth();
    currentMillis = millis();

    //Serial.print("time difference :: ");
    //Serial.print(currentMillis - pastMillis);
}


void screenView()
{
/*
    Serial.print("RIGHT :: ");
    if ( PAST1_pSensor1 == true )       Serial.print("ON");
    else if( PAST1_pSensor1 == false )  Serial.print("OFF");
    Serial.print("  ");     
    if ( pSensor1 == true )         Serial.print("ON");
    else if( pSensor1 == false )    Serial.print("OFF");
    Serial.print("     ");

    Serial.print("CENTER :: ");
    if ( PAST1_pSensor2 == true )       Serial.print("ON");
    else if( PAST1_pSensor2 == false )  Serial.print("OFF");
    Serial.print("  ");     
    if ( pSensor2 == true )         Serial.print("ON");
    else if( pSensor2 == false )    Serial.print("OFF");
    Serial.print("     ");

    Serial.print("LEFT :: ");
    if ( PAST1_pSensor3 == true )       Serial.print("ON");
    else if( PAST1_pSensor3 == false )  Serial.print("OFF");
    Serial.print("  ");     
    if ( pSensor3 == true )         Serial.println("ON");
    else if( pSensor3 == false )    Serial.println("OFF");

    patientStatus = checkStatus();
    //patientStatus = checkStatus1();
    Serial.print("Patient Status :: ");
    if ( patientStatus == STATUS_NORMAL )
        Serial.println("OK");
    else if ( patientStatus == STATUS_WARNNING ||  patientStatus == STATUS_ERROR )
        Serial.println("WARNNING or SYSTEM_ERROR");
    else if ( patientStatus == STATUS_URGENT )
        Serial.println("Hurry up!!");
*/
}

int checkStatus()
{
    int tempStatus = STATUS_NORMAL;

    switch(PAST1_pSensor2)
    {
        case false:
            switch(pSensor2)
            { 
                case false:  // PAST1_pSensor2==false, pSensor2==false
                    if( (PAST1_pSensor1==false) && (pSensor1==false) && (PAST1_pSensor3==false) && (pSensor3==false) )
                        tempStatus = STATUS_NORMAL;
                    else if( (PAST1_pSensor1==false) && (pSensor1==false) && (PAST1_pSensor3==false) && (pSensor3==true) )  
                        tempStatus = STATUS_URGENT;
                    else if( (PAST1_pSensor1==false) && (pSensor1==false) && (PAST1_pSensor3==true) && (pSensor3==false) )  
                        tempStatus = STATUS_URGENT;
                    else if( (PAST1_pSensor1==false) && (pSensor1==false) && (PAST1_pSensor3==true) && (pSensor3==true) )  
                        tempStatus = STATUS_URGENT;
                    else if( (PAST1_pSensor1==false) && (pSensor1==true) && (PAST1_pSensor3==false) && (pSensor3==false) )
                        tempStatus = STATUS_URGENT;
                    else if( (PAST1_pSensor1==false) && (pSensor1==true) && (PAST1_pSensor3==false) && (pSensor3==true) )  
                        tempStatus = STATUS_ERROR;
                    else if( (PAST1_pSensor1==false) && (pSensor1==true) && (PAST1_pSensor3==true) && (pSensor3==false) )  
                        tempStatus = STATUS_ERROR;
                    else if( (PAST1_pSensor1==false) && (pSensor1==true) && (PAST1_pSensor3==true) && (pSensor3==true) )  
                        tempStatus = STATUS_ERROR;

                    else if( (PAST1_pSensor1==true) && (pSensor1==false) && (PAST1_pSensor3==false) && (pSensor3==false) )
                        tempStatus = STATUS_URGENT;
                    else if( (PAST1_pSensor1==true) && (pSensor1==false) && (PAST1_pSensor3==false) && (pSensor3==true) )  
                        tempStatus = STATUS_ERROR;
                    else if( (PAST1_pSensor1==true) && (pSensor1==false) && (PAST1_pSensor3==true) && (pSensor3==false) )  
                        tempStatus = STATUS_NORMAL;
                    else if( (PAST1_pSensor1==true) && (pSensor1==false) && (PAST1_pSensor3==true) && (pSensor3==true) )  
                        tempStatus = STATUS_WARNNING;
                    
                    else if( (PAST1_pSensor1==true) && (pSensor1==true) && (PAST1_pSensor3==false) && (pSensor3==false) )
                        tempStatus = STATUS_URGENT;
                    else if( (PAST1_pSensor1==true) && (pSensor1==true) && (PAST1_pSensor3==false) && (pSensor3==true) )  
                        tempStatus = STATUS_ERROR;
                    else if( (PAST1_pSensor1==true) && (pSensor1==true) && (PAST1_pSensor3==true) && (pSensor3==false) )  
                        tempStatus = STATUS_ERROR;
                    else if( (PAST1_pSensor1==true) && (pSensor1==true) && (PAST1_pSensor3==true) && (pSensor3==true) )  
                        tempStatus = STATUS_ERROR;
                    break;
                
                case true:  // PAST1_pSensor2==false, pSensor2==true
                    if( (PAST1_pSensor1==false) && (pSensor1==false) && (PAST1_pSensor3==false) && (pSensor3==false) )
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==false) && (pSensor1==false) && (PAST1_pSensor3==false) && (pSensor3==true) )  
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==false) && (pSensor1==false) && (PAST1_pSensor3==true) && (pSensor3==false) )  
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==false) && (pSensor1==false) && (PAST1_pSensor3==true) && (pSensor3==true) )  
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==false) && (pSensor1==true) && (PAST1_pSensor3==false) && (pSensor3==false) )
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==false) && (pSensor1==true) && (PAST1_pSensor3==false) && (pSensor3==true) )  
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==false) && (pSensor1==true) && (PAST1_pSensor3==true) && (pSensor3==false) )  
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==false) && (pSensor1==true) && (PAST1_pSensor3==true) && (pSensor3==true) )  
                        tempStatus = STATUS_WARNNING;

                    else if( (PAST1_pSensor1==true) && (pSensor1==false) && (PAST1_pSensor3==false) && (pSensor3==false) )
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==true) && (pSensor1==false) && (PAST1_pSensor3==false) && (pSensor3==true) )  
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==true) && (pSensor1==false) && (PAST1_pSensor3==true) && (pSensor3==false) )  
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==true) && (pSensor1==false) && (PAST1_pSensor3==true) && (pSensor3==true) )  
                        tempStatus = STATUS_WARNNING;
                    
                    else if( (PAST1_pSensor1==true) && (pSensor1==true) && (PAST1_pSensor3==false) && (pSensor3==false) )
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==true) && (pSensor1==true) && (PAST1_pSensor3==false) && (pSensor3==true) )  
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==true) && (pSensor1==true) && (PAST1_pSensor3==true) && (pSensor3==false) )  
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==true) && (pSensor1==true) && (PAST1_pSensor3==true) && (pSensor3==true) )  
                        tempStatus = STATUS_WARNNING;
                    break;

                default:
                    break;
            }
            break;

        case true:
            switch(pSensor2)
            {
                case false:  // PAST1_pSensor2==true, pSensor2==false
                    if( (PAST1_pSensor1==false) && (pSensor1==false) && (PAST1_pSensor3==false) && (pSensor3==false) )
                        tempStatus = STATUS_NORMAL;
                    else if( (PAST1_pSensor1==false) && (pSensor1==false) && (PAST1_pSensor3==false) && (pSensor3==true) )  
                        tempStatus = STATUS_URGENT;
                    else if( (PAST1_pSensor1==false) && (pSensor1==false) && (PAST1_pSensor3==true) && (pSensor3==false) )  
                        tempStatus = STATUS_NORMAL;
                    else if( (PAST1_pSensor1==false) && (pSensor1==false) && (PAST1_pSensor3==true) && (pSensor3==true) )  
                        tempStatus = STATUS_URGENT;
                    else if( (PAST1_pSensor1==false) && (pSensor1==true) && (PAST1_pSensor3==false) && (pSensor3==false) )
                        tempStatus = STATUS_URGENT;
                    else if( (PAST1_pSensor1==false) && (pSensor1==true) && (PAST1_pSensor3==false) && (pSensor3==true) )  
                        tempStatus = STATUS_ERROR;
                    else if( (PAST1_pSensor1==false) && (pSensor1==true) && (PAST1_pSensor3==true) && (pSensor3==false) )  
                        tempStatus = STATUS_ERROR;
                    else if( (PAST1_pSensor1==false) && (pSensor1==true) && (PAST1_pSensor3==true) && (pSensor3==true) )  
                        tempStatus = STATUS_ERROR;

                    else if( (PAST1_pSensor1==true) && (pSensor1==false) && (PAST1_pSensor3==false) && (pSensor3==false) )
                        tempStatus = STATUS_URGENT;
                    else if( (PAST1_pSensor1==true) && (pSensor1==false) && (PAST1_pSensor3==false) && (pSensor3==true) )  
                        tempStatus = STATUS_ERROR;
                    else if( (PAST1_pSensor1==true) && (pSensor1==false) && (PAST1_pSensor3==true) && (pSensor3==false) )  
                        tempStatus = STATUS_NORMAL;
                    else if( (PAST1_pSensor1==true) && (pSensor1==false) && (PAST1_pSensor3==true) && (pSensor3==true) )  
                        tempStatus = STATUS_URGENT;
                    
                    else if( (PAST1_pSensor1==true) && (pSensor1==true) && (PAST1_pSensor3==false) && (pSensor3==false) )
                        tempStatus = STATUS_URGENT;
                    else if( (PAST1_pSensor1==true) && (pSensor1==true) && (PAST1_pSensor3==false) && (pSensor3==true) )  
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==true) && (pSensor1==true) && (PAST1_pSensor3==true) && (pSensor3==false) )  
                        tempStatus = STATUS_URGENT;
                    else if( (PAST1_pSensor1==true) && (pSensor1==true) && (PAST1_pSensor3==true) && (pSensor3==true) )  
                        tempStatus = STATUS_WARNNING;
                    break;

                case true:  // PAST1_pSensor2==true, pSensor2==true
                    if( (PAST1_pSensor1==false) && (pSensor1==false) && (PAST1_pSensor3==false) && (pSensor3==false) )
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==false) && (pSensor1==false) && (PAST1_pSensor3==false) && (pSensor3==true) )  
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==false) && (pSensor1==false) && (PAST1_pSensor3==true) && (pSensor3==false) )  
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==false) && (pSensor1==false) && (PAST1_pSensor3==true) && (pSensor3==true) )  
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==false) && (pSensor1==true) && (PAST1_pSensor3==false) && (pSensor3==false) )
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==false) && (pSensor1==true) && (PAST1_pSensor3==false) && (pSensor3==true) )  
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==false) && (pSensor1==true) && (PAST1_pSensor3==true) && (pSensor3==false) )  
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==false) && (pSensor1==true) && (PAST1_pSensor3==true) && (pSensor3==true) )  
                        tempStatus = STATUS_WARNNING;

                    else if( (PAST1_pSensor1==true) && (pSensor1==false) && (PAST1_pSensor3==false) && (pSensor3==false) )
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==true) && (pSensor1==false) && (PAST1_pSensor3==false) && (pSensor3==true) )  
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==true) && (pSensor1==false) && (PAST1_pSensor3==true) && (pSensor3==false) )  
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==true) && (pSensor1==false) && (PAST1_pSensor3==true) && (pSensor3==true) )  
                        tempStatus = STATUS_WARNNING;
                    
                    else if( (PAST1_pSensor1==true) && (pSensor1==true) && (PAST1_pSensor3==false) && (pSensor3==false) )
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==true) && (pSensor1==true) && (PAST1_pSensor3==false) && (pSensor3==true) )  
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==true) && (pSensor1==true) && (PAST1_pSensor3==true) && (pSensor3==false) )  
                        tempStatus = STATUS_WARNNING;
                    else if( (PAST1_pSensor1==true) && (pSensor1==true) && (PAST1_pSensor3==true) && (pSensor3==true) )  
                        tempStatus = STATUS_WARNNING;
                    break;
                
                default:
                    break;
            }
            break;
        default:
            tempStatus = STATUS_NORMAL;
            break;
    } // end of switch(PAST1_pSensor2)

    return tempStatus;
  
}

int checkStatus1()
{
    if ( pSensor1 == false &&  pSensor2 == false && pSensor3 == false ) //000
        return STATUS_NORMAL;
    else if( pSensor1 == false &&  pSensor2 == false && pSensor3 == true ) //001
        return STATUS_URGENT;
    else if( pSensor1 == false &&  pSensor2 == true && pSensor3 == false ) //010
        return STATUS_WARNNING;
    else if( pSensor1 == false &&  pSensor2 == true && pSensor3 == true ) //011
        return STATUS_WARNNING;
    else if( pSensor1 == true &&  pSensor2 == false && pSensor3 == false ) //100
        return STATUS_URGENT;
    else if( pSensor1 == true &&  pSensor2 == false && pSensor3 == true ) //101
        return STATUS_URGENT;
    else if( pSensor1 == true &&  pSensor2 == true && pSensor3 == false ) //110
        return STATUS_WARNNING;
    else if( pSensor1 == true &&  pSensor2 == true && pSensor3 == true ) //111
        return STATUS_WARNNING;
    else
        return STATUS_NORMAL;
}

void readSensorValue_checkStatus()
{
    PAST2_pSensor1 = PAST1_pSensor1;
    PAST1_pSensor1 = pSensor1;
    PAST2_pSensor2 = PAST1_pSensor2;
    PAST1_pSensor2 = pSensor2;  
    PAST2_pSensor3 = PAST1_pSensor3;
    PAST1_pSensor3 = pSensor3;

    tSensor = analogRead(A0);
  
    tempSensor1 = analogRead(A1);
    if ( tempSensor1 > THRESHOLD_VALUE )
        pSensor1 = false;
    else if( tempSensor1 <= THRESHOLD_VALUE && tempSensor1 >= 0 )
        pSensor1 = true;
  
    tempSensor2 = analogRead(A2);
    if ( tempSensor2 > THRESHOLD_VALUE )
        pSensor2 = false;
    else if( tempSensor2 <= THRESHOLD_VALUE && tempSensor2 >= 0 )
        pSensor2 = true;

    tempSensor3 = analogRead(A3);
    if ( tempSensor3 > THRESHOLD_VALUE )
        pSensor3 = false;
    else if( tempSensor3 <= THRESHOLD_VALUE && tempSensor3 >= 0 )
        pSensor3 = true;
  
    patientStatus = checkStatus();
    //patientStatus = checkStatus1();
}

void sendBlueTooth()
{

    tSensor = tSensor*10;
    changedData = tSensor / 20;

    sndFirstBit = changedData / 100;
    tempData = changedData % 100;
    sndSecondBit = tempData / 10;
    sndThirdBit = tempData % 10;

    bluetooth.print("RHIN");
    bluetooth.print(sndFirstBit);       bluetooth.print(",");
    bluetooth.print(sndSecondBit);      bluetooth.print(",");
    bluetooth.print(sndThirdBit);       bluetooth.print(",");
    bluetooth.print(PAST1_pSensor1);    bluetooth.print(",");
    bluetooth.print(pSensor1);          bluetooth.print(",");
    bluetooth.print(PAST1_pSensor2);    bluetooth.print(",");
    bluetooth.print(pSensor2);          bluetooth.print(",");
    bluetooth.print(PAST1_pSensor3);    bluetooth.print(",");
    bluetooth.print(pSensor3);          bluetooth.print(",");
    bluetooth.println(patientStatus);

}

