# Synthetic for Computer Vision

###### tags: `unrealcv`

The plan for this repository. What do I want to see from here?

paper, dataset, tool, articles, also discussion maybe? Reddit?

The purpose for this, start a project, or write paper?


This is a repo for tracking the progress of using synthetic images for computer vision research. If you found any important work is missing or information is not up-to-date, please edit this file directly and make a pull request.

This repository maintains a list of publications using synthetic data for computer vision research. Each publication is tagged with some keywords to make it easier to search.

See also: 
[Computer vision dataset index (YACVID)]( http://riemenschneider.hayko.at/vision/dataset/index.php?filter=+synthetic)

Other relevant, but not directly related resources can be found in [a separate page](). 

TODO: sync this page with github

What are useful tools for the community.

This page collects [tools](#tools), [dataset](#dataset).
Domain adaptation issue.

project, code and data

application, 


Realistic rendering, interaction, physical simulation.

tags: tool

## Simulation framework

DeepMind lab, OpenAI universe (OpenAI gym), UnrealCV, Malmo, UECraft for playing StarCraft


**Tips for editing this page**

**Hyperlink**: The paper id of this page is from google scholar. We use `div` id to localize a paper. For example, we add to the paper *"A naturalistic open source movie for optical flow evaluation."*.  

```html
<div id="butler2012naturalistic"></div>
```
So that we can use [a link](#butler2012naturalistic) to quickly jump to this paper.

```markdown
[the sintel paper](#butler2012naturalistic)
```


## Synthetic image dataset

- Semantic Pose using Deep Networks Trained on Synthetic RGB-D
([paper](http://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Papon_Semantic_Pose_Using_ICCV_2015_paper.pdf))
tags: 2015, 

- Physically-Based Rendering for Indoor Scene Understanding Using Convolutional Neural Networks 
([project](http://robots.princeton.edu/projects/2016/PBRS/))
tags: 2016, dataset

- SceneNet RGB-D: 5M Photorealistic Images of Synthetic Indoor Trajectories with Ground Truth
([paper](https://arxiv.org/pdf/1612.05079v3.pdf))
([project](https://robotvault.bitbucket.io/scenenet-rgbd.html))
([code](https://github.com/jmccormac/pySceneNetRGBD))
tags: 2017, dataset,

[Generating Realistic Camera Shake for Virtual Scenes](https://www.jvrb.org/past-issues/10.2013/3833)


**Click publication to jump to the paper title, detailed information such as code and project page will be provided together with pdf file.**

<div id="outline"></div>
## Outline
This is a brief summary of this page, you can quickly jump to what you want.
- [Synthetic image dataset](#dataset)
- [3D models](#models)
- [Tools](#tool)
- [Resource Index](#resource)
- [Reference](#reference)

<div id="dataset"></div>

## 1. Image dataset [↑](#outline)

| Name          | Publication                         |
|:--------------|:------------------------------------|
| Virtual KITTI | [CVPR2016](#gaidon2016virtual)      |
| Synthetia     | [CVPR2016](#ros2016synthia)         |
| Sintel        | [ECCV2012](#butler2012naturalistic) |
| SceneFlow     | [CVPR2016](#mayer2015large)         |


<div id="models"></div>

## 2. 3D Model Repository [↑](#outline)

Realistic 3D models are critical for creating realistic and diverse virtual worlds. Here are research efforts for creating 3D model repositories.

- ShapeNet       [ArXiv](#chang2015shapenet)  
- 3dscan         [ArXiv](#choi2016large)      
- seeing3Dchairs [CVPR2014](#aubry2014seeing)


<div id="tool"></div>

## 3. Tools [↑](#outline)

- Render for CNN 
Blender, [ICCV2015](#su2015render)
- UETorch
Unreal Engine 4(UE4), [ICML2016](#lerer2016learning)
- UnrealCV 
UE4, [ArXiv](#qiu2016unrealcv)
- VizDoom
Doom, [ArXiv](#kempka2016vizdoom)

<div id="resource"></div>

## Resources [↑](#outline)

ECCV 2016 Virtual/Augmented Reality for Visual Artificial Intelligence (VARVAI) workshop [link](http://adas.cvc.uab.es/varvai2016/)

Virtual Reality Meets Physical Reality:
Modelling and Simulating Virtual Humans and Environments
Siggraph Asia 2016 workshop [link](http://sigvr.org/)

## Misc. [↑](#outline)

- RealismCNN [github](https://github.com/junyanz/RealismCNN)
- Abnormality Detection in Images(http://paul.rutgers.edu/~babaks/abnormality_detection.html)

# Related topics [↑](#outline)
## Domain Transfer

## Reinforcement Learning

<div id="reference"></div>

## People
Great research always comes from great researchers. This is a short list of researchers that are combining computer vision with virtual worlds.

# Reference [↑](#outline)

If you want to edit this README file. The div id is bib citekey from google scholar, use div id makes it easier to reference a work in this document.

## Non publication
universe.openai.com

## 2016
(Total=14)
- CLEVR: A Diagnostic Dataset for Compositional Language and Elementary Visual Reasoning
	([pdf](https://arxiv.org/abs/1612.06890))

- SceneNet RGB-D: 5M Photorealistic Images of Synthetic Indoor Trajectories with Ground Truth

- Procedural Generation of Videos to Train Deep Action Recognition Networks
	([pdf](https://arxiv.org/abs/1612.00881))
	([project](http://adas.cvc.uab.es/phav/))

- TorchCraft: a Library for Machine Learning Research on Real-Time Strategy Games
	([pdf](https://arxiv.org/abs/1611.00625))
	([code](https://github.com/TorchCraft/TorchCraft))

- A Virtual Reality Platform for Dynamic Human-Scene Interaction. 2016   
	([pdf](https://xiaozhuchacha.github.io/projects/siggraphasia16_vrplatform/vrplatform2016siggraphasia.pdf))
	([project](https://xiaozhuchacha.github.io/projects/siggraphasia16_vrplatform/index.html))

- ResearchDoom and CocoDoom: Learning Computer Vision with Games. 2016   
	([pdf](https://arxiv.org/pdf/1610.02431.pdf))
	([project](www.robots.ox.ac.uk/~vgg/research/researchdoom/))

<div id="ros2016synthia"></div>
-   The SYNTHIA dataset: A large collection of synthetic images for semantic segmentation of urban scenes.  2016
	 ([pdf](http://www.cv-foundation.org/openaccess/content_cvpr_2016/html/Ros_The_SYNTHIA_Dataset_CVPR_2016_paper.html))
	 ([project](http://synthia-dataset.net/))
	 ([citation:4](http://scholar.google.com/scholar?cites=9178628328030932213&as_sdt=2005&sciodt=0,5&hl=en))

<div id="gaidon2016virtual"></div>
-   Virtual Worlds as Proxy for Multi-Object Tracking Analysis.  2016   
	 ([pdf](http://arxiv.org/abs/1605.06457))
	 ([project](http://www.xrce.xerox.com/Research-Development/Computer-Vision/Proxy-Virtual-Worlds))
	 ([citation:5](http://scholar.google.com/scholar?cites=11727455440906017188&as_sdt=2005&sciodt=0,5&hl=en))

-   Playing for data: Ground truth from computer games.  2016   
	 ([pdf](http://link.springer.com/chapter/10.1007/978-3-319-46475-6_7))
	 ([citation:1](http://scholar.google.com/scholar?cites=12822958035144353200&as_sdt=2005&sciodt=0,5&hl=en))

-   Play and Learn: Using Video Games to Train Computer Vision Models.  2016   
	 ([pdf](http://arxiv.org/abs/1608.01745))
	 ([citation:1](http://scholar.google.com/scholar?cites=16081073673799361643&as_sdt=2005&sciodt=0,5&hl=en))

<div id=""></div>
-   ViZDoom: A Doom-based AI Research Platform for Visual Reinforcement Learning.  2016    
	([:octocat:code](https://github.com/Marqt/ViZDoom))
	([pdf](http://arxiv.org/abs/1605.02097))
	([project](http://vizdoom.cs.put.edu.pl/))
	([citation:4](http://scholar.google.com/scholar?cites=4101579648300742816&as_sdt=2005&sciodt=0,5&hl=en))

<div id="choi2016large"></div>
-   A large dataset of object scans.  2016   
	 ([pdf](http://arxiv.org/abs/1602.02481))
	 ([project](http://redwood-data.org/3dscan/))
	 ([citation:6](http://scholar.google.com/scholar?cites=5989950372336055491&as_sdt=2005&sciodt=0,5&hl=en))

<div id="qiu2016unrealcv"></div>
-   UnrealCV: Connecting Computer Vision to Unreal Engine  2016    
	<span class="octicon octicon-mark-github"></span>
	([:octocat:code](https://github.com/unrealcv/unrealcv))
	([project](http://unrealcv.github.io))
	([pdf](http://arxiv.org/abs/1609.01326))   

<div id="lerer2016learning"></div>
-   Learning Physical Intuition of Block Towers by Example  2016   
	([:octocat:code](https://github.com/facebook/UETorch))
	([pdf](http://arxiv.org/abs/1603.01312))
	([citation:12](http://scholar.google.com/scholar?cites=12846348306706460250&as_sdt=2005&sciodt=0,5&hl=en))

-   Target-driven Visual Navigation in Indoor Scenes using Deep Reinforcement Learning  2016   
	 ([pdf](http://arxiv.org/abs/1609.05143))   

## 2015
(Total=3)

-   A Large Dataset to Train Convolutional Networks for Disparity, Optical Flow, and Scene Flow Estimation.  2015    
	 ([pdf](http://arxiv.org/abs/1512.02134))
	 ([citation:9](http://scholar.google.com/scholar?cites=16431759299155441580&as_sdt=2005&sciodt=0,5&hl=en))

<div id="su2015render"></div>
-   Render for cnn: Viewpoint estimation in images using cnns trained with rendered 3d model views.  2015   
	([:octocat:code](https://github.com/ShapeNet/RenderForCNN))
	([pdf](http://www.cv-foundation.org/openaccess/content_iccv_2015/html/Su_Render_for_CNN_ICCV_2015_paper.html))
	([citation:33](http://scholar.google.com/scholar?cites=1209553997502402606&as_sdt=2005&sciodt=0,5&hl=en))

<div id="chang2015shapenet"></div>
-   Shapenet: An information-rich 3d model repository.  2015    
	 ([pdf](http://arxiv.org/abs/1512.03012))
	 ([project](http://shapenet.cs.stanford.edu/))
	 ([citation:27](http://scholar.google.com/scholar?cites=1341601736562194564&as_sdt=2005&sciodt=0,5&hl=en))

## 2014
(Total=2)

-   Virtual and real world adaptation for pedestrian detection.  2014    
	 ([pdf](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6587038))
	 ([citation:46](http://scholar.google.com/scholar?cites=2637402509859183337&as_sdt=2005&sciodt=0,5&hl=en))

<div id="aubry2014seeing"></div>
-   Seeing 3d chairs: exemplar part-based 2d-3d alignment using a large dataset of cad models.  2014   
	([:octocat:code](https://github.com/dimatura/seeing3d))
	([pdf](http://www.cv-foundation.org/openaccess/content_cvpr_2014/html/Aubry_Seeing_3D_Chairs_2014_CVPR_paper.html))
	([project](http://www.di.ens.fr/willow/research/seeing3Dchairs/))
	([citation:110](http://scholar.google.com/scholar?cites=18030645502969108287&as_sdt=2005&sciodt=0,5&hl=en))

## 2013
(Total=1)

-   Detailed 3d representations for object recognition and modeling.  2013   
	 ([pdf](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6516504))
	 ([citation:67](http://scholar.google.com/scholar?cites=6595507135181144034&as_sdt=2005&sciodt=0,5&hl=en))

## 2012
(Total=1)

<div id="butler2012naturalistic"></div>

- A naturalistic open source movie for optical flow evaluation.  2012 
([pdf](http://link.springer.com/chapter/10.1007/978-3-642-33783-3_44))
([project](http://sintel.is.tue.mpg.de/))
([citation:227](http://scholar.google.com/scholar?cites=15124407213489971559&as_sdt=20000005&sciodt=0,21&hl=en))
tags: dataset, sintel

## 2010
(Total=1)

-   Learning appearance in virtual scenarios for pedestrian detection.  2010   
	 ([pdf](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5540218))
	 ([citation:79](http://scholar.google.com/scholar?cites=17243485674852907889&as_sdt=2005&sciodt=0,5&hl=en))
     
<div id="testdiv"></div>

## 2007
(Total=1)

-   Ovvv: Using virtual worlds to design and evaluate surveillance systems.  2007   
	 ([pdf](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=4270516))
	 ([citation:58](http://scholar.google.com/scholar?cites=3459961090644684583&as_sdt=2005&sciodt=0,5&hl=en))

The OpenAI universe, GTA environment.
The Udacity driving environment.


Related projects, dataset and code
GAN generate synthetic images
OpenAI universe drive car
Add a google scholar search link for each paper
Add https://xiaozhuchacha.github.io/projects/siggraphasia16_vrplatform/vrplatform2016siggraphasia.pdf and its cited work
Add https://xiaozhuchacha.github.io/projects/siggraphasia16_vrplatform/vrplatform2016siggraphasia.pdf and its cited work
http://adas.cvc.uab.es/varvai2016/