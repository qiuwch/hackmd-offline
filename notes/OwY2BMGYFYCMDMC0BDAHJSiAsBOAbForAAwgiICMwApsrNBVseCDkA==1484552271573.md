# Done: Stereo - CVPR17 draft
###### tags: `unrealcv` `cvpr17`

## Introduction
Tell the story and attract reader. What we did, what problem we solved, our contribution. 
The importance and limitation of benchmark
The importance and unique strength of synthetic data.

**Fig: Teaser figure to show the big picture or just attract reader**
Idea: a few synthetic images, depth, mask. Show that synthetic data can help us spot the problem. @yizhang

## Related work

Stereo dataset, middlebury and KITTI @yizhang, number of images, our advantage.
Synthetic dataset, virtual KITTI, playing for data, Blender data, what is the difference and our strength
HAZOP: qiuwch
~~Stereo algorithms? Do you want to include methods we evaluated?~~

## Method

### Construct virtual world
**Fig: Interactive design tool.** @qiuwch show that others can easily do this
**Fig: Information we have, depth ground truth, object segmentation mask material property** @qiuwch, UrbanCity
**Equation: Compute disparity from depth** @yizhang and we verify it is accurate.

Need to briefly introduce Unreal Engine and UnrealCV for readers not familar with it. @qiuwch

### Case study
**Need to have a theoretical understanding of different methods. why we need these cases** @yizhang
**Equation: for these models**, MCCNN, DispNet, COR, SPS 

Impact and new(state of art) algorithms

Verify our diagnosis is consitent from the theoretical understanding, these theoretical understanding can be quoted from original paper.

**Fig: Show the cases we have, no texture, reflection, transparency.** @yizhang
**Question: How these theoretical cases can really related to real world performance.**

**TODO: Need to discuss the big structure**

Helpful for algorithm development. Why important, how we implement it.

### Attribute based evaluation
Extra information, the difference with others.

We compute mask from ground truth and use mask for evaluation. Several types of masks. 

The advantage this method, why it is important.
**Fig: Mask type: thin object, object boundary, material property** @qiuwch @yizhang 

**Is this large-scale evaluation consistent with manually designed cases, is it consitent with HAZOP and KITTI**, show our evaluation can transfer.

**Equation: How to compute mask**

## Experiment

**Fig: Screenshot for the scenes we use**
**How many images we generate, what is the rendering speed, resolution, etc.** 
**Table: compare our dataset with other dataset, number of images, types of ground truth**

**Equation: Evaluation metric** why we use, @yizhang, one or two representive

### Synthetic training
Weak result, is this worth a subsection, or just one paragraph is enough?

### Result for case study
**Which evalution metric we use, why and how we use them?** @yizhang
reflection-error, notexture-error, etc.

Opportunity for semantic info.

**Table: Design the table structure first, we can fill in numbers later** 
@yizhang top-priority
row: method name,   col: evaluation metric, reflection-error, all, notexture-error, report both.

What metric can be useful for our algorithm analysis

**Do we want to put FCRF to show it is good for thin object?**
**Table: Case study result**
One table or multiple tables?

Explain this table.
**Not only show our evaluation, the analysis is also very important**

### Result for attribute-based evaluation

Consider merging the experiment and method together?
**Table: table for different attributes**


## Conclusion and future work 

Need to submit supplementary report, which contains more images to show our dataset, and the analysis report for each method. 

## TODO:
- UrbanCity rendering @qiuwch
- Write introduction @qiuwch


<!--
Critical cases, where the algorithm will fail?

Our contribution
1. summarizing the challenges and evaluate algorithms.
2. Produce an dataset for traning and diagnosis.

Instead of using a number to evaluate an algorithm. We can produce a detailed report for an algorithm using the detailed information we have.

Also we provide higher level information as oracle for detailed analysis.

The Tesla crash.

Writing test case for algorithms.

With the observation and diagnosis tool we have. We propose a method to solve some of these issues. It solves the issue with a better model and also achive good performance in KITTI dataset.
-->