import streamlit as st
import tempfile
import cv2
from ultralytics import YOLO
import os

# Load YOLO model
model = YOLO("best.pt")  # update path if needed

# Streamlit UI
st.title("🚍 Smoke Detection from Vehicles")
st.write("Upload a video and the model will detect vehicles emitting smoke.")

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    # Get file extension
    suffix = os.path.splitext(uploaded_file.name)[-1]

    # Save uploaded video to a temp file with the correct extension
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
        tmp_file.write(uploaded_file.read())
        video_path = tmp_file.name

    st.video(video_path)
    st.info("Processing video...")

    # Run YOLOv8 on video
    results = model.predict(
        source=video_path,
        save=True,
        save_txt=False,
        conf=0.3,
        iou=0.5,
        stream=False,
        show=False,
        device='cpu',
        project="runs",
        name="inference",
        exist_ok=True
    )

    # Get predicted output path
    output_dir = os.path.join("runs", "outputs")
    # subfolders = sorted(os.listdir(output_dir), key=lambda x: os.path.getmtime(os.path.join(output_dir, x)), reverse=True)
    # latest_run = os.path.join(output_dir, subfolders[0])
    # pred_video = os.path.join(latest_run, os.path.basename(video_path))

    # Show result
    st.success("Done! Here's the processed video:")
    st.video(pred_video)

    # Download button
    # with open(pred_video, "rb") as f:
    #     st.download_button("⬇️ Download Result", f, file_name="smoke_detection_output.mp4")

