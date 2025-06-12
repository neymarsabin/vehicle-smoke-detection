import os
import shutil
import random
from pathlib import Path

# Paths
ROOT_DIR = "."  # Update this
IMAGE_DIR = Path(ROOT_DIR) / "images"
LABEL_DIR = Path(ROOT_DIR) / "labels"

# Output
OUTPUT_DIR = Path(ROOT_DIR)
TRAIN_IMG_DIR = OUTPUT_DIR / "train/images"
TRAIN_LBL_DIR = OUTPUT_DIR / "train/labels"
VAL_IMG_DIR = OUTPUT_DIR / "val/images"
VAL_LBL_DIR = OUTPUT_DIR / "val/labels"

# Create directories
for dir_path in [TRAIN_IMG_DIR, TRAIN_LBL_DIR, VAL_IMG_DIR, VAL_LBL_DIR]:
    os.makedirs(dir_path, exist_ok=True)

# Collect files
image_files = list(IMAGE_DIR.glob("*.*"))
image_files = [f for f in image_files if f.suffix.lower() in [".jpg", ".jpeg", ".png"]]

# Shuffle and split
random.seed(42)
random.shuffle(image_files)

split_idx = int(0.8 * len(image_files))
train_files = image_files[:split_idx]
val_files = image_files[split_idx:]

def copy_files(file_list, target_img_dir, target_lbl_dir):
    for img_path in file_list:
        lbl_path = LABEL_DIR / (img_path.stem + ".txt")
        if lbl_path.exists():
            shutil.copy2(img_path, target_img_dir / img_path.name)
            shutil.copy2(lbl_path, target_lbl_dir / lbl_path.name)
        else:
            print(f"⚠️ Warning: Label not found for {img_path.name}, skipping.")

copy_files(train_files, TRAIN_IMG_DIR, TRAIN_LBL_DIR)
copy_files(val_files, VAL_IMG_DIR, VAL_LBL_DIR)

print(f"✅ Done! Total: {len(image_files)} | Train: {len(train_files)} | Val: {len(val_files)}")

