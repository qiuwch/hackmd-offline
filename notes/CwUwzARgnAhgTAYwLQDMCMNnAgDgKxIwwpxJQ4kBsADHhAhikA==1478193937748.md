Learning best practice of OSS 
===
These are something that not taught by my teachers and advisor

### How to write python unittest?

For unit test, how to run a portion of the test. How to write assert, how to use parameters for test?

How to write a mock-up for testing.

Skip some tests, when opencv is not available.

### How to do logging.

How to use sphinx to write documentation

## Basic workflow
Very basic and important concepts
[Semantic version](http://semver.org)

[Write changelog](http://keepachangelog.com/en/0.3.0/)

[The github workflow](https://guides.github.com/introduction/flow/)

### How to release

The changelog should be kept in a plain text file, do not rely on any website even github. Plain text is much easier to edit and immigrate.

Why to put artifact? Github is better than bintray. It has a better integration between artifact and the source code.

How to put release to github? Use python script to automatic this process. For the plugin, use python to upload, unrealcv-mac.zip, unrealcv-linux.zip, unrealcv-win.zip. Before upload I need to do testing to make sure the code is of good quality, unrealcv plugin can not be tested by itself, so its process will depend on the playground project.

Currently Jenkins is the only build system I can rely on, though it is not good, I don't have better choices.

It seems there is not a good way to do automatic semantic version labeling, maybe do it myself by hand. The CHANGELOG should be cleaner than `git log`. So the strategy for this should be using `git log` to get a rough idea can then do editing to make it my changelog.

## Something I want to do
### Notify users I have a new release of my project.
- Use a github issue, which no one can make comment and ask users to subscribe to this issue is a way to try. 

### Monitor the statistics of my project.
- Use google analytics, use github API to get the download statistics of a specific version.

### Make more connection with other users
==Create a gitter channel==

### Provide docs
To encourage development, I should have some documents for my code so that people can know where to modify.

For development, the basic requirement is how to build the code and run the code.

    

## Useful tools
- Google analytics
- [Github star history](http://www.timqian.com/star-history/)


### Project statistics
- Compare `unrealcv/unrealcv`, `hackmdio/hackmd`, 

## My experience
I think the script should be kept outside the project. At least the development branch should be kept outside and only the stable one be kept in the repo.

There is no need to make a new commit by fixing some bugs in my packaging scripts.

Use python to write scripts and make sure these scripts can also be imported, so that I can use the combination to create more powerful functions.

## Some good projects I should follow
### Famous research projects
- [Tensorflow](https://github.com/tensorflow/tensorflow/releases)
- Caffe 

### Famous projects
- atom
- homebrew
- linux-kernel 
- [hackmd](https://github.com/hackmdio/hackmd/releases) (The editor I am using), this is a really excellent project, clean and elegant

### Unreal Engine projects
- UETorch
- Unreal.js
- Leap Motion Plugin

### Related projects
- UETorch
- VizDoom