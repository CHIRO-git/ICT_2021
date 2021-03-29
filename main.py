import cv2
import os

from show import lcd
from gaze_tracking import GazeTracking
from gaze_tracking import startclock    # get concentration module from startclock
from face_recog import face_recog_mod as frm
import dbconnection as db
import interface



########################################################################################################################

# system initialize

cwd 		= os.path.abspath(os.path.dirname(__file__))
gaze 		= GazeTracking()
encodings 	= []
vid 		= cv2.VideoCapture(0)

stopwatch 	= startclock.Timer()
stopwatch.Start()

indicator 	= True # first true second false
pageNo 		= 100
temp_input 	= 0
event 		= 0
########################################################################################################################

# system main loop

while True :
    # Interface main
    lcd.show(pageNo)

    # event phase
    if event == 0:
        # control phase
        if indicator == True:
            indic = ['>', ' ']
        else:
            indic = [' ', '>']

        pageNo, indicator, event, input = interface.interface(pageNo, indicator, event, interface.Ardread())
    elif event == 1:
        frm.activate(vid)
		event = 0
        pageNo = 100
    elif event == 2:
        frm.deactivate()
		event = 0
        pageNo = 100
    elif event == 3:
        detected = frm.detect(vid)
        if detected:
            while True:
                ret, img = vid.read()
                gaze.refresh(img)
                frame = gaze.annotated_frame()
                lcd.show_clock(stopwatch.timestr2)

                if gaze.is_right():
                    stopwatch.Stop()
                elif gaze.is_left():
                    stopwatch.Stop()
                elif frm.head(img) and gaze.is_center():
                    stopwatch.Start()
                elif gaze.is_closed():
                    stopwatch.Stop()


                if type(interface.Ardread()) is int:
                    db.save(str(stopwatch.timestr1))
                    event = 0
                    pageNo = 100
                    break
        else :
            # can't find user face
            event = 0
            pageNo = 100

    elif event == 5:
        db.upload()
		event = 0
        pageNo = 100
