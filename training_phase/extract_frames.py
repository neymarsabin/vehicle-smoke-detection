import os
import cv2

def extract_frames(video_path, output_dir, interval_sec=2):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    interval = int(fps * interval_sec)

    frame_count = 0
    saved_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % interval == 0:
            filename = os.path.join(output_dir, f"frame_{saved_count:04d}.jpg")
            cv2.imwrite(filename, frame)
            saved_count += 1
        frame_count += 1

    cap.release()
    print(f"✅ Extracted {saved_count} frames to {output_dir}")

# Example usage:
extract_frames("001.mp4", "frames/video1", interval_sec=2)
extract_frames("002.mp4", "frames/video2", interval_sec=2)
