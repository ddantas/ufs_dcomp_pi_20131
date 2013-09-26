#include <Stepper.h>

#define INX 6
#define INY 7
#define LEDX 12
#define LEDY 13

const int stepsPerRevolution = 64;
Stepper myStepperX(stepsPerRevolution, 11,9,10,8); 
Stepper myStepperY(stepsPerRevolution, 5,4,3,2); 

int buttonx = 0;
int buttony = 0;

void setup() {
  myStepperX.setSpeed(200);
  myStepperY.setSpeed(200);
  Serial.begin(9600);
  pinMode(INX, INPUT_PULLUP);
  pinMode(INY, INPUT_PULLUP);
}

void loop() {
  buttonx = digitalRead(INX);
  buttony = digitalRead(INY);
  digitalWrite(LEDX, buttonx);
  digitalWrite(LEDY, buttony);

  if (Serial.available()) {
    char c = Serial.read();
    if (c == 'X' & buttonx == LOW){
      for (int i = 0; i < 32; i++)
      {
        myStepperX.step(1);
      }
    }
    else if (c == 'A' & buttonx == LOW) {
      for (int i = 0; i < 32; i++)
      {
        myStepperX.step(-1);
      }
    }
    else if (c == 'Y' & buttony == LOW){
      for (int i = 0; i < 32; i++)
      {
        myStepperY.step(1);
      }
    }
    else if (c == 'B' & buttony == LOW) {
      for (int i = 0; i < 32; i++)
      {
        myStepperY.step(-1);
      }
    }
  } 
}

