from pathlib import Path
import shutil
from ultralytics import YOLO

# Set paths
project_root = Path('.')           # Your main project directory
data_yaml = project_root / 'data.yaml'
custom_model_output = project_root / 'smoky_vehicle_best.pt'

# overrite yolo model
model = YOLO('yolov8s.pt')

# Run training
model.train(
    imgsz=640,
    batch=16,
    epochs=15,
    data="./data.yaml",
    name='smoky_vehicle_detector',
)

# After training, copy the best.pt to the project directory
trained_model_dir = Path('runs/train/smoky_vehicle_detector/weights')
best_model_path = trained_model_dir / 'best.pt'

if best_model_path.exists():
    shutil.copy(best_model_path, custom_model_output)
    print(f"[✔] Model saved to: {custom_model_output}")
else:
    print("[✖] Training completed, but 'best.pt' not found.")
