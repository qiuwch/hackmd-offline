# Profiling Unreal Engine, speed, performance

The bottleneck of UnrealCV is communication and async task processing. I have a rough understanding the performance bottleneck, the profiling tool can help me better understand what is wrong.

I need to have benchmark code to track the progress I got.

[This tutorial](https://wiki.unrealengine.com/Profiling,_How_To_Count_CPU_Cycles_Of_Specific_Blocks_Of_Your_Game_Code) shows how to use the profiling tool, but the UI is not easy to interprete for me yet. [CPU Profiling](https://docs.unrealengine.com/latest/INT/Engine/Performance/CPU/)

Notice: the stat tracking code should be removed?

## The bottleneck in unrealcv
Take the command `vget /camera/0/object_mask` as an example. The command parsing and dispatching is fast, this can be verified with a simple command such as `vget /unrealcv/status`.

In `ProcessPendingRequest`, process pending tasks with a `CommandDispatcher`.

`FCommandDispatcher -> ExecAsync` can be improved, current implementation is stupid, better to learn how UE4 is doing this.

How to use [AsyncTask](https://wiki.unrealengine.com/Using_AsyncTasks) in UE4 read its implementation.

[ReadPixels](https://github.com/EpicGames/UnrealEngine/blob/release/Engine/Source/Runtime/Engine/Private/UnrealClient.cpp#L41) is very slow, [here]() is a discussion. ReadPixelsPtr is not helpful because it also uses the ReadPixels. The implementation details show the ReadPixels need to wait for the rendering thread to complete so that it can access the data, is there a faster way, or a way to prioritize my operation? I need to use hound to help me figure out the implementation details underlying the code.

Check [RenderingThread.h](https://github.com/EpicGames/UnrealEngine/blob/release/Engine/Source/Runtime/RenderCore/Public/RenderingThread.h) to see how to implemnt ENQUEUE_UNIQUE_RENDER_COMMAND_ONEPARAMETER. It is actually doing a Task invokation, doing it directly and set priority might be faster.

There might be some undocumented features useful for my implementation, `GameThreadWaitForTask`.

Understand the [TaskGraph](https://wiki.unrealengine.com/Multi-Threading:_Task_Graph_System) system is helpful.

Some functions in [this list](https://docs.unrealengine.com/latest/INT/API/Runtime/Core/Async/index.html) can be helpful for my implementation. For example the FCompletionList.

The detail of `RHIReadSurfaceData`. In [D3D11RenderTarget.cpp](https://github.com/EpicGames/UnrealEngine/blob/release/Engine/Source/Runtime/Windows/D3D11RHI/Private/D3D11RenderTarget.cpp#L960). This is the windows implementation of RHI, in Line 960. `FRHICommandListImmediate` is defined in `RHICommandList.h`.

In [FRenderCommand](https://docs.unrealengine.com/latest/INT/API/Runtime/RenderCore/FRenderCommand/index.html), when specify which thread to run, how to ensure that? It seems difficult?

I need to understand the how to complete a `FGraphEventRef`, check [TaskGraphInterfaces.h](https://github.com/EpicGames/UnrealEngine/blob/release/Engine/Source/Runtime/Core/Public/Async/TaskGraphInterfaces.h), where is the EventRef comes from the TaskGraph system and how to use it? This is an interesting and important file.

`ConstructAndDispatchWhenReady` will return a FGraphEventRef, but where is it from, what is it pointing to, why it is sometimes NULL?


## The maximum framerate of UE4

Can I limit the frame capture rate per second?

Probably I need to write a [unit test] for some functions, such the regexp based dispatcher. This is an overview of [the test framework of UE4](https://docs.unrealengine.com/latest/INT/Programming/Automation/).

## The proformance of very basic commands
The execution of a basic command takes no time in the fourth step. I need to have an average number of how much time is spent in each step.

30 fps -> 30 ms
2 fps -> 500 ms

In this stage, optimizing the overhead does not help a lot. I need to optimize the `ReadPixels` first. If I did not read pixels, just enable the `CaptureCompoent`, the FPS drops but still OK. The noticiable FPS drop and CPU usage is from the unnecessary rendering of `CaptureComponent`. If I have a control of the ticking, what should be the correct order for reading data from the buffer? 

Check [the UnrealCV architecture](https://hackmd.io/EYTgTA7BBmCMDMBaWBTCAWR74QByJFnQGNFcBDBABhQBNbt4qg==?both) to see where to improve.

## The underlying rendering of SceneCaptureComponent

I need to understand how much time is spent in each step, can I know this?

## Check the cost in a game project
The more complex the game project, the slower the project will be.