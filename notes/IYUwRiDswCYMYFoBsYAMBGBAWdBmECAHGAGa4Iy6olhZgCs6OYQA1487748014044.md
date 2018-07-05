# TODO: UnrealCV tutorial index

###### tags: `unrealcv`
TODO: merge this document with http://docs.unrealcv.org

## FAQ
- Check whether a port is in use in windows
`netstat -a -b`

## What do I need for a dev doc
- Linking doc to code.

TODO:Learn how to use doxygen to generate doc from code.

How to compile plugin.
How to install plugin to a new project
Benchmark.
How to modify code, the code structure?
How to release new versions.

## Setting up development environment

To develop UnrealCV (or any UE4 plugin), you need to have a C++ UE4 project. There are two types of UE4 project, one is C++ project another is blueprint project. (blueprint is a visually scripting language develope by Epic Games).

An example can be seen from the demo project unrealcv/playground. The playground project is a tiny but rich project contains many cases for testing and developing unrealcv. We recommend to start with this project, get familiar with it and run the test cases come with this project.

The essential steps are:
1. Create a c++ project.
2. Create a Plugins folder and put unrealcv into it.

### 




## Contributing

## Changelog


## How to add and modify UnrealCV code.

### Project setup
If you just want to compile and use UnrealCV code, and don't want to modify it. It is easy to follow these [steps]() to produce binaries that compatible with your machine. 

If you want to modify the functions or add features to UnrealCV, it is easier to integrate the plugin into an UE4 project.

We provide an example project `unrealcv/playground` to demonstrate how to do that. To finish the following tutorials, you need to have `git` and `Unreal Engine` installed in your machine.

Getting the example project. The example project can be retrieved with
`git clone git@github.com:unrealcv/playground.git --recursive`.

UnrealCV is a submodule of this git repository, so after running this command it should be already included in the `Plugins/unrealcv` folder.

#### Windows

To develop in windows, you need to have Visual Studio 2015 installed.

By right click the `playground.uproject`, you can generate a Visual Studio solution file. You can open the solution and modify the 

#### Linux

### Add a command handler

We will demonstrate how to add a new command `vset /unrealcv/hello [msg]` to display a hello message in the virtual world.

The Unreal Engine C++ documentation can be found here.

### Implement a function
