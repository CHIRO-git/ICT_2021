import cv2
from gaze_tracking import GazeTracking
from gaze_tracking import startclock #get concentration module from startclock

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
stopwatch = startclock.Timer()
stopwatch.Start()

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    stopwatch.MakeWidget()
    text = ""

    if gaze.is_right():
        stopwatch.Stop()
        text = "Looking right"
    elif gaze.is_left():
        stopwatch.Stop()
        text = "Looking left"
    elif gaze.is_center():
        stopwatch.Start()
        text = "Looking center"
    elif gaze.is_closed():
        stopwatch.Stop()
        text = "Eyes closed"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2) #print where one is looking at

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, str(stopwatch.timestr), (90, 200), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    #print time how long one has concentrated. Changes ONLY when one blinks, or look somewhere else.

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
