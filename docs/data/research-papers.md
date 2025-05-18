## Previous Work
## existing research?
1. [Automatic Detection Method for Black Smoke Vehicles Considering Motion Shadows](https://pmc.ncbi.nlm.nih.gov/articles/PMC10574957/)
2. [DB-NET: Detecting Vehicle Smoke with Deep Block Networks](https://www.mdpi.com/2076-3417/13/8/4941)
3. [Vehicle Smoke Synthesis and Attention-Based Deep Approach for Vehicle Smoke Detection](https://www.mdpi.com/2076-3417/13/8/4941)
4. [A lightweight model for Real-Time Detection of Vehicle Black Smoke](https://www.mdpi.com/1424-8220/23/23/9492)
5. [Video-based smoky vehicle detection with a coarse-to-fine framework](https://arxiv.org/abs/2207.03708)
6. [Detecting Smoky Vehicles from traffic surveillance videos based on dynamic features](https://link.springer.com/article/10.1007/s10489-019-01589-z)
7. [An Improved method for AI-based smoky vehicle detection from traffic surveillance videos](https://link.springer.com/article/10.1007/s11760-024-03659-3#data-availability)

## Explanations
### 1. Automatic Detection Method for Black Smoke Vehicles Considering Motion Shadows
- as vehicles move, they cast shadows called "motion shadows" that can look like smoke in the footage
- that might trick a basic detection system into flagging the wrong vehicles
- this method is special because it figures out how to tell the difference between real smoke and these confusing shadows

#### Why it matters?
- Cleaner Air
- Efficiency
- The Shadow Problem

#### steps:
##### Finding Moving Objects
- pick out anything that's moving like vehicles, shadows and smoke from them
- uses an AI model called YOLOv5s, which is "You Only Look Once version 5, small"

##### Sorting Out Smoke from Shadows
- What it does -> after the moving stuff, system figures out what's smoke, what's a shadow, and what's just a vehicle
- Superpixel segmentation -> chopping video frames into small puzzle pieces based on color and texture
- later those pieces are used to analyze
- classifying the pieces -> pieces go into other AI model called MobileNettv3, a lightweight tool that's trained to label each piece as either a vehicle, smoke or shadow
- not going to worry too much about the details of working with shadows for the time being

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

### 3. Vehicle Smoke Synthesis and Attention-Based Deep Approach for Vehicle Smoke Detection



