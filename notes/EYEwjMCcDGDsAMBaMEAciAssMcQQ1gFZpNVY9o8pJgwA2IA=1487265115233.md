# Discussion with Chi Li

The 3D car parsing project with NEC.

The network is supervised in many layers, each layer is for one concept. For example: viewpoint, shape, visibility, etc. 

The technical requirements in this project is producing the visibility, the keypoint location in 2D, 3D, etc. If we want to use UE4 for this, we need the `import`, `keypoint export`(also required for the text project), `occlusion detection`. 

TODO: produce a city scene with multiple cars. Also think whether easy to produce the information needed.

1. The multiple car parsing project for future
2. Realistic phsyics simulation project

The mentioned paper [End-to-end people detection in crowded scenes](https://arxiv.org/pdf/1506.04878v3.pdf)

## 2/15

Get some annotated models from ShapetNet. Try them and see how to get keypoints annotation.