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
