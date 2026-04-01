import pandas as pd
import matplotlib.pyplot as plt

def show_dashboard():
    try:
        df = pd.read_csv("workout_stats.csv")

        if df.empty:
            print("No data to display")
            return

        # Reps per session
        plt.figure()
        plt.plot(df["Reps"], marker='o')
        plt.title("Reps per Session")
        plt.xlabel("Session")
        plt.ylabel("Reps")
        plt.show()

        # Exercise distribution
        plt.figure()
        df["Exercise"].value_counts().plot(kind='bar')
        plt.title("Exercise Distribution")
        plt.show()

    except Exception as e:
        print("Error loading dashboard:", e)