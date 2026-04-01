from utils.angles import calc_angle
from utils.counter import count_reps

def process_biceps(landmarks, flag, count):
    shoulder = landmarks[11]
    elbow = landmarks[13]
    wrist = landmarks[15]

    angle = calc_angle(shoulder, elbow, wrist)
    flag, count = count_reps(angle, flag, count, 160, 40)

    feedback = "Good" if angle > 40 else "Extend arm"

    return angle, flag, count, feedback