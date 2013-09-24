import serial
import time


#it makes a connection between arduino and python
def OpenA(port):
   arduino = serial.Serial(port, 9600)
   time.sleep(2) # waiting the initialization...
   print("initialising")
   return arduino

#it makes the stepper motor moves 1/64 of the complete round in 'direction'
def OneStep(direction, arduino):
    arduino.write(direction) # one step
    #print("one step ", direction)
    #time.sleep(2) # waits for 2 seconds

#the stepper motor moves 'x' steps in the x axis in 'direction'  
def StepX(direction, x, arduino):
    #print("moving ", x, "steps in ", direction)
    for i in range(x):
        if(direction == 'F'):
            OneStep('X', arduino)
        elif(direction == 'B'):
            OneStep('A', arduino)

#the stepper motor moves 'y' steps in the y axis in 'direction'  
def StepY(direction, y, arduino):
    #print("moving ", y, "steps in ", direction)
    for i in range(y):
        if(direction == 'F'):
            OneStep('Y', arduino)
        elif(direction == 'B'):
            OneStep('B', arduino)

#the stepper motor moves 'x' steps in the x axis and 'y' steps in the y axis
def StepXY(x, y, arduino):
    for i in range(y):
        StepX('F', x, arduino)
        StepX('B', x, arduino)
        StepY('F', 1, arduino)
        
#it closes the connection with arduino
def CloseA(arduino):
    arduino.close()


#main

port = 'COM3'
dirf = 'F'
dirb = 'B'
arduino = OpenA(port)
print("moving x")
StepX(dirf, 10000, arduino)
time.sleep(5)
print("moving y")
StepY(dirb, 20, arduino)
CloseA(arduino)
