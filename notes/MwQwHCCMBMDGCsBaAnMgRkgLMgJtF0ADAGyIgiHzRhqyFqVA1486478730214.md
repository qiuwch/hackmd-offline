# Draft of the project proposal for advanced distributed system

[The note for this draft](https://hackmd.io/CwVgbBBMBGkLRgGYFMDsdisdOBDZkIGuADJABxgDMAnKiFQIxA==?both). For a more serious writing, move this draft to overleaf and use latex.

## The background

Speed up the robotics training, no matter it is a real robot or a synthetic environment. The news of [training robotics system with multiple robotics arms in google](http://www.theverge.com/2016/3/9/11186940/google-robotic-arms-neural-network-hand-eye-coordination).

Show [a demo of OpenAI gym]()

A lot of requests for making the virtual environment faster, distributing the computation is a natural idea.

TODO: prepare a few of videos and execution demo for unrealcv.

## Related work

The [A3C](#A3C) is a high impact work in 2016, it makes reinforcement learning asynchronous, but only running in one machine ([code]()). Previous attempt, such as: [the Gorrila]() and the [DistBelift]() can distribute the learner and actor to different machines using a technique called parameter server. The model and delta $\delta W$ needs to be transferred between machines. 

## The problems and challenges

The special challenges of distributing a physical simulation system. What is the remaining challenges in the previous work is still unclear yet, I need to dive more into it. Probably the speed the schedule, not nothing very challenging?

It is possible to see the challenges in the future work of these papers.


## Plan

The final goal is making unrealcv a distributed system (show a demo of [unrealcv](https://unrealcv.org), but starting from UE4 is too complicated and might be beyond the scope of this course. It is easier to start from a simpler graphics environment, such as those provided by the [OpenAI gym](https://gym.openai.com/).

## Related work

<div id="distQ"></div>

- Distributed deep Q-learning [paper](https://arxiv.org/abs/1508.04186) [note](https://hackmd.io/GwUwrAnAZg7AhhAtAE2sxAWARlgjIuAJkJEVwGNCMwAOGAZkLwiA) [code]()

<div id="A3C"></div>

- A3C [code](https://github.com/coreylynch/async-rl) [paper](https://arxiv.org/pdf/1602.01783v1.pdf) [note](https://hackmd.io/GwUwrAnAZg7AhhAtAE2sxAWARlgjIuAJkJEVwGNCMwAOGAZkLwiA)

A3C is done in one machine, is it easy to scale it up to multiple machines? If not, what is the challenge?

- Gorila [code]() [paper](https://arxiv.org/abs/1507.04296)

- The [DistBelief system]() and the [tensorflow system]()

