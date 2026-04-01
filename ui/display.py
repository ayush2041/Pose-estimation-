import cv2

def draw_ui(image, count, feedback, exercise):
    cv2.rectangle(image, (0,0), (320,160), (0,0,0), -1)

    cv2.putText(image, f'Exercise: {exercise}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

    cv2.putText(image, f'Reps: {count}', (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.putText(image, f'Feedback: {feedback}', (10, 110),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

    cv2.putText(image, "Press D for Dashboard", (10, 140),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0), 1)