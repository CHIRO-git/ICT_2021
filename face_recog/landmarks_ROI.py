import dlib
import cv2 as cv
import numpy as np
import os



detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv.VideoCapture(0)

# range doesn't6 include last data
ALL = list(range(0, 68))
RIGHT_EYEBROW = list(range(17, 22))
LEFT_EYEBROW = list(range(22, 27))
RIGHT_EYE = list(range(36, 42))
LEFT_EYE = list(range(42, 48))
NOSE = list(range(27, 36))
MOUTH_OUTLINE = list(range(48, 61))
MOUTH_INNER = list(range(61, 68))
JAWLINE = list(range(0, 17))
FACE_COMPO = list(range(17, 68))

index = ALL

while True:

    ret, img_frame = cap.read()

    img_frame = cv.flip(img_frame,1)        # only use for test! mirror mode
    img_gray = cv.cvtColor(img_frame, cv.COLOR_BGR2GRAY)

    dets = detector(img_gray, 1)
    Detected = False
    for face in dets:
        Detected = True
        cv.putText(img_frame, "Face Detected", (0,25), cv.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)
        shape = predictor(img_frame, face)  # detect 68 dots from face

        list_points = []
        for p in shape.parts():
            list_points.append([p.x, p.y])

        list_points = np.array(list_points)


        # draw dots all of points included in index
        """
        for i, pt in enumerate(list_points[index]):
            pt_pos = (pt[0], pt[1])
            cv.circle(img_frame, pt_pos, 2, (0, 255, 0), -1)
        """

        # draw rectangle

        Rect_top = 480
        Rect_bot = 0
        Rect_left = 640
        Rect_right = 0
        coord_x = []
        for i, pt in enumerate(list_points[ALL]):
            coord_x.append(pt[0])
            if pt[1] < Rect_top:
                Rect_top = pt[1]
            elif pt[1] > Rect_bot:
                Rect_bot = pt[1]

            if pt[0] < Rect_left:
                Rect_left = pt[0]
            elif pt[0] > Rect_right:
                Rect_right = pt[0]



        # detect turning head
        left_x = list_points[33][0] - list_points[31][0]
        left_y = list_points[33][1] - list_points[31][1]
        right_x = list_points[35][0] - list_points[33][0]
        right_y = list_points[35][1] - list_points[33][1]
        nose_left = np.sqrt(left_x*left_x+left_y*left_y)
        nose_right = np.sqrt(right_x*right_x+right_y*right_y)
        nose_ratio = nose_right / nose_left
        cv.putText(img_frame, str(round(nose_ratio,3)), (Rect_left, Rect_bot + 50),
                   cv.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)
        if nose_ratio > 1.15 :
            cv.putText(img_frame, "left", (Rect_left, Rect_bot + 25), cv.FONT_HERSHEY_DUPLEX, 1.0,
                       (255, 255, 255), 1)
            nose_aim = 1
        elif nose_ratio < 0.85 :
            cv.putText(img_frame, "right", (Rect_left, Rect_bot + 25), cv.FONT_HERSHEY_DUPLEX, 1.0,
                       (255, 255, 255), 1)
            nose_aim = 0
        else :
            cv.putText(img_frame, "forward", (Rect_left, Rect_bot + 25), cv.FONT_HERSHEY_DUPLEX, 1.0,
                       (255, 255, 255), 1)
            nose_aim = 0
        """coord_x2 = []
        for i, pt in enumerate(list_points[NOSE]):
            coord_x2.append(pt[0])
        cv.putText(img_frame, str(np.std(coord_x)-np.std(coord_x2)), (Rect_left, Rect_bot + 50), cv.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)
"""



    if Detected:
        # set ROI
        ROI_top = 480
        ROI_bot = 0
        ROI_left = 640
        ROI_right = 0
        if nose_aim:
            ROI_interest = LEFT_EYE
        else :
            ROI_interest = RIGHT_EYE

        for i, pt in enumerate(list_points[ROI_interest]):
            if pt[1] < ROI_top:
                ROI_top = pt[1]
            elif pt[1] > ROI_bot:
                ROI_bot = pt[1]

            if pt[0] < ROI_left:
                ROI_left = pt[0]
            elif pt[0] > ROI_right:
                ROI_right = pt[0]

        # view ROI
        dit = int((ROI_right - ROI_left) * 0.5) # give extra space
        ROI = img_frame[ROI_top - dit:ROI_bot + dit, ROI_left - dit:ROI_right + dit]
        # cv.rectangle(img_frame, (ROI_left, ROI_top), (ROI_right, ROI_bot), (255, 0, 0), 1)
        ROI = cv.resize(ROI, (0, 0), 3, 3, cv.INTER_AREA)

        cv.imshow("ROI", ROI)

    cv.imshow('result', img_frame)

    key = cv.waitKey(1)

    if key == 27:
        break


cap.release()