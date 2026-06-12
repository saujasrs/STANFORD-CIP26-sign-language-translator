# Real-Time Sign Language Translator

This project is an incremental AI and computer vision system for translating
hand signs from webcam input into text.

## Current Phase

Phase 1 is implemented:

- Open the webcam.
- Read video frames in real time.
- Display the live camera feed.
- Quit safely by pressing `q`.

## Project Roadmap

1. Webcam access
2. Hand detection using MediaPipe
3. Landmark extraction
4. Dataset collection
5. Data preprocessing
6. Random Forest model training
7. Model evaluation
8. Real-time prediction
9. Sentence construction
10. Text-to-speech
11. UI improvements
12. Optional deep learning upgrade

## Setup

Create and activate a virtual environment, then install dependencies:

```bash
pip install -r requirements.txt
```

Run the Phase 1 webcam preview:

```bash
python main.py
```

If you use an external webcam such as a Logitech camera, try:

```bash
python main.py --camera-index 1
```

If that does not open the correct camera, try `--camera-index 2`.

Press `q` to quit the webcam window.
