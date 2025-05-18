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
