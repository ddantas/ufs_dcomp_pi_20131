
#include <Stepper.h>

const int stepsPerRevolution = 64;
Stepper myStepper(stepsPerRevolution, 11,9,10,8);            


void setup() {
  myStepper.setSpeed(200);
}

void loop() {
  for (int i = 0; i < 32; i++)
  {
    myStepper.step(-64);
  }

  delay(1000);

  for (int i = 0; i < 32; i++)
  {
    myStepper.step(64);
  }
  
  delay(1000);
}

