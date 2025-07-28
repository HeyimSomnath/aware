import cv2
import numpy as np
import dlib
import time
from imutils import face_utils
import winsound

# download: http://dlib.net/files/shape_predictor_5_face_landmarks.dat.bz2

# Initialize camera
cap = cv2.VideoCapture(0)

# Load face detector and facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Initialize counters and status
sleep = 0
drowsy = 0
active = 0
status = ""
color = (0, 0, 0)

# For FPS calculation
prev_time = time.time()

# Distance function
def compute(ptA, ptB):
    dist = np.linalg.norm(ptA - ptB)
    return dist

# Blink ratio calculation
def blinked(a, b, c, d, e, f):
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)

    if ratio > 0.25:
        return 2  # Eyes open
    elif 0.21 < ratio <= 0.25:
        return 1  # Drowsy
    else:
        return 0  # Sleeping

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_frame = frame.copy()  # Safe initialization
    faces = detector(gray)

    if len(faces) == 0:
        status = "No face detected"
        color = (0, 0, 255)
    else:
        for face in faces:
            x1, y1 = face.left(), face.top()
            x2, y2 = face.right(), face.bottom()
            cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            landmarks = predictor(gray, face)
            landmarks = face_utils.shape_to_np(landmarks)

            # Eye landmarks
            left_blink = blinked(landmarks[36], landmarks[37],
                                 landmarks[38], landmarks[41],
                                 landmarks[40], landmarks[39])
            right_blink = blinked(landmarks[42], landmarks[43],
                                  landmarks[44], landmarks[47],
                                  landmarks[46], landmarks[45])

            # Drowsiness logic
            if left_blink == 0 or right_blink == 0:
                sleep += 1
                drowsy = 0
                active = 0
                if sleep > 6:
                    status = "SLEEPING !!!"
                    color = (255, 0, 0)
                    winsound.Beep(1000, 500)  # Beep alert

            elif left_blink == 1 or right_blink == 1:
                sleep = 0
                active = 0
                drowsy += 1
                if drowsy > 6:
                    status = "Drowsy !"
                    color = (0, 0, 255)

            else:
                drowsy = 0
                sleep = 0
                active += 1
                if active > 6:
                    status = "Active :)"
                    color = (0, 255, 0)

            # Draw facial landmarks
            for (x, y) in landmarks:
                cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

    # Display status
    cv2.putText(frame, status, (100, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

    # FPS display
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
    cv2.putText(frame, f"FPS: {int(fps)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100, 255, 0), 2)

    # Show frames
    cv2.imshow("Frame", frame)
    cv2.imshow("Result of detector", face_frame)

    key = cv2.waitKey(1)
    if key == 27:  # ESC key
        break

# Release camera and destroy windows
cap.release()
cv2.destroyAllWindows()
