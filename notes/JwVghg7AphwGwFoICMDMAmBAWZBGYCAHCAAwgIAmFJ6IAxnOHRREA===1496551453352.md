# ICCV17 Rebuttal

Thanks for useful comments from all reviewers. We will polish our paper and remove redundancy to make it more concise. We address a few major points first and then the discussion is organized by reviewer number.
 
1. The visual realism of Unreal Engine.
 
Thanks for reviewer 1 to point out the realism issue. This is an important topic for our work and the adoption of synthetic images in computer vision. It is hard to explain the realism and sometimes subjective. The visual realism of a synthetic image is dominated by two factors, rendering and modeling, we will explain UE4 from these two perspectives. 
 
In terms of rendering, path tracing is a more realistic rendering technique than the deferred shading used in Unreal Engine. Theoretically, renders like PBRT or Mitsuba can produce more realistic images given enough computational time. But that does not mean the realism of UE4 is not enough.
 
For specularity, the complex lighting interaction in the scene is precomputed and cached in UE4. That is why the engine can achieve realistic rendering with a real-time performance. The physically based material system makes it easy to create and share realistic high-specular materials like metal and plastic. For transparency, UE4 can model the refraction of transparent objects. Although it cannot accurately model the caustics effect caused by a complex transparent object, it is enough for the common cases we have with car windshields and building windows. 
 
A picture is more than a thousand words, if the figure in the paper is not convincing enough.  ue4arch.com shows some examples (videos and images) of realistic UE4 projects. The car customization project is a good example to showcase the transparency and specularity effects in UE4.
 
In terms of modeling, the rich realistic resources of UE4 are incomparable. 3D models are the input of the renderer. Without physically correct models, it is not possible to get realistic images no matter how good the renderer is. UE4 uses a physically based material system, which UnrealStereo depends on to adjust the material property. The 3D models available from UE4 contain great details, such as the roughness of a leather, the physically correct materials like metal and plastic. These data are captured from real objects or created by experienced visual artist. The huge user base of UE4 makes these resources cheaper and easy to access.

UE4 and UnrealStereo are not producing the best quality images, it is lower than the best in the movie industry. But they are the most suitable tools for this moment. When the Sintel optical flow dataset is developed. Path tracing is already a popular technique and Blender has a PBRT-based render called Cycles. But not much 3D resources to feed the renderer, making it not very useful. The virtual reality community is trying to build authentic virtual worlds for users and most of these resources are delivered through UE4. Using offline renderers is a good idea, but given the current status, we will stick with UE4. 
 
Last but not the least, no matter what rendering approach we choose, it is important to validate the result on real images. The result we get from synthetic and the KITTI dataset shows consistent results.
 
It might be appealing to think no matter how realistic the synthetic images to the human, there is still unnoticeable difference making them not useful. This might be true, but this is also a sign showing the system is not robust enough, and it might be easily fooled with some invisible noise to human.
 
This diagnosis work is a part of a larger project, which will extend the synthetic images to more applications. These applications include interaction with objects, physics simulation, etc. These tasks can be combined with diagnosis to create vision system useful for the real world. Those tasks are hard to achieve with an offline renderer.
 
2. Missing related work (Rev.1) 

<!-- THE PROBLEM WE ARE TRYING TO SOLVE THE ANALYSIS OF ROBUSTNESS -->

CONTROL THE NOISE LEVEL. NUISANCE FACTOR. THEY CONTROL GAUSSIAN, WE CONTROL MATERIAL PROPERTY. 


?? IMAGE -> TOY IMAGE -> REALISTIC IMAGE
COMPARE WITH GCPR 2013. THIS PAPER USES grating IMAGE (ASK ALAN HOW TO CALL THIS TYPE OF IMAGE??) TO PERFORM THE EXPERIMENT. THESE IMAGES ARE USEFUL FOR PURELY THEORETICAL ANALYSIS. GENERALIZATION TO REAL WORLD APPLICATION REQUIRES BETTER DATA AS WE SHOW IN THE PAPER. AND THIS PAPER CLEARLY POINTED OUT "the potential of using synthetic data for evaluation in computer vision has not yet been fully utilized" AND OUR DATA IS FROM THE REALSTIC RENDERING PERSPECTIVE.

<!-- THE CONTRIBUTION IS WE CAN CONTROL HARZAROUS LEVEL TO STUDY THE ROBUSTNESS OF VISION ALGORITHM, WHICH HAS NEVER BEEN DONE BEFORE -->


The Middlebury dataset has controlled image pairs, but it is difficult to get these images in real setup. While our tool makes it easy to generate large amount of controlled images in different situations. Neilson and Yang (CVPR 2008) has different types of texture, but they did not study the effects of textureless surfaces or varying the level of texturelessness. Synthetic dataset by Peris et al. (ICPR 2012) contains different illuminations, but they did not use them to analyze robustness of stereo algorithms. Artificial dataset by Haeusler and Kondermann (GCPR 2013) shows preliminary results of using synthetic images to diagnose stereo algorithms. But the realism and the size of their data is limited and they did not verify the conclusion on real images. 

[18] PROPOSED SOME HARZARDOUS REGIONS. OUR METHOD PROVIDES THE CONTROL OF HARZARDOUS LEVEL, WHICH [18] CAN NOT PROVIDE.

and we use the same definition for occlusion areas with [18]. 


These related work are useful for the paper and can make it clearer, and we will add them to the revised version.


The proposed evaluation regions in [18] and by Honauer et al. are useful, 


3. BadPix scores (Rev.1)

We think the BadPix metric is a useful metric which shows characteristics not observed from the EPE metric we used. We will add it to Tab.2 and Tab.3 in the revised version.

4. Test on Middlebury dataset (Rev.1) 

It is helpful to validate our result on more real-world dataset, such as Middlebury. The issue is the Middlebury lacks object level segmentation, so we need to do extra annotation for this experiment. Actually, we are considering extending our experiment to a new dataset developed by Raquel’s group. 

4. How easy to use UnrealStereo (Rev.2)

The tool can run both in Linux and windows. The hardware requirement comes from UE4. The minimum requirement is memory>8G, GPU>GTX470 from UE4 documentation. Machines used for training deep network would easily meet this requirement. 

UnrealStereo is designed to be easy to use for researchers without UE4 background. We provide tutorials going through the steps of generating data and controlling hazardous factors. These tutorials also cover the minimal required knowledge of UE4. It usually takes a few hours to go through the tutorials based on the experience we have in our lab. We will link these resources in the final version which does not require anonymity. We will also revise Sec.3.1 to make this clearer.

The speed of generating stereo pairs is 2 fps. The fly path can be generated by (1) navigating in the scene and record trajectory with our script; (2) scripts using rules.

5. Expediency? of the approach (Rev.3) 

The effects of image sensors, calibration and image noise are indeed important and have been studied in former stereo datasets already. In our paper we have a different focus on hazardous regions and robustness analysis. They are also important and did not get enough attention. We will try to include more challenges, such as the sensor difference, but it is not the core of the idea. 

To validate our evaluation results, we performed experiments on the real-world KITTI dataset (see Sec.4.1, L.621). 

6. Reproducibility (Rev.3)

As mentioned in L.535, both the data used in the experiments and data generation tool will be made public available soon. And we will make this clearer.

7. Misc.
-	(Rev.1) The size of the images is 640x480 and the disparity ranges of our scenes are mostly comparable to KITTI (<200). So the comparison to the KITTI errors is not distorted.
-	(Rev.2) Multiview can be done through pause the simulation and move camera to different positions. 
-	(Rev.2) The stereo ground truth has subpixel accuracy, because we have very accurate depth and camera information.

----------------
To AC:

The reviewer 3 missed some important points in the paper and seems did not read the paper careful enough.

1.	We showed the validation result on KITTI dataset in Sec.4.1 so we cannot agree with the comment from reviewer 3, "In particular, it appears a validation of the approach (as suggested in ll.842f) has not been tackled in the paper.". He probably missed this experiment when reading the paper.

2. He said "It appears it would not be possible to reproduce the results, as the generated datasets (or the data needed to generate these datasets) will not be made available." This is purely conjecture since we already promise we will release our code and data (in L.165, L.258, L.535).
