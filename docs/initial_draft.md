### Initial Draft
#### Choosing the Right Approach
- using pre-trained models like YOLO, which detect both smoke and vehicles??
- commercial systems like Scylla, or Bosch AVIOTEC also offer ready-to-use solutions, though they may need customization for vehicles

#### YOLO-Based Object Detection
- YOLO(You Only look Once) is a fast and accurate object detection model widely used for detecting vehicles and smoke.
- fine-tune it on your training data, ensuring dataset includes labeled images of vehicles and smoke under various conditions.

### Steps
#### Detection
- Use YOLOv5 or YOLOv8 for real-time detection of vehicles and smoke in each frame
- Fine-tune YOLOv5 on the training data to improve accuracy for vehicles and smoke.

#### Tracking
- Apply DeepSORT to track vehicles across frames, assigning each a unique ID

#### Association
- For each smoke detection:
    - find the nearest vehicle track based on centroid distance
    - compute the vehicle's direction(velocity vector) from tracking data
    - check if smoke is behind the vehicle(dot product of vehicle-to-smoke vector and velocity vector < 0)
    - associate smoke with the vehicle if within a distance threshold (e.g. 50 pixels)

#### Scoring
- for each vehicle track:
    - maintain a smoke score (start at 0)
    - increment score by 1 when associated smoke is detected in a frame
    - decrement score by 1 otherwise (minimum 0)
    - flag the vehicle if the score exceeds a threshold (e.g. 5 out of 10 frames)

#### Output
- record flagged vehicle IDs
- capture images or video clips of flagged vehicles for evidence
- integrate with a notification system if required

### Implementation Notes
- YOLOv5s: Lightweight and suitable for real-time CCTV processing
- DeepSORT: Combines detection with tracking for consistent vehicle IDs
- Tuning: Adjust distance threshold and scoring threshold based on footage characters
- Optimization: Use model pruning or quantization for edge deployment if needed
