import serial

PORT = '/dev/ttyACM0'
BaudRate = 9600
ARD= serial.Serial(PORT,BaudRate)
def Decode(A):
    A = A.decode()
    A = int(A)
    return A

def Ardread(): # return list [Ard1,Ard2]
    if ARD.readable():
        LINE = ARD.readline()
        code=Decode(LINE)
        print(code)
        return code
    else :
        return

def pagenum(page,digit):
    return (page % pow(10,digit)) / pow(10,digit-1)



def interface(pageNo, indicator, event, input):

    if input == -2:
        # up
        indicator = False
    elif input == 2:
        # down
        indicator = True
    elif input == -1:
        # left
        if pagenum(pageNo, 3) == 1:
            if pagenum(pageNo, 2) == 1 and pagenum(pageNo, 1) == 2:
                pageNo -= 1
            elif pagenum(pageNo, 2) == 2 and pagenum(pageNo, 1) == 2:
                pageNo -= 1
        elif pagenum(pageNo, 3) == 2:
            if pagenum(pageNo, 2) == 0:
                pageNo -= 100
    elif input == 1:
        # right
        if pagenum(pageNo, 3) == 1:
            if pagenum(pageNo, 2) == 0:
                pageNo += 100
            elif pagenum(pageNo, 2) == 1 and pagenum(pageNo, 1) == 1:
                pageNo += 1

    elif input == 5:
        # click
        if pagenum(pageNo, 3) == 1:
            if pagenum(pageNo, 2) == 0:
                if indicator is True:
                    pageNo += 11
                elif indicator is False:
                    pageNo += 21
            elif pagenum(pageNo, 2) == 1:
                if pagenum(pageNo, 1) == 1:
                    if indicator is True:
                        event = 1
                    elif indicator is False:
                        event = 2
                elif pagenum(pageNo, 1) == 2:
                    pageNo = 100
            elif pagenum(pageNo, 2) == 2:
                if pagenum(pageNo, 1) == 1:
                    if indicator is True:
                        event = 3
                    elif indicator is False:
                        event = 4
                elif pagenum(pageNo, 1) == 2:
                    pageNo = 100
        elif pagenum(pageNo, 3) == 2:
            if pagenum(pageNo, 2) == 0:
                if indicator is True:
                    pageNo += 11
                elif indicator is False:
                    pageNo = 100
            elif pagenum(pageNo, 2) == 1 and pagenum(pageNo, 1) == 1:
                if indicator is True:
                    pageNo += 1
                elif indicator is False:
                    pageNo -= 11
            elif pagenum(pageNo, 2) == 1 and pagenum(pageNo, 1) == 2:
                if indicator is True:
                    event = 5
                elif indicator is False:
                    pageNo -= 12

    input = 0
    return pageNo, indicator, event, input