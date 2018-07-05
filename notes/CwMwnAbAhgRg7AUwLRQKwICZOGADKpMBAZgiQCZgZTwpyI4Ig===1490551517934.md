# ICCV Stereo plan - Yi Zhang

###### tags: `iccv17`, `plan`


- What problem we are solving?

Stereo is not robust to harzadous factors. No way to measure how robust an algorithm is.

- Why this is an important problem?

The failure will cause serverous loss.

- How well we solved this problem, what is our method

- Evidence to show we solved this problem well.


- Conclusion: contribution?

## Some thoughts

1. Rebuttal, KITTI hazardous cases.

annotation + evaluation 

the issue of reflection. water + TV + car, virtual -> real

real annotation
Use real data to justify, need more annotation, what annotation we already have? (TODO)

reflection, whether it can solve.

2. More methods?

ELAS, Vanila Lucas Kanade, Even performance much better, framework similar, robustness not huge improvement. R1 stereo method asumption. 
Classical methods, such as the very old one and the one in OpenCV, industry level, we can say the performance is better, but robustness is the same.
The CAD method. Semantic is the future direction. Prove not hallucinating depth. (TODO)

CAD method. 90+, R1 hahucilation is dangerous. High level guide, semantic segmentation, CAD model guide. Confident information instead of guessing. Chanllenge level. Robustness (TODO)


```python
compute_result(method, l, r) # MATLAB, skip this
evaluate_result(method, l, r) # read from file
```

DispNet, long range context, local feature missing textureless , superpixel

3. Robustness, finetune

Finetune fit better to our data. Whether the robustness change. 
The fine tuning issue, better, but the robustness is the same?

4. Small number images, 10 image pairs, 500

What are some clear take home message?
What we are going to release.

What is our technical novelty?

Questions from reviewers.

**Technical contribution**, how to say, tell how hard it is to make sure these working well

**Theoretical contribution**

Compare with other synthetic dataset, what is our technical contribution?


## Release list

What do we want to release.

- Evaluation code + evalutation server? Code to draw the radar plot?
    Generate new data for challenge
    we only need the estimation for evaluation.
- The real images annotation? Specular, transparent, no texture 
    KITTI 2012 reflective
    Example images.
- Synthetic images with GT (how many). 2015 - 200, intersect
    1. Factor control cases, each image with hazardous level, 10 image pair
    (TODO)
    2. Images with hazardous region computed
    3. Images with gt.  10k, transparency 10k+ photorealistic images + image generation tool
    
No need for different scenes -> merge together. Object ID. object mask. (TODO)