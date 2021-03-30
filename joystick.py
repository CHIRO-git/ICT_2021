import serial
import time

PORT = '/dev/ttyACM0'
BaudRate = 9600
ARD= serial.Serial(PORT,BaudRate)
temp = 0

def Decode(A):
    A = A.decode()
    A = int(A)
    return A

def Ardread(): # return list [Ard1,Ard2]
    if ARD.readable():
        LINE = ARD.readline()
        code=Decode(LINE)
        return code
    else :
        return

while True:
    temp = Ardread()
    if type(Ardread()) is int :
        print('get!')
    time.sleep(1)