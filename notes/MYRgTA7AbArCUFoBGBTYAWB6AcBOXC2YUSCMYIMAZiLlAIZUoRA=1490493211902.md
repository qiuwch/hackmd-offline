# Dataset plan - Matt

###### tags: `unrealcv`, `plan`

- object mask
- API
- how to store data

- make it extensible, 

Extensible

object mask.
- 8bit png, indexed file. nice visualization

0-255, 256 objects per image. 16-bit image
- save one image.
- save objects binary mask

image size 256 ** 2
one 8-bit image: (256 * 256 * 8)
256 binary mask: (256 * 256 * 1) * 256 (objects)

color png file.

binary mask -> compression, RLE run length encoding

## Storage decision choices
1. one object-mask image, 16-bit
2. save multiple binary masks, use RLE to compress 

Dataset level meta file, json
object -> category map

Image level meta file


## Visualization
- object color
- category color
- disable some not useful category

## API
For computer vision researcher. 
Start COCO

## Object category label.

https://github.com/Microsoft/AirSim