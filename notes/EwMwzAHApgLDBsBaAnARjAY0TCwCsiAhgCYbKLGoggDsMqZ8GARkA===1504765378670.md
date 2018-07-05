# Deleted
---
layout: single
permalink: /index.html
---

UnrealCV is a project to help computer vision researchers build virtual worlds using Unreal Engine 4 (UE4). It extends UE4 with a plugin by providing:

1. A set of UnrealCV commands to interact with the virtual world.
2. Communication between UE4 and an external program, such as Caffe.

UnrealCV can be used in two ways. The first one is using a compiled game binary with UnrealCV embedded. This is as simple as running a game, no knowledge of Unreal Engine is required. The second is installing UnrealCV plugin to Unreal Engine 4 (UE4) and use the editor of UE4 to build a new virtual world.

Please read [Tutorial: Getting Started](http://docs.unrealcv.org/en/master/tutorials/getting_started.html) to learn using UnrealCV.

<center>
<img src="http://unrealcv.org/images/homepage_teaser.png" alt="annotation"/>
Images generated from the technical demo <a href="http://docs.unrealcv.org/en/master/reference/model_zoo.html#realisticrendering">RelisticRendering</a><br>
</center>

## Tutorials

- [Getting Started](http://docs.unrealcv.org/en/master/tutorials/getting_started.html) - The basics of using UnrealCV, start from here.

- [Generate an image dataset with ground truth](http://docs.unrealcv.org/en/master/tutorials/generate_images_tutorial.html) - An iPython notebook showing how to generate an image dataset with rich ground truth from a virtual scene.

- [Integrate with Faster-RCNN](http://docs.unrealcv.org/en/master/tutorials/faster_rcnn.html) - Show how to use images from a video game for testing faster-RCNN.

- [Integrate with OpenAI Gym](https://github.com/zfw1226/gym-unrealcv) - Show how to get started with OpenAI Gym interface for reinforcement learning tasks.

- [Install Plugin to UE4](http://docs.unrealcv.org/en/master/plugin/install.html) - How to install UnrealCV plugin into UE4.

## Reference

- [Architecture](http://docs.unrealcv.org/en/master/reference/architecture.html) - Technical Details of UnrealCV

- [Command List](http://docs.unrealcv.org/en/master/reference/commands.html) - All available commands provided in UnrealCV

## Citation

If you found this project useful, please consider citing our paper

```bibtex
@article{qiu2016unrealcv,
  Author = {Qiu, Weichao and Yuille, Alan},
  Journal = {arXiv preprint arXiv:1609.01326},
  Title = {UnrealCV: Connecting Computer Vision to Unreal Engine},
  Year = {2016}
}
```

## Contact

UnrealCV is an open-source project created by students from Johns Hopkins University and Peking University under the supervision of [Prof. Alan Yuille](https://ccvl.jhu.edu/team/) and [Prof. Yizhou Wang](http://www.idm.pku.edu.cn/staff/wangyizhou/). It is maintained by the UnrealCV team, see [the team member list](contact.html).

If you have any suggestion or interested in using UnrealCV, please [contact us](contact.html).
