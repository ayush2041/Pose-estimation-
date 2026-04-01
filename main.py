import cv2
import mediapipe as mp
import time

from exercises.biceps import process_biceps
from exercises.squat import process_squat
from exercises.pushup import process_pushup

from ui.display import draw_ui
from utils.stats import save_stats
from utils.dashboard import show_dashboard

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
pose = mp_pose.Pose()

count = 0
flag = None
exercise = "biceps"
start_time = time.time()

print("B=Biceps | S=Squat | P=Pushup | D=Dashboard | Q=Quit")

while cap.isOpened():
    ret, frame = cap.read()

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    try:
        landmarks = results.pose_landmarks.landmark

        if exercise == "biceps":
            angle, flag, count, feedback = process_biceps(landmarks, flag, count)

        elif exercise == "squat":
            angle, flag, count, feedback = process_squat(landmarks, flag, count)

        elif exercise == "pushup":
            angle, flag, count, feedback = process_pushup(landmarks, flag, count)

        draw_ui(image, count, feedback, exercise)

    except:
        pass

    mp_drawing.draw_landmarks(
        image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS
    )

    cv2.imshow("FitTrack", image)

    key = cv2.waitKey(10) & 0xFF

    if key in [ord('b'), ord('s'), ord('p')]:
        duration = time.time() - start_time
        save_stats(exercise, count, duration)

        if key == ord('b'):
            exercise = "biceps"
        elif key == ord('s'):
            exercise = "squat"
        elif key == ord('p'):
            exercise = "pushup"

        count = 0
        flag = None
        start_time = time.time()

    elif key == ord('d'):
        show_dashboard()

    elif key == ord('q'):
        duration = time.time() - start_time
        save_stats(exercise, count, duration)
        break

cap.release()
cv2.destroyAllWindows()