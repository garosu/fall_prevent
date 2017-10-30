#include <Servo.h>
#include "MsTimer2.h"

#define MY_PORT (1)

#define HALL_A  (3)
#define HALL_B  (5)
#define HALL_C  (6)

#define DIR     (9)
#define PWM     (10)

#define GEAR_RATIO (15) //14.5
//#define ONE_ROTATION  (87*4)  // 14.5*6(6step)*4(4polar)

//#define LEVEL_1 (20)
//#define MOMENT_NUMBER (0)
//#define LEVEL_1 (34)
//#define MOMENT_NUMBER (5)
#define LEVEL_1 (40)
#define LEVEL_2 (70)
#define LEVEL_3 (95)

#define MOMENT_NUMBER (13)   //  motor_1, motor_2 : 5
#define ONE_ROTATION  (87*4)  // 14.5*6(6step)*4(4polar)

//#define LEVEL_1 (45)
//#define MOMENT_NUMBER (7)

#define STATE_1 (1)   // 001 
#define STATE_2 (2)   // 011
#define STATE_3 (3)   // 010
#define STATE_4 (4)   // 110
#define STATE_5 (5)   // 100
#define STATE_6 (6)   // 101

int hallSensor_A = LOW;
int hallSensor_B = LOW;
int hallSensor_C = HIGH;

int tempOne = 0;

void setup()
{
  Serial.begin(9600);

  pinMode(HALL_A, INPUT);
  pinMode(HALL_B, INPUT);
  pinMode(HALL_C, INPUT);
  pinMode(DIR, OUTPUT);
  pinMode(PWM, OUTPUT);

  MsTimer2::set(2, checkCount);
}
  
int repeatNumber = 0;
int polarNumber = 0;

int curSPEED = 0;

int curState;
int prevState;

int i = 0;
int numRotation = 1;
char temp[100];
int rcv_leng = 0;
char cTemp=1;
int motorDirection;
int decNumber = 0;

char stopString[] = "1STOP";

unsigned int goalRotation = 1;

void loop()
{  
/*
  while( i < 100 )
  {
    Serial.println('1');
    i++;
  }
  delay(5000);
*/
/* ========================================== */  
/* check to change Hall sensor state and .... */  
/* ========================================== */  
/*
  if(sensorFlag == 1)
  {
    prevState = curState;
    curState = readHallSensor();

    if(prevState == curState)
    {
      repeatNumber++;
    }
    else
    {
      tempOne++;
      repeatNumber = 0;
    }
*/
//    if(repeatNumber == 6)
//    {
//      rotateStop();
//      sensorFlag = 0;
//      Serial.print("너무 무거워요\n");
//      // pwm value를 높인다. and check,... and check .... if max, stap the motor
//    }
/*
    if( (repeatNumber < 5) && (tempOne >= (ONE_ROTATION-MOMENT_NUMBER)*numRotation) )
    {
      Serial.print("한바퀴");
      //if( polarNumber == GEARRATIO )
      {
        rotateStop();
        polarNumber = 0;
        tempOne = 0;
        sensorFlag = 0;
      }
    }  
  }    
 */ 
/* ========================================== */  
/* check input signal and processing routine */  
/* ========================================== */  
  while(Serial.available())  
  {    
    rcv_leng = Serial.readBytes(temp, 10);
    //cTemp = Serial.read();
    //Serial.print(rcv_leng);
  }

  if( (rcv_leng > 0 ) && (temp[4] == '1') ) 
  {
    if( (temp[0]=='R') && (temp[1]=='H') && (temp[2]=='I') && (temp[3]=='N') )
    {
      rcv_leng = 0;
      int directionInt = temp[5] - '0';
      int strengthInt = temp[6] - '0';
      int rot10 = temp[7] - '0';
      int rot1 = temp[8] - '0';
      int rot0 = temp[9] - '0';

      goalRotation = rot10*ONE_ROTATION*10 + rot1*ONE_ROTATION + rot0*35;
  
      if(directionInt == 1)
      {
          rotateCW(1, strengthInt);
          MsTimer2::start();
      }
      else if(directionInt == 2)
      {
          rotateCW(0, strengthInt);
          MsTimer2::start();
      }
/*
      switch(cTemp) {
        case '1':
          rotateStop();
          break;
        case '2':
          numRotation = 1;
          rotateCW(1);
          MsTimer2::start();
          break;
        case '3':
          numRotation = 2;
          rotateCW(1);
          MsTimer2::start();
          break;
        case '4':
          numRotation = 3;
          rotateCW(1);
          MsTimer2::start();
          break;
        case '5':
          numRotation = 4;
          rotateCW(1);
          MsTimer2::start();
          break;
        case '6':
          numRotation = 1;
          rotateCW(0);
          MsTimer2::start();
          break;
        case '7':
          numRotation = 2;
          rotateCW(0);
          MsTimer2::start();
          break;
        case '8':
          numRotation = 3;
          rotateCW(0);
          MsTimer2::start();
          break;
        case '9':
          numRotation = 4;
          rotateCW(0);
          MsTimer2::start();
          break;
        default:
          //Serial.print("garosu welcome\n");
          break;
      }// end of switch */
    }// end of if(rhin...)      
  }// check length and port

}

void checkCount()
{
  int isChanged = 0;

  isChanged = readHallSensor();

  if(isChanged >= 1)
    tempOne++;

//  if( tempOne >= (ONE_ROTATION-MOMENT_NUMBER)*numRotation )
  if( tempOne >= goalRotation-MOMENT_NUMBER )
  {
    MsTimer2::stop();
    rotateStop();
    tempOne = 0;
    Serial.println('1');
  }
  
}

int readHallSensor()
{
  prevState = curState;

  hallSensor_A = digitalRead(HALL_A);
  hallSensor_B = digitalRead(HALL_B);
  hallSensor_C = digitalRead(HALL_C);

  if( hallSensor_A == LOW && hallSensor_B == LOW && hallSensor_C == HIGH )//001
    curState = STATE_1;
  else if( hallSensor_A == LOW && hallSensor_B == HIGH && hallSensor_C == HIGH )//011
    curState = STATE_2;
  else if( hallSensor_A == LOW && hallSensor_B == HIGH && hallSensor_C == LOW )//010
    curState = STATE_3;
  else if( hallSensor_A == HIGH && hallSensor_B == HIGH && hallSensor_C == LOW )//110
    curState = STATE_4;
  else if( hallSensor_A == HIGH && hallSensor_B == LOW && hallSensor_C == LOW )//100
    curState = STATE_5;
  else if( hallSensor_A == HIGH && hallSensor_B == LOW && hallSensor_C == HIGH )//101
    curState = STATE_6;
  else
    curState = STATE_1;

  //Serial.print(curState);  
  //Serial.print("\n");

  if(prevState==curState)
    return 0;
  else
    return curState;  
}

void rotateStop()
{
  analogWrite(PWM, 0);
}

void rotateCW(int Direction, int strength)
{
  if(Direction==1)
  {
    if(strength == 1)
      analogWrite(PWM, LEVEL_1);
    else if(strength == 2)
      analogWrite(PWM, LEVEL_2);
    else if(strength == 3)
      analogWrite(PWM, LEVEL_3);
    else
      analogWrite(PWM, LEVEL_1);
        
    digitalWrite(DIR, HIGH);
    delay(5);
  }
  else if(Direction==0)
  {
    if(strength == 1)
      analogWrite(PWM, LEVEL_1);
    else if(strength == 2)
      analogWrite(PWM, LEVEL_2);
    else if(strength == 3)
      analogWrite(PWM, LEVEL_3);
    else
      analogWrite(PWM, LEVEL_1);

    digitalWrite(DIR, LOW);
    delay(5);
  }
}

