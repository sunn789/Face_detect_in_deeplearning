# 🚀 Real-Time Face & Landmark Detection (2025)

A high-performance, deep learning-based face detection project using **Google MediaPipe Tasks** and **OpenCV**. This project detects faces and key landmarks (eyes, nose, mouth, and ears) in real-time via webcam.

![Python](img.shields.io)
![MediaPipe](img.shields.io)
![OpenCV](img.shields.io)

## ✨ Features
- **Deep Learning Model:** Uses BlazeFace (TFLite) for high accuracy.
- **Keypoint Detection:** Tracks 6 facial landmarks (eyes, nose, mouth, ears).
- **Real-Time Performance:** Optimized for CPU using XNNPACK delegate.
- **Modern API:** Implemented using the latest MediaPipe Tasks API (2025).

## 🛠️ Prerequisites

Before running the project, ensure you have the following installed:

```bash
pip install opencv-python mediapipe
```

## 📂 Model Setup
1. **Download the pre-trained model:** [blaze_face_short_range.tflite](storage.googleapis.com)
2. **Place the file:** Ensure the `.tflite` file is in the root directory of this project.

## 🚀 How to Run
### Image Detection
To detect faces in a static image:
```bash
python imgrec.py
```


## Live Webcam Detection
To run the real-time webcam detector:
```bash
python webcam_detect.py
```

## 📝 How it Works
### The project follows these steps:
- 1BGR to RGB: Converts OpenCV's default color space to RGB for the AI model.
- **Inference: The MediaPipe Face Detector processes the frame.
- **Coordinate Transformation: Converts normalized landmarks (0.0 to 1.0) into pixel coordinates.
- **Visualization: Draws bounding boxes and landmark circles on the live stream.
📸 Keypoints Map
### The model identifies 6 specific points:
- Right/Left Eyes
- Nose Tip
- Mouth Center
- Right/Left Ear Tragus
## 🤝 Contributing
Contributions, issues, and feature requests are welcome!
Developed by @@Rad - 2025