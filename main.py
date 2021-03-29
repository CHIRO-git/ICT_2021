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

indicator = True # first true second false
pageNo = 100
temp_input = 0
event = 0
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
    elif event == 2:
        frm.deactivate()
    elif event == 3:
        detected = frm.detect(vid)
        if detected:
            while True:
                ret, img = vid.read()
                gaze.refresh(img)
                frame = gaze.annotated_frame()
				lcd.show_clock()

                if gaze.is_right():
                    stopwatch.Stop()
                elif gaze.is_left():
                    stopwatch.Stop()
                elif frm.head(img) and gaze.is_center():
                    stopwatch.Start()
                elif gaze.is_closed():
                    stopwatch.Stop()
			if input != 0 :
				event = 0
			if escaped:
                db.save(stopwatch.timestr)
        else :
            # can't find user face
            event = 0

    elif event == 5:
        db.upload()






"""
if detected :
    print("detected")
    while True:
        ret, img = vid.read()
        face_find, head_shake = frm.head(img)

        # if
        if head_shake is False:
            gaze.refresh(img)
            frame = gaze.annotated_frame()
            stopwatch.MakeWidget()

            if gaze.is_right():
                stopwatch.Stop()
                print("Looking right")
            elif gaze.is_left():
                stopwatch.Stop()
                print("Looking left")
            elif gaze.is_center():
                stopwatch.Start()
                print("Looking center")
            elif gaze.is_closed():
                stopwatch.Stop()
                print("Eyes closed")


        if cv2.waitKey(10) == ord("q") :
            break

cv2.destroyAllWindows()
"""