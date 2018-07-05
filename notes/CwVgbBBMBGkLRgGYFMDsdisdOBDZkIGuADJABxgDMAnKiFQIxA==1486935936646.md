# Project proposal for the advanced distributed system

[The draft of project proposal](https://hackmd.io/MwQwHCCMBMDGCsBaAnMgRkgLMgJtF0ADAGyIgiHzRhqyFqVA)


How to distribute the simulation to multiple machines. Concurrent the game process. Maybe start the project with OpenAI gym and a very simple computer graphics environment, instead of UE4 directly.

## My goal in this project
I need to seperate the computer graphics part, the machine learning and training part, and only left the distributed challenges.


TODO: What has already been done in A3C and the distributed systems?
TODO: What to do and what is the challenge

Based upon the OpenAI gym system.

Data parallization and model parallization.

[How to draw figures for document](https://hackmd.io/CwUwJghgrADCBGBaSAmA7I4N5kQTjRQDNEYiUwAOCMWiNPIA)

The basic concepts DQN.

What is DistBelief.

In the DistBelief system, here is a system overview. DistBelief is the first generation of google brain.

![](https://github.com/alexminnaar/AkkaDistBelief/blob/master/images/downpour_sgd.png?raw=true)

Figure: from https://github.com/alexminnaar/AkkaDistBelief

But for a reinforcement learning task, is it easy to parallize the data?

Q: What is on-policy and off-policy?
Q: what is actor-critic?

Compare with previous ones and why? using far less resource than massively distributed approaches

In Gorila, each process contains an actor that acts in its own copy of the environment, a separate replay memory, and a learner that samples data from the replay memory and computes gradients of the DQN loss

proposed a parallel version of the Sarsa algorithm that uses multiple separate actor-learners to accelerate training. Each actor-learner learns separately and periodically sends updates to weights that have changed significantly to the other learners using peer-to-peer communication.

actor- critic being an on-policy policy search method and Q-learning being an off-policy value- based method.

TODO: What types of tasks can be parallized, can all of them?

on-policy reinforcement learning methods such as Sarsa and actor-critic

HOGWILD! on the same machine.

TODO: understand the architecture of these papers.
TODO: See what is the problem
TODO: Show a demo to persuade others.
TODO: Have a discussion with TK about how to parallize the training
TODO: See related efforts


Try running the code myself to have a sense of what I need to do.

Make sure to read the background material in the github code page. Read these papers for a few rounds, get the rough idea first, then refine it.

[Distributed version of OpenAI gym](https://github.com/viswanathgs/dist-dqn)

## Background

Reinforcement training with real images, the google robotics arms. The simulated environment for training.

## Problem and challenge

The speed of simulation. Can we distribute the simulation to multiple machines?

Is this a plausible idea? 

The speed of the simulation, the communication cost

I can not ensure each environment running at the same speed. How to do a distributed training if the environment is hard to control?

The whole project will be very complex, how to make it feasible and make sure team members can learn something from it?

## Plan
Start from something simple, (OpenAI gym) to move towards harder tasks.

Parallize data, model

one machine or multiple machines.

What is the current bottleneck. 

## Related work

Here is [a slide from MIT](web.mit.edu/larsb/Public/16.412/Advanced%20Lecture/Lecture3.ppt), not very useful.

- Distributed deep Q-learning [paper](https://arxiv.org/abs/1508.04186) [note](https://hackmd.io/GwUwrAnAZg7AhhAtAE2sxAWARlgjIuAJkJEVwGNCMwAOGAZkLwiA) [code]()

- A3C [code](https://github.com/coreylynch/async-rl) [paper](https://arxiv.org/pdf/1602.01783v1.pdf) [note](https://hackmd.io/GwUwrAnAZg7AhhAtAE2sxAWARlgjIuAJkJEVwGNCMwAOGAZkLwiA)

A3C is done in one machine, is it easy to scale it up to multiple machines? If not, what is the challenge?

TODO: Read the related work of this carefully and see the comparison with other works.

- Gorila (General Reinforcement Learning Architecture) [code]() [paper](https://arxiv.org/abs/1507.04296)  [a blog post](http://www.humphreysheil.com/blog/gorila-google-reinforcement-learning-architecture)

This piece of work is done by google DeepMind.

In this work, they created parallel actors that generate new behaviour; parallel learners. Is it applicable to any task and any network? What is missing here and what can we improve?

In order to generate more data, we deploy multi- ple agents running in parallel that interact with multiple instances of the same environment.

a distributed experience replay memory

In A3C the replay memory is not required, so they can use on-policy, is this correct?

What is difference between Gorila and DistBelief?

![](https://i.imgur.com/ISOVBQA.png)


Figure: The Gorila system overview, compare this with the DistBelief figure

![](http://www.humphreysheil.com/api/image/dsilver-3.png)

Figure: From the blog post.

- DistBelief

Model paral- lelism, where different machines are responsible for storing and training different parts of the model, is used to allow efficient training of models much larger than what is feasi- ble on a single machine or GPU. Data parallelism, where multiple copies or replicas of each model are trained on different parts of the data in parallel, allows for more effi- cient training on massive datasets than a single process.

## Useful links

