import streamlit as st
from ultralytics import YOLO
import os
from pathlib import Path

# 🧼 Hide Streamlit header and footer
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 🧱 UI Layout
st.title("🚗 Smoky Vehicle Detection")
st.markdown("Upload a CCTV video. The system will detect and highlight smoky vs non-smoky vehicles.")

# 📤 Upload section
uploaded_video = st.file_uploader("Upload a CCTV video", type=["mp4", "mov", "avi"])
YOLO_MODEL_PATH = "best.pt"

if uploaded_video:
    # Create temp input path
    input_dir = "./inputs"
    os.makedirs(input_dir, exist_ok=True)
    input_path = os.path.join(input_dir, "input_video.mp4")

    with open(input_path, "wb") as f:
        f.write(uploaded_video.read())

    model = YOLO(YOLO_MODEL_PATH)

    # Set output directory to current script folder
    output_dir = "./outputs"
    output_name = "prediction"
    results = model.predict(
        source=input_path,
        save=True,
        save_txt=False,
        project=output_dir,
        name=output_name,
        exist_ok=True,
        conf=0.25,
        save_conf=True
    )

    output_video_path = Path(output_dir) / output_name / "input_video.avi"
    if output_video_path.exists():
        st.video(str(output_video_path))
        with open(output_video_path, "rb") as f:
            st.download_button("⬇️ Download Result Video", f, file_name="annotated_output.mp4")
    else:
        st.error("❌ Output video not found. Check model output.")
