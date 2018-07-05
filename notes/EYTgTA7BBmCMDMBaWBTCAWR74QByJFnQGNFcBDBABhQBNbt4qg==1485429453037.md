# DRAFT: UnrealCV architecture and design
###### tags: `unrealcv`

The concepts in this document is defined in [UE4 concepts](https://hackmd.io/MYUwTALAhgzAHAEwLQCMpwGxIgBjDJATmBgEYkoIAzCGHEYKlYHIA===).

## Ground truth generation

The SceneCaptureComponent is the most important thing in the unrealcv project.

[USceneCaptureComponent2D](https://docs.unrealengine.com/latest/INT/API/Runtime/Engine/Components/USceneCaptureComponent2D/index.html) is used in the ground truth extraction. During the rendering, information is rendered to the RenderTarget of a SceneCaptureComponent. The rendering passes through all steps and information is extracted in the post-process step and achieved with PostProcess materials. When sharing one views, the rendering only needs to be done once. Rendering the same place multiple times is a huge waste for my purpose. To see whether this is plausible, I need to read the code of USceneCaptureComponent2D rendering.

[SceneCaptureComponent2D](https://github.com/EpicGames/UnrealEngine/blob/release/Engine/Source/Runtime/Engine/Classes/Components/SceneCaptureComponent2D.h) definitions. [SceneCaptureComponent](https://github.com/EpicGames/UnrealEngine/blob/release/Engine/Source/Runtime/Engine/Private/Components/SceneCaptureComponent.cpp#L382) implementation.

Do SceneCapture in every frame is not a very efficient implementation.

## The communication

- TcpServer receives raw packet, decodes it
- UE4CVServer converts the raw packet to unrealcv command
- The unrealcv command is dispatched by the dispatcher 
- The command is executed by a `CommandHandler`, this varies depending on task
