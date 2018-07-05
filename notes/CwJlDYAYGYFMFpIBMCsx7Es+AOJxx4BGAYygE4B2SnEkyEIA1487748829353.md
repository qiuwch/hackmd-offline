# Done: UnrealCV poster outline

## Questions

### Technical
1. Accurate
Depth, 0-256, HDR save. We can get projection matrix.

2. How to get image, save to disk and return filename
Plan to return binary, support hdf5, json to export complex data structure.

3. Speed
10 - 20 fps, extend 40 - 50fps.

4. Optical flow
No.

5. Precise time tick control

6. Multiple cameras
Will support, under development

7. Do you need game project.
Yes. our limitation.

### Non-technical

1. Vision for this project

Make virtual worlds easy to create, use and share. Provide basic APIs and maintain it and find collaboration. We will also use this in our research.

2. Where to get Unreal resources.

See link in the poster. turbosquid, UE market, demos.

3. What do you think about virtual data for CV.

It has limitations, 1. transfer, 2. some are hard to simulate. 

But have great potentials. 1. Due to VR, more models, easier to create. 2. GPU and algorithm, make it more real. 3. It can do many things real images can not.

4. Unity, Unreal and Blender.
Do not trash Unity. Blender: bad, can not provide interactivity, not good industry support. good, offline rendering, realistic. 

We just pick one. Unreal Engine is open source.

Take the email from skydio

5. Development plan

    1. Collision. 2. Better multiple cameras, 3. Project matrix. 4. Stability and speed.

If need more features, contact us.



[2 minutes workshop spotlight](https://docs.google.com/presentation/d/1-JQ0RNOrM7JLQePLdqBvcO9DhXjJ7LtTXN2tM9JSxfI/edit#slide=id.p) About 3 - 5 slides

## Things to think about
- Audience
Expert and non-expert, I don't care much expert, I care about my users.

- Application
Show how to generate image dataset
Show diagnosis

- Feature
Easy to use, platform support

- What
An Unreal Engine plugin

- Why
Making creating virtual world easier

- Detail
The communication, the 

- Loved by the community and actively maintained.

Related work, if you interested in, see http://github.com/qiuwch/synthetic-computer-vision for more related work.

Do not trash unity!!!!

A 10 lines python code (without comments)
```python
import json; camera_trajectory = json.load(open('camera_traj.json'))
from unrealcv import client
client.connect()
# Get object information
obj_info = client.request('vget /objects')
for [loc, rot] in camera_trajectory:
    # Set position of the first camera
    client.request('vset /camera/0/location {x} {y} {z}'.format(**loc))
    client.request('vset /camera/0/rotation {pitch} {yaw} {roll}'.format(**rot))
    # Get image and ground truth
    modes = ['lit', 'depth', 'object_mask']
    [im, dep, obj] = [client.request('vget /camera/0/%s' % m) for m in modes]
    print ['%s is saved to %s' % (k, v) for (k,v) in zip(modes, [im, dep, obj])]
```

### Something small
- A QR code to include links of the poster
Generate a QR code using http://www.qrstuff.com/

## Abstract
UnrealCV is a tool to help computer vision researchers building virtual worlds. 

What is the benefit of having a virtual world?

Should we add more discussion?

## Show the annotation image

## Architecture
The image to show details

## UnrealCV commands

## Conclusion
