### 2. DB-NET: Detecting Vehicle Smoke with Deep Block Networks 
- authors created a new dataset of 3,962 images with labeled vehicle smoke
- Deep Block Network(DB-Net) is a new AI model proposed by the authors that detect vehicle smoke detection as "block-wise prediction" problem, making it both accurate and fast
- DB-Net outperforms other methods in both accuracy and speed

#### Why it matters?
- environmental impact
- automation
- real-world challenge

#### problem with existing methods
General object detection methods falls into:

- Bounding-Box Detection
    - draws a rectangle around the smoke area but often miss the exact shape, leading to less accurate results
    - think of trying to outline a cloud with a square - it's not a perfect fit
- Pixel-Level Segmentation
    - this label every single pixel in an image as smoke or not, which is super accurate but takes a long time to process 

#### How it works?
##### Dataset
- authors created a new dataset of 3,962 images with labeled vehicle smoke

##### Breaking Images into Blocks
- DB-Net splits each video frame into a grid of smaller blocks
- Each block is analyzed separately, which is faster than looking at every pixel

##### Deep Learning to Analyze Blocks
- deep neural network to classify each block as either containing smoke or not
- DB-Net is built with layers that learn to spot smoke by looking at features like color, texture and how the block changes from one video frame to the next.
- it is like teaching AI to recognize the wispy, dark look of smoke versus the solid shape of a car

##### Putting it all together
- DB-Net combines the results to create a map of where the smoke is in the image

#### Key Features
- block-wise approach -> by working with blocks instead of pixels or boxes, DB-Net strikes a balance between accuracy and speed
- efficient design -> it's built to process videos quickly, which is crucial for real-time monitoring
- open dataset -> labeled images are gifts to the AI community, letting others build on this work

#### Results
- accuracy -> DB-Net achieved high accuracy in spotting smoke
- speed -> it processes images quickly, making it suitable for real-time use
- comparison -> DB-Net outperformed both bounding-box methods
