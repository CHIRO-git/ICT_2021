import face_recognition
import dlib
import cv2
import  numpy as np

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

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




vid = cv2.VideoCapture(0)



def capture(vid):
    """
    vid = cv VideoCapture
    capture image from cam, save as jpeg file in user folder.
    """
    while True:
        ret, frame = vid.read()

        if ret:
            cv2.imshow('frame_color', frame)
            if cv2.waitKey(1) == ord('c'):  # if button input True, capture and save image as jpg
                cv2.imwrite('./user/test_image.jpg', frame)
                break

def readimg(imgaddr):
    """
    imgaddr = jpg image file address
    return encoding as list var.
    encoding image for recognizing face
    """
    image = face_recognition.load_image_file(imgaddr)
    encoding = face_recognition.face_encodings(image)[0]
    return encoding

def detect(vid, encodings):
    """
    vid = cv VideoCapture , encodings = list of encoding var.
    If matched face exists, return True
    from Cam video, find face and match with encoded face datas.
    """
    face_locations = []
    face_encodings = []
    while True:
        ret, frame = vid.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(encodings, face_encoding)
            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                return True


def head(vid):
    """
    vid = cv VideoCapture
    return face missed or head shake
    find face from cam video, detect head shaken.
    """
    ret, img_frame = vid.read()

    img_frame = cv2.flip(img_frame, 1)  # only use for test! mirror mode
    img_gray = cv2.cvtColor(img_frame, cv2.COLOR_BGR2GRAY)

    dets = detector(img_gray, 1)
    Detected = False
    for face in dets:
        Detected = True
        shape = predictor(img_frame, face)  # detect 68 dots from face

        list_points = []
        for p in shape.parts():
            list_points.append([p.x, p.y])

        list_points = np.array(list_points)

    # detect turning head
    if Detected:
        left_x = list_points[33][0] - list_points[31][0]
        left_y = list_points[33][1] - list_points[31][1]
        right_x = list_points[35][0] - list_points[33][0]
        right_y = list_points[35][1] - list_points[33][1]
        nose_left = np.sqrt(left_x * left_x + left_y * left_y)
        nose_right = np.sqrt(right_x * right_x + right_y * right_y)
        nose_ratio = nose_right / nose_left
        if nose_ratio > 1.15:
            head_shake = True
            print("left")
        elif nose_ratio < 0.85:
            head_shake = True
            print("right")
        else:
            head_shake = False
            print("forward")
    else :
        print("face missed!")


#debug
encodings = []


capture(vid)

encodings.append(readimg('./user/test_image.jpg'))

detected = detect(vid, encodings)

if detected :
    print("detected")
    while True:
        head(vid)
        if cv2.waitKey(10) == ord("q"):
            break