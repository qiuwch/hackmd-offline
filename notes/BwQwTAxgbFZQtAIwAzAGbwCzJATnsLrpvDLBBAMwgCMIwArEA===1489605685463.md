# UnrealStereo high-level summary 

## Contribution

- precise **control** of nuisance factors in the image, provide this ability to other researchers develop and test. experimental design
- largely reduce the cost of the stress test. controlled stress test with comparision to KITTI
- quantitively evaluate the effect of challenging factors / assumption violation
- support many realistic 3D contents, offer training resources.

Future work, training algorithms with more semantic information in use.

## Technical contribution 

How hard to achieve this



difference, important, solve some problem

## What we did

1. New dataset, data generation tool
2. ~~Point the assumption in stereo~~, generate challenging cases to help them analyze and understand these cases
4. Our result can be validated in KITTI, a new way to analyze algorithm, justification
5. Rank algorithms and get some conclusions


## Difference with others

1. Data: Users can generate more images. Photorealistic including many visual effects. Control material property 

~~Virtuall KITTI~~, Flying Things, Middlebury, KITTI 

Flying things (random + cars): realistic rendering technique, but not our contribution. visual artist design semantically right, organization according to real photo, not random. Images comparable but with generation tool. 

Background is a picture, so no realistic lighting. Technically the graphics details (TODO). Realistic effect + semantic structure.

Middlebury: large scale (learning, testing cover more cases), no reflective, transparent.

KITTI: Missing groundtruth, for example transparency. Long tail distribution. 

V.S. real: provide precise control in testing stage, control level, create different situations. We can verify the assumption of our algorithms. debate of harzadous.

HCI/Bosch Robust Vision Challenge, HAZOP: Challenging images for stereo, provide corner cases to overcome the long tail distribution in real world. 
Cost, high cost -> no cost. Ground truth accuracy, hard to get dense. Extreme cases is possible, precise control is not possible. Flat surface, curve surface, many examples. Extreme cases for real is not too hard. Related information we can not get (object boundary, semantic). Calculate the cost and say why the cost reduction is important.


## Why dataset is important

large dataset is important, learning based algorithm
benchmark is important?


experimental design.
trainsit
for learning,
cirruculum 

Not sure when we need to provide more labeling data. Active data collection.

Qi: 
select examples and tune
Not only test on extreme cases

Verify the theory.
Try and see the result.
Validate whether the model is right.

Our attempt to 
The learning based algorithm.

new experimental paradigm.

Different characteristic of deep learning.

Good/bad boundary
CAD has the potential to do this.
Train on synthetic and test on real.

Simple cases (experimental design)

systematical exploration. therotical framework. systematically generate based on this framework.