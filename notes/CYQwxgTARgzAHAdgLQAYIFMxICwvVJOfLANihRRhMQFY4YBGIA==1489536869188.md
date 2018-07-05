# Shader development

###### tags: `unrealcv`, `UE4` 

How to write a shader, how to deploy a shader?

Should the output of a shader be combined with other shaders?

How many different shader languages?

HLSL?

https://en.wikipedia.org/wiki/High-Level_Shading_Language. This is from microsoft.

The equivalent is GLSL.

The [shader development](https://docs.unrealengine.com/latest/INT/Programming/Rendering/ShaderDevelopment/) of Unreal Engine.

usf, unreal shader file.

[how to debug usf file](https://forums.unrealengine.com/showthread.php?6719-Debugging-USF-(Unreal-Shader-Files))

Should I learn renderdoc?

The microsoft shader documentation [in MSDN](https://msdn.microsoft.com/en-us/library/bb509561(v=VS.85).aspx).

The github [shader plugin project](https://github.com/Temaran/UE4ShaderPluginDemo)

[SV_InstanceID](https://social.msdn.microsoft.com/Forums/en-US/32d524a6-09eb-4585-a705-17298aff28ff/cant-use-svinstanceid-in-a-vertex-shader?forum=wingameswithdirectx)

Read this page about [instance id](https://msdn.microsoft.com/en-us/library/windows/desktop/bb509647(v=vs.85).aspx)
and [this page about instance id](https://msdn.microsoft.com/en-us/library/windows/desktop/bb205118(v=vs.85).aspx)

The [HLSL index page in MSDN](https://msdn.microsoft.com/en-us/library/windows/desktop/bb509561(v=vs.85).aspx)

InstanceID is visible to VS.

[gl_InstanceID](https://www.khronos.org/opengl/wiki/Built-in_Variable_(GLSL))

After setting up the information, I need to output the result as image or other formats.

[InstanceID in UE4](https://answers.unrealengine.com/questions/463074/per-instance-id-for-static-mesh-instances.html).

Come to think of it, wouldn't the actor position node give you the information necessary to do this check too? This might be very interesting.

PostProcess material can not access the material instance information.

[Instance ID in postprocess](https://docs.unrealengine.com/latest/INT/Engine/Rendering/PostProcessEffects/PostProcessMaterials/#blendingbetweendifferentmaterialinstances) see the input. What can the input be? how to change it?
