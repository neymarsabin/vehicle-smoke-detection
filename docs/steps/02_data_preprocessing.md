## Data PreProcessing
Ran a bunch of pre-processing steps.
### Data Cleaning
- removed a bunch of noisy data 
    - like video clips that were not stable while capturing
    - some of the videos don't have vehicles, only motorbikes that I do not care about at this moment. I am only going to use it for testing the model not training
    - some of the videos were from streets, that I don't need
    - the output was a total of 50mins long
- split lager videos to smaller 30 seconds chunk
    - split images into smaller 30 seconds with same encoding using `ffmpeg`
    ```bash
    python split_raw_videos.py

    ```
- frame extraction
    - used a python script to extract frames from the videos, per seconds or per second
    - because I need to use this to label videos
