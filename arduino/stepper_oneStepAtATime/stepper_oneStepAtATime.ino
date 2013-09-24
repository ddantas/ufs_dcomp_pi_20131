
#include <Stepper.h>

const int stepsPerRevolution = 64;
Stepper myStepper(stepsPerRevolution, 8,6,7,5);            


void setup() {
  myStepper.setSpeed(200);
  Serial.begin(9600);
}

void loop() {
   if (Serial.available()) {
     char c = Serial.read();
     if (c == 'H') {
        for (int i = 0; i < 32; i++)
        {
          myStepper.step(64);
        }
     }
     else if (c == 'L') {
        for (int i = 0; i < 32; i++)
        {
          myStepper.step(-64);
        }
     }
   } 
}

