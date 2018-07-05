# UE4 Rendering

Some related class

- SceneCapturePixelShader
- the class `USceneCaptureComponent2D`, declared in `SceneCapture2D.h` and defined in `SceneCaptureComponent.cpp`.
    Useful functions of this class 
    
    - `CaptureSceneDeferred()` this will be called in every tick if `bCaptureEveryFrame` is enabled.
    - `CaptureScene()` this will capture immediately. This function calls `FSceneInterface::UpdateSceneCaptureContents()`.
    
- `FSceneInterface`, declared in `SceneInterface.h`, and defined in `SceneInterface.cpp`.
    - `UpdateSceneCaptureContents()` this is abstract.

- `FScene`, declared in `ScenePrivate.h` and defined in `RendererScene.cpp` and `SceneCaptureRendering.cpp`, which is very weird organization.
    - `UpdateSceneCaptureContents()` defined in `SceneCaptureRendering.cpp`
        Get the viewpoint in this function. CaptureComponent can use a custom projection matrix! 
        `CreateSceneRendererForSceneCapture()`
        Can I use a static function to simulate the UpdateSceneCaptureContents()? Are the data exposed?
        `UpdateSceneCaptureContent_RenderThread`, this function draws data to the TextureRenderTarget.
        The `FSceneRenderer` needs to be created everytime this function is called. Is this neccessary and why?
        It seems this function can be a static function, with no issue.
        **This requires `RHICmdList`.**
        
- function `CreateSceneRendererForSceneCapture` defined in `SceneCaptureRendering.cpp`.

- static function `UpdateSceneCaptureContent_RenderThread()` defined in `SceneCaptureRendering.cpp`, call the `UpdateSceneCaptureContentDeferred_RenderThread()`.

- static function `UpdateSceneCaptureContentDeferred_RenderThread()`, defined in `SceneCaptureRendering.cpp`
    
    this function calls `SceneRenderer->Render(RHICmdList);`
    Find the `SceneRenderer->Render()` and keep diving.
    
- class `FSceneRenderer`, declared in `SceneRendering.h`, `Render()` is a virtual function and implemented in `FDeferredShadingSceneRenderer`.

An overview is in `RenderingOverview.INT.udn`.

- class `FDeferredShadingSceneRenderer`, declared in `DeferredShadingRenderer.h` and defined in `DeferredShadingRenderer.cpp`


I need to bundle the required update together.

- `UScene`, declared in `Scene.h` and defined in `Scene.cpp`. This is an object.

`SceneCaptureRendering.cpp`

How many `RenderTarget` can a renderer support? `FSceneRenderTargets` is a bundle of `RenderTarget`?

- class `FSceneRenderTargets`, declared in `SceneRenderTargets.h`, defined in `SceneRenderTargets.cpp`
    - `CreateSnapshot()` which takes `viewinfo` as input, what is it for?
    - It is best if I can get this directly from the output.
    
- class `FRenderTarget`, declared in `UnrealClient.h`, see the inherience for it in here, https://docs.unrealengine.com/latest/INT/API/Runtime/Engine/FRenderTarget/index.html. Very strange naming convention.., for example `FTextureRenderTarget2DResource -> FTextureRenderTargetResource -> FRenderTarget`

- `UTextureRenderTarget`, `TextureRenderTarget.h` and `TextureRenderTarget.cpp`

Can I get `SceneContexts` directly from `RHICmdList` after one pass of rendering, that will be much more elegant, if this is possible!

Read `GBuffer` after a render pass, instead of doing multiple passes for each one. Maybe better to read the info in `the render thread` and send it back to `the game thread`.

Questions to answer, how to define and how to get the viewpoint.