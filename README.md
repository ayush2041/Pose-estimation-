# 🏋️ FitTrack – Real-Time Exercise Form Analyzer

FitTrack is a real-time exercise tracking system that monitors body movements using a webcam and analyzes exercise form. It provides repetition counting, posture feedback, and session tracking to help users perform exercises correctly and track their performance over time.

---

## 🚀 Features

* 🎯 Real-time body tracking using webcam
* 🔢 Automatic repetition counting
* 📐 Joint angle calculation for movement analysis
* ⚠️ Posture feedback for correct and incorrect form
* 🏃 Multiple exercise support:

  * Biceps curls
  * Squats
  * Pushups
* 🖥️ Live UI overlay with exercise stats
* 📊 Workout session tracking (CSV storage)
* 📈 Dashboard visualization using charts

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** OpenCV, MediaPipe, NumPy, Pandas, Matplotlib
* **Concepts:** Computer Vision, Pose Tracking, Motion Analysis

---

## 📂 Project Structure

```
fittrack/
│
├── main.py
│
├── exercises/
│   ├── biceps.py
│   ├── squat.py
│   ├── pushup.py
│
├── utils/
│   ├── angles.py
│   ├── counter.py
│   ├── stats.py
│   ├── dashboard.py
│
├── ui/
│   ├── display.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/ayush2041/fittrack.git
cd fittrack
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

---

## 🎮 Controls

| Key | Action         |
| --- | -------------- |
| B   | Biceps         |
| S   | Squat          |
| P   | Pushup         |
| D   | Open Dashboard |
| Q   | Quit           |

---

## 📊 Dashboard

* Displays repetitions per session
* Shows distribution of exercises performed
* Visualizes workout data using matplotlib

---

## 📁 Output

The system automatically generates:

📄 `workout_stats.csv`

Example:

```
Date,Exercise,Reps,Duration
2026-04-01 14:20,biceps,12,45.3
```

---

## 🧠 How It Works

1. Captures live video using OpenCV
2. Detects body landmarks using MediaPipe
3. Calculates joint angles using vector mathematics
4. Tracks movement patterns to count repetitions
5. Provides feedback based on predefined thresholds
6. Stores workout data and visualizes it using charts

---

## 📸 Demo

> Add:

* Screenshots of UI
* Dashboard graphs
* Short demo video (recommended)

Example:

```
## 🎥 Demo
[Watch Demo](your-video-link)
```

---

## 📈 Future Improvements

* Web-based interface (React + Flask)
* Mobile version
* Advanced workout analytics
* Personalized exercise recommendations

---

## 🤝 Contributing

Contributions are welcome. Feel free to fork the repository and submit pull requests.

---

## 📬 Contact

**Ayush Singh**
📧 [singhayush2041@gmail.com](mailto:singhayush2041@gmail.com)
🔗 https://github.com/ayush2041

---

## ⭐ Acknowledgements

* MediaPipe by Google
* OpenCV community

---
