## Labeling
After I have all the frames that I need to label, I labelled them with two classes:
- `vehicle` -> bounding box for all back of the vehicles going away from the camera
- `smoky` -> bounding box for all back + smoky areas near the vehicles that is emitting visible smoke

### Software for labeling
I used `label-studio` to label the frames from the pre-processing step. You might need to update a env variable to allow maximum number of frames in the application. I will add them here later:
```bash
export 
```
