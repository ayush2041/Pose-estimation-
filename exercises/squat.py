from utils.angles import calc_angle
from utils.counter import count_reps

def process_squat(landmarks, flag, count):
    hip = landmarks[23]
    knee = landmarks[25]
    ankle = landmarks[27]

    angle = calc_angle(hip, knee, ankle)

    flag, count = count_reps(angle, flag, count, 160, 70)

    if angle < 70:
        feedback = "Go lower"
    elif angle > 160:
        feedback = "Stand straight"
    else:
        feedback = "Good"

    return angle, flag, count, feedback