import csv
from datetime import datetime

def save_stats(exercise, reps, duration):
    file_name = "workout_stats.csv"

    try:
        with open(file_name, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Exercise", "Reps", "Duration"])
    except FileExistsError:
        pass

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            exercise,
            reps,
            round(duration, 2)
        ])