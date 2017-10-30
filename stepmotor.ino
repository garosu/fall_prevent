#include <Stepper.h>
//#include "MsTimer2.h"

#define ClkPIN  (6)
#define DirPIN  (7)
#define EnvPIN  (8)
#define ONE_ROUND (4146)

#define CW_DIRECTION  (1)
#define CCW_DIRECTION  (0)

#define MAX_HEIGHT  (90)
#define BASIC_STEP  (829) // because ONE_ROUND is 5mm, then *2 means 1Cm per ONE_ROUND
#define StepPerCm   (BASIC_STEP)

const int stepsPerRevolution = 200;
Stepper myStepper(stepsPerRevolution, 6, 7);

int cur_Height = 0;
int rcv_leng = 0;
int move_Height = 0;
int num_Rotation = 0;

// RHIN + Direction + 10 + 1 + 0
char temp[7]; // RHIN + Direction + 10 + 1

void goto_initHeight();
void enableMotor();
void disableMotor();
void send_curHeight();

void setup() 
{
  Serial.begin(57600);

  pinMode(DirPIN, OUTPUT);
  pinMode(ClkPIN, OUTPUT);
  pinMode(EnvPIN, OUTPUT);
  
  //MsTimer2::set(10, checkCount);
  //myStepper.setSpeed(1800);//max
  myStepper.setSpeed(1200);  // 2second 1 round
  digitalWrite(DirPIN, LOW);
  digitalWrite(ClkPIN, HIGH);
  disableMotor();
}

void loop() 
{  
  delay(10);
  while(Serial.available())
  {
    rcv_leng = Serial.readBytes(temp, 7);

    if( (rcv_leng > 0) && ( temp[0]=='R') && ( temp[1]=='H') && ( temp[2]=='I') && ( temp[3]=='N') ) 
    {
      int Direction = temp[4];
      int rot1 = temp[5] - '0';
      int rot0= temp[6] - '0';

      move_Height = rot1*10 + rot0;
      //num_Rotation = move_Height * StepPerCm;
      enableMotor();  
      
      if( Direction == 'U' )
      {
        if( move_Height > 30 )
        {
          myStepper.step(-30*StepPerCm);
          move_Height = move_Height - 30;
          cur_Height = cur_Height + 30;
          if( move_Height > 30 )
          { 
            myStepper.step(-30*StepPerCm);
            move_Height = move_Height - 30;
            cur_Height = cur_Height + 30;
          }         
        }
        myStepper.step(-move_Height*StepPerCm);
        cur_Height = cur_Height + move_Height;
      }
      else if( Direction == 'D' )
      {
        if( move_Height > 30 )
        {
          myStepper.step(30*StepPerCm);
          move_Height = move_Height - 30;
          cur_Height = cur_Height - 30;
          if( move_Height > 30 )
          { 
            myStepper.step(30*StepPerCm);
            move_Height = move_Height - 30;
            cur_Height = cur_Height - 30;
          }         
        }
        myStepper.step(move_Height*StepPerCm);
        cur_Height = cur_Height - move_Height;
      }
      else if( Direction == 'I' )
      {
        goto_initHeight();
      }
    }

//    send_curHeight();
    delay(200);
  }
}

void send_curHeight()
{
  int send0 = cur_Height / 100;
  int x = cur_Height % 100;
  int send1 = x / 10;
  int send2 = x % 10;

  Serial.print(send0);
  Serial.print(",");  
  Serial.print(send1);
  Serial.print(",");  
  Serial.println(send2);  
}

void goto_initHeight()
{
  if( cur_Height != 0 )
  {
    enableMotor();  
    if( cur_Height > 30 )
    {
      myStepper.step(30*StepPerCm);
      cur_Height = cur_Height - 30;
      if( cur_Height > 30 )
      { 
        myStepper.step(30*StepPerCm);
        cur_Height = cur_Height - 30;
      }         
    }
    myStepper.step(cur_Height*StepPerCm);
    cur_Height = 0;
  }  
}

void enableMotor()
{
  digitalWrite(EnvPIN, HIGH);
  delay(5);    
}
void disableMotor()
{
  digitalWrite(EnvPIN, LOW);
  delay(5);    
}
