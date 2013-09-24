#include <Stepper.h>


const int stepsPerRevolution = 64;
Stepper myStepper(stepsPerRevolution, 11,9,10,8);            


void setup() {
  myStepper.setSpeed(200);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
     char c = Serial.read();
     if (c == 'F') {
        for (int i = 0; i < 32; i++)
        {
          myStepper.step(1);
        }
     }
     else if (c == 'B') {
        for (int i = 0; i < 32; i++)
        {
          myStepper.step(-1);
        }
     }
   } 
}
