import streamlit as st
import os
import cv2
from utils.detector import SmokeDetector
import tempfile
from pathlib import Path

st.set_page_config(page_title="Smoky Vehicle Detector", layout="centered")
st.title("🚗💨 Smoky Vehicle Detector")

uploaded_file = st.file_uploader("Upload a traffic video", type=["mp4", "avi", "mov"])

if uploaded_file:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    video_path = tfile.name

    st.video(video_path)
    if st.button("Analyze Video"):
        st.info("Running detection...")
        detector = SmokeDetector()

        cap = cv2.VideoCapture(video_path)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out_path = Path("outputs/") / Path(uploaded_file.name).name
        os.makedirs("outputs", exist_ok=True)

        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out = cv2.VideoWriter(str(out_path), fourcc, fps, (width, height))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            detections = detector.detect_smoke(frame)
            for (x1, y1, x2, y2) in detections:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame, "Smoke", (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

            out.write(frame)

        cap.release()
        out.release()
        st.success("Detection complete!")
        st.video(str(out_path))
