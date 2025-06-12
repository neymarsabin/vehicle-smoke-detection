import os
from pathlib import Path
import cv2

INPUT_DIR = Path("../../videos/smoky")
OUTPUT_DIR = Path("../../videos/first-train-frames")
FRAME_INTERVAL = 1

os.makedirs(OUTPUT_DIR, exist_ok=True)

video_files = list(INPUT_DIR.glob("*"))

for video_path in video_files:
    cap = cv2.VideoCapture(str(video_path))
    fps = cap.get(cv2.CAP_PROP_FPS)
    interval = int(fps * FRAME_INTERVAL)

    video_name = video_path.stem
    frames_count = 0
    saved_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frames_count % interval == 0:
            filename = OUTPUT_DIR / f"{video_name}_frame_{saved_count:04d}.jpg"
            cv2.imwrite(str(filename), frame)
            saved_count += 1
        frames_count += 1

    cap.release()
    print(f"✅ Extracted {saved_count} frames from {video_name}")
