# Related dataset

###### tags: `unrealcv`

How to annotate data, the standard format, compatibility and elegance. [A list of computer vision dataset](https://github.com/jbhuang0604/awesome-computer-vision)

[Ground truth we can provide](https://hackmd.io/IwMwJghgzA7BAMBaArMATAFkRgxmgnIgBwZRSLwBGmalwUyGlUQA)

- ImageNet
- PASCAL
- CityScape, several cities, outdoor
- COCO: caption, instance, category
- KITTI, virtual KITTI 
- Synthetia
- Sintel, Middlebury
- NYU indoor
- Human pose?
- ~~Face recognition?~~~
- 3D meshes for reconstruction.
- BSD, edge detection
- vispedia
- GTA dataset: the data format of this one. This is a bad quality dataset
- PASCAL 3D+
- MIT places

## Segmentation task

What is the popular way to save semantic segmentation ground truth?

8-bit png can only support 0-255? What if I need more? 
The COCO API is not a good way for storage, because the accuracy has been sacrified, but convert from object mask to COCO API is neccessary.


https://en.wikipedia.org/wiki/Indexed_color
https://en.wikipedia.org/wiki/Run-length_encoding

http://www.xrce.xerox.com/Our-Research/Computer-Vision/Proxy-Virtual-Worlds
Read this for some lessons.
---

TODO: Interactive annotation. How to get an image that requires annotation. 

How to release depth map, object instance mask. need a file to map from instance name to category.

I will provide one fundamental ground truth and use scripts to convert them to other specific dataset formats.

evaluation server

Find the overlap of these dataset, benchmarks and build a unified annotation. 

What if I find something I don't know the label?

Check UberNet

The generation of unseen objects.