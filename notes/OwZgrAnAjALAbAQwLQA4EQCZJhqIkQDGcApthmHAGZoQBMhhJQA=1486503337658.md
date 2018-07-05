# Computer vision benchmark based on synthetic data (Matt + Weichao)

In the UnrealCV paper, only a toy dataset was generated. The file format is not compatible with popular image dataset yet, and no off-shelf dataset that others can use directly. This limits the popularity of synthetic data.

Benchmark pushes the advancement of computer vision. New benchmark provides data and evaluation to understand new algorithms. Synthetic data can do much more than hard for real images. There are already some examples, [Sintel](http://sintel.is.tue.mpg.de), [Virtual KITTI](http://www.xrce.xerox.com/Our-Research/Computer-Vision/Proxy-Virtual-Worlds), [SYNTHIA](http://synthia-dataset.net), more can be found in [this page](https://github.com/unrealcv/synthetic-computer-vision)

The goal of this project is setuping up benchmark using synthetic images. And this can be futher extended to task-oriented challenges.

## Advantages


## The goal

We need to have a plan for what to do (TODO). The short-term goal is mimicing those standard benchmarks in computer vision, such as PASCAL and COCO, fix the technical details that preventing others to use synthetic data, such as the file format incompatibility, etc. The long term goal for this benchmark is creating task-oriented benchmark for computer vision.

We need to think the benefits we can bring to the community, this requires talking with people working with specific tasks (TODO). For example: 1. object detection, we can generate bounding box for a lot of objects (hundreds or thousands), we can label which region is occluded and use this to study the effect of occlusion. 2. One image with many annotations (obj_mask, depth) is hard, a unified CV algorithm ([UberNet](https://arxiv.org/abs/1609.02132)) requires this type of data.

Get familiar with existing benchmarks, What tasks we want to include and why our data will be attractive to the community. (TODO) 

We will need to think a lot of details later, like: How many images is sufficient. What ground truth should be included. What is the ground truth format. Do we need an evaluation server? What scenes can we provided. Do we need a baseline algorithm? How to popularize our work. What is missing from the UnrealCV toolset. 

## Related work
- [PASCAL](http://host.robots.ox.ac.uk/pascal/VOC/)
- [COCO](http://mscoco.org/) - A large dataset with good API
- [CocoDoom](https://arxiv.org/abs/1610.02431) - Apply COCO API to the popular game Doom
- [UberNet](https://arxiv.org/abs/1609.02132)
- [UnrealStereo](https://arxiv.org/abs/1612.04647) - Use UnrealCV for stereo diagnosis, data will be available soon
- [UberNet](https://arxiv.org/abs/1609.02132)
- [ImageNet]()
- [VizDoom]()
- [Sintel](http://sintel.is.tue.mpg.de)

Explaination of COCO API.


[personal note of weichao](https://hackmd.io/AwQwLAbGDMBmIFoCcYDGBTBYCsAmJCARrtBFmIcEgOwAmaISSQA=)