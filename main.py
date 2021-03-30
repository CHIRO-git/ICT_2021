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

cwd = os.path.abspath(os.path.dirname(__file__))
gaze = GazeTracking()
encodings = []
vid = cv2.VideoCapture(0)

stopwatch = startclock.Timer()
stopwatch.Start()

indicator = True # True indicates first, False indicates second
pageNo = 100
temp_input = 0
event = 0
indic = ['>', ' ']
count = 0
########################################################################################################################

# system main loop

while True :
    # Interface main
    lcd.show(pageNo, indic)

    # event phase
    if event == 0:
        # control phase
        temp_input = interface.Ardread()
        pageNo, indicator, event, input = interface.interface(pageNo, indicator, event, temp_input)

        if indicator == True:
            indic = ['>', ' ']
        else:
            indic = [' ', '>']



    if event == 1:
        frm.activate(vid)
        pageNo = 100
        event = 0
    elif event == 2:
        frm.deactivate()
        pageNo = 100
        event = 0
    elif event == 3:
        # detected = frm.detect(vid)
        if True:
            while True:
                count += 1
                ret, img = vid.read()
                gaze.refresh(img)
                frame = gaze.annotated_frame()
                lcd.show_clock(str(stopwatch.timestr2))

                if frm.head(img):
                    if gaze.is_right():
                        stopwatch.Stop()
                    elif gaze.is_left():
                        stopwatch.Stop()
                    elif gaze.is_center():
                        stopwatch.Start()
                    elif gaze.is_closed():
                        stopwatch.Stop()
                else:
                    stopwatch.Stop()

                if count > 10:
                    count = 11
                    if type(interface.Ardread()) is int:
                        db.save(str(stopwatch.timestr1))
                        event = 0
                        pageNo = 100
                        break
                        count = 0
        else :
            # can't find user face
            event = 0
            pageNo = 100
    elif event == 4:
        pageNo = 100
        event = 0
    elif event == 5:
        db.upload()
        pageNo = 100
        event = 0