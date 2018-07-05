# Count

1. The visual realism of Unreal Engine.
 
Thanks for reviewer 1 to point out the realism issue. This is an important topic for our work and the adoptation of synthetic images in computer vision. It is hard to explain the realism and sometimes subjective. The visual realism of a synthetic image is dominated by two factors, rendering and modeling, we will explain UE4 from these two perspectives. 
 
In terms of rendering, path tracing is a more realistic rendering technique than the deferred shading used in Unreal Engine. Theoretically, Renders, like PBRT or Mitsuba, can produce more realistic images given enough computational time. But that does not mean the realism of UE4 is not enough.
 
For specularity, the complex lighting interaction in the scene is precomputed and cached. That’s why the engine can achieve realistic rendering with a real-time performance. The physically based material system makes it easy to create and share realistic high-specular materials like metal and plastic. For transparency, UE4 can model the refraction of transparent objects. Althogh it can not accurately model the caustics effect caused by a complex transparent object, it is enough for the common cases we have with car windshields and building windows. 
 
A picture is more than a thousand words, if the figure in the paper is not convincing enough.  ue4arch.com shows some examples (videos and images) of realistic UE4 projects,  The car customization project is a good example to showcase the transparency and specularity effects in UE4.
 
In terms of modeling, the rich realistic resources of UE4 are incomparable. 3D models are the input of the renderer. Without physically correct models, it is not possible to get realistic images no matter how good the renderer is. UE4 uses a physically based material system, which UnrealStereo depends on to adjust the material property. The 3D models we can get from UE4 contain great details, such as the roughness of a leather, the physically correct materials like metal and plastic. These data are captured from real objects or created by experienced visual artist. The huge user base of UE4 makes these resources cheaper and easy to access.
 
UE4 and UnrealStereo are not producing the best quality images, it is lower than the best in the movie industry. But they are the most suitable tools for this moment. When the Sintel optical flow dataset is developed. Path tracing is already a popular technique and Blender has a PBRT-based render called Cycles. But not much 3D resources to feed the renderer, making it not very useful. The virtual reality community is trying to build authentic virtual worlds for users and most of these resources are delivered through UE4. Using offline renderers is a good idea, but given the current status, we will stick with UE4. 
 
Last but not the least, no matter what rendering approach we choose, it is important to validate the result on real images. The result we get from synthetic and the KITTI dataset shows consistent results.
 
It might be appealing to think no matter how realistic the synthetic images to the human, there is still unnoticable difference making them not useful. This might be true, but this is also a sign showing the system is not robust enough, and it might be easily fooled with some invisible noise to human.
 
This diagnosis work is a part of a larger project, which will extend the synthetic images to more applications. These applications include interaction with objects, physics simulation, etc. These tasks can be combined with diagnoisis to create vision system useful for the real world. Those tasks are hard to achieve with an offline renderer.