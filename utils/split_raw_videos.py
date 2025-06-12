import os
import subprocess
from pathlib import Path

# Configuration
INPUT_DIR = "../../videos"             # Folder containing large 4K videos
OUTPUT_DIR = "../../videos/splitted"      # Where 30-second clips will go
CHUNK_DURATION = 30 # in seconds
SUPPORTED_FORMATS = (".mp4", ".mov", ".mkv", ".avi")

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Find all video files in the input directory
video_files = [f for f in Path(INPUT_DIR).glob("*") if f.suffix.lower() in SUPPORTED_FORMATS]

for video_path in video_files:
    base_name = video_path.stem  # File name without extension
    ext = video_path.suffix
    output_template = os.path.join(OUTPUT_DIR, f"%03d{base_name}_video{ext}")

    print(f"⏳ Splitting {video_path.name} into 30-second chunks...")

    # ffmpeg command to split the video
    command = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel", "info",
        "-i", str(video_path),
        "-c", "copy",
        "-map", "0:a:0?",
        "-map", "0:v:0",
        "-f", "segment",
        "-segment_time", str(CHUNK_DURATION),
        "-reset_timestamps", "1",
        output_template
    ]

    subprocess.run(command, check=True)
    print(f"✅ Done: {video_path.name}")

print("\n🎉 All videos processed.")

