import serial
import time


#it makes a connection between arduino and python
def OpenA(port):
   arduino = serial.Serial(port, 9600)
   time.sleep(2) # waiting the initialization...
   print("initialising")
   return arduino

#it makes the stepper motor moves 1/64 of the complete round 'direction'
def OneStep(direction, arduino):
    arduino.write(direction) # one step
    #print("one step ", direction)
    #time.sleep(2) # waits for 2 seconds

#the stepper motor moves 'x' steps in the 'direction' and returns the current position 
def StepX(direction, x, arduino):
    #print("moving ", x, "steps in ", direction)
    for i in range(x):
        OneStep(direction, arduino)
    return x

#the stepper motor moves back to the origin        
def Origin(position, arduino):
    #print("moving back to origin")
    StepX('B', position, arduino)

#it closes the connection with arduino
def CloseA(arduino):
    arduino.close()

#main
port = 'COM3'
name = OpenA(port)
dirf = 'F'
dirb = 'B'
steps = 10
OneStep(dirf, name)
OneStep(dirb, name)
StepX(dirf, steps, name)
StepX(dirb, steps, name)
Origin(steps, name)
CloseA(name)




