### Vehicle Smoke Detection
This is a project focused on detecting vehicle smoke using YOLOv8s model. The goal is to identify vehicles emitting visible smoke from CCTV footage. In my case I am using a dataset of vehicles that I captured myself using a GoPro 4k camera at 60fps. All of the videos is a place from my city, that I cannot add here but I have added sample images in the `model/training_phase_3/images` directory.

### Project Structure
```plaintext
vehicle-smoke-detection/
├── model/training_phase_3/ # main directory for training the model
            |-- docs/ # tried to maintain a few docs while research about vehicle smoke detection
            |-- data.yaml # dataset configuration file for YOLOv8
            |-- train_test_split.py # script to split the dataset(`./images`) into train and test sets
            |-- train_yolo.py # script to train the YOLOv8 model
            |-- server.py # run streamlit app to visualize the results
|--- utils/
          |-- extract_frames.py # script to extract frames from videos
          |-- split_raw_videos.py # script to split large videos into smaller chunks
```

### Installation
You need to use `uv` to install the dependencies. Make sure you have `uv` installed.
```bash
uv sync
```

### Usage
To train the YOLOv8 model, run the following command:
```bash
cd model/training_phase_3/
python train_yolo.py
```
This step generates a `best.pt` model file in the `model/training_phase_3/weights/` directory, which is the trained YOLOv8 model. Copy that file to the `model/training_phase_3/best.pt` directory.

### Visualization
To visualize the results, run the following command:
```bash
cd model/training_phase_3/
streamlit run server.py
```

### Results
The trained model can detect normal and smoky vehicles in the videos. The app is not yet deployed but you can run it locally to see the results. This is not a fully working version there are still some issues with the model, but it is a good starting point. I will keep updating the model and the app as I progress.

## Contributing
Just fork it and update docs or code. Submit a pull request, issues and I will review it. Ask me anything on the issues/discussions page.
