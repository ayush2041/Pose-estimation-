from utils.angles import calc_angle
from utils.counter import count_reps

def process_pushup(landmarks, flag, count):
    shoulder = landmarks[11]
    elbow = landmarks[13]
    wrist = landmarks[15]

    angle = calc_angle(shoulder, elbow, wrist)

    flag, count = count_reps(angle, flag, count, 160, 70)

    if angle < 70:
        feedback = "Go lower"
    elif angle > 160:
        feedback = "Full extension"
    else:
        feedback = "Good"

    return angle, flag, count, feedback