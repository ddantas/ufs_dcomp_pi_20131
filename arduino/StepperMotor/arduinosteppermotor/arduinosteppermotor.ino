#include <Stepper.h>

#define INX 6
#define INY 5
#define LEDX 3
#define LEDY 4

const int stepsPerRevolution = 64;
Stepper myStepperX(stepsPerRevolution, 11,9,10,8); 
Stepper myStepperY(stepsPerRevolution, 6,4,5,3); 

int buttonx = 0;
int buttony = 0;

void setup() {
  myStepperX.setSpeed(200);
  myStepperY.setSpeed(200);
  Serial.begin(9600);
  pinMode(INX, INPUT);
  pinMode(INY, INPUT);
}

void loop() {
  buttonx = digitalRead(INX);
  buttony = digitalRead(INY);
  digitalWrite(LEDX, buttonx);
  digitalWrite(LEDY, buttony);

  if (Serial.available()) {
    char c = Serial.read();
    if (c == 'X' & !buttonx){
      for (int i = 0; i < 32; i++)
      {
        myStepperX.step(1);
      }
    }
    else if (c == 'A' & !buttonx) {
      for (int i = 0; i < 32; i++)
      {
        myStepperX.step(-1);
      }
    }
    else if (c == 'Y' & !buttony){
      for (int i = 0; i < 32; i++)
      {
        myStepperY.step(1);
      }
    }
    else if (c == 'B' & !buttony) {
      for (int i = 0; i < 32; i++)
      {
        myStepperY.step(-1);
      }
    }
  } 
}

