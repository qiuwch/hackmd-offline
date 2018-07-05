VDL Client-Server Architecture Design
===
<!--
## The learner and actor/environment

![](https://i.imgur.com/Uz3FMgy.png)
<center>
Fig 2. (Deprecated but we want to keep it) Detailed view of the server-client architecture for server A and its clients. A: Actor, L: Learner, E: Environment. Source file is <a href='https://drive.google.com/file/d/0B9V-uDXSgSr2M3JSS053cW1EY3c/view?usp=sharing'>here</a>
</center>
-->

### Background
Environment: where the learning actions take place
Actor: apply selected actions in the environmrnt and collect reward data
Learner: process the data generated through the interactions between actors and environment and learn

### The learner and actor

<div id="joint_learner"/>

![](https://i.imgur.com/0zBUXNU.png)

<center>
Fig.joint_learner:  Learner and actor in the same machine.
</center>

<!-- figures are stored in https://www.lucidchart.com/invitations/accept/0d87d565-fe6a-4834-b8d5-cd9224d24a17 -->


```
S.V.: Simple virtual environment
R.V.: Realistic virtual environment
R: Real environment
```
In S.V. \cite{A3C, DQN}, the speed of rendering is very fast, so the learner and actor are in the same machine, shown in [Fig.joint_learner](#joint_learner). It can easily reach more than 1000fps. The bottleneck is the learner, which learns at hundreds fps (NEED TO CHECK THE EXACT NUMBER). The S.V. won't bring in much overhead for the learning system, so it can be easily done within one machine. Putting learner and actor within the same machine also saves the effort of sending observation from environment through network. The observation can be a few numbers (Cartpole) or image (Breakout) or other sensor input.

In a relastic virtual environment (R.V.), the simulation part can be slower than the learner, say 20fps. This number can be even lower if we want to do very accurate physics simulation. In this case, the simulation is a bottleneck for the learner and the learner needs to wait for the simluation engine, which slows down the learning process.

So we propose to seperate the learner with the simulation engine, as shown in [Fig.sep_learner](#sep_learner). This design has some benefits: 1. it makes our system extensibly to real environment. We can replace the actor/environment loop with a real robot without modification. 2. one powerful learner can be connected to multiple actors, shown in [Fig.multi_envs](#multi_envs) 3. learner and actor can have completely different system configurations making the system much easier to deploy and can be easily adapted with current state-of-the-art methods. Currently learner requires powerful CUDA GPU which is 30x faster than CPU.

But seperating the learner with actors gives us a few challenges. The speed of communication is a big challenge. 

<div id='sep_learner'/>

![](https://i.imgur.com/2mkCGjQ.png)
<center>Fig.sep_learner: Learner and actor in seperate machines.</center>

<div id='multi_envs'/>

![](https://i.imgur.com/2gGJHZv.png)
<center>Fig.multi_envs: Connect a learner with multiple actors.</center>




## System Architecture

The distributed system model for our Distributed Reinforcement Learning in Virtual Environment (VDL) project is a client-server architecture, where several central servers collectively manage the communication and task distribution between clients who run the actual learning algorithm in a relistic virtual environment. 

We use a fault-tolerant architecture with 3 servers, 6 learners and 12 actors as our example from now on. For simplicity, a learner with two actors will constitute a client. Denote $S_A,S_B,S_C$ the 3 servers, $L_{A0},L_{A1},L_{B0},L_{B1},L_{C0},L_{C1}$ the 6 learners, and $A_{A0},A_{A1},A_{A2},A_{A3},A_{B0},A_{B1},A_{B2},A_{B3},A_{C0},A_{C1},A_{C2},A_{C3}$ the 12 actors. 
Each client (leaner + actors combination) only directly communicates with the server that has the same letter (e.g. Client $\{L_{A1},A_{A0},A_{A1}\}$ talks with Server $S_A$ only). Within a client, an actor can only talk to the learner, and only the learner can talk to a server. For a robotics lab, a simpler architecture can be used where the client is just a single machine instead of a combination of machines. Figure 1 illustrates the complex architecture:

![Client-server architecture with 3 servers, 6 learners and 12 actors](https://i.imgur.com/a7Qx7JW.png)
<center>
Fig 1. Falut-tolerant client-server architecture with 3 servers, 6 learners and 12 actors.

A complex architecture that can be extended to the national scale.
</center>

Assocaiated with a learning model is a problem space $P$. To harness the power of distributed systems, $P$ is partitioned into subspaces $P_A$, $P_B$ and $P_C$ where Server $S_i$ is responsible for training on $P_i$. Furthermore, each $S_i$ partitions $P_i$ into $P_{i0}$ and $P_{i1}$, and client with learner $L_{ij}$ will train on $P_{ij}$. When the clients are training, they will exchange information with each other via the central servers, and through Anti-Entropy Method the servers will gain the same knowledge. Eventually, when all trainings are done, all clients will have the same final model parameter outputs.

When an agent is running the learning algorithm, there is a  _score_ associating with how good the current parameters are. There is a _low threshold_ of score such that if an agent's score drops below the threshold, then it stops its current searching and move on to help another agent. The server maintains score information of client agents and manages the agent movements if necessary. Similarly, if a crash occurs, other machines will help distribute the leftover task evenly. Thus, our architecture is able to provide fault-tolerant capabilities. More details to follow.




## Coding Steps
1. Start with a single-machine Leaner/Actor code where learner is in Tensorflow and actor is in OpenAI. We will try to separate it into two machines. Then, we will extend it such that there will be one learner and two actors communicating through the network. This will consist one client.
2. At the same time as Step 1, we will also try to replicate a single-machine client into multiple clients and build the server cluster managing the communications between them. This will consist the server cluster.
3. Then, we will replace the single-machine clients in Step 2 with the multi-machine clients in Step 1. 
4. (Can do Step 5 first) Add fault-tolerant capabilities to our architecture.
5. 	Construct a baseline experiment to compare task learning on a single machine vs our architecture.
6. NVIDIA vs Intel NUC: compare their performances as learner (machine learning) and actor (rendering).





## What to buy
* 2 NUCs: http://www.intel.com/content/www/us/en/nuc/nuc-kit-nuc7i7bnh.html  
 Something like this, but the one Yair mentioned is what we mean
 ![](https://i.imgur.com/nHfU4Yr.png =300x)
 
* 2 OWI arms: https://www.amazon.com/OWI-OWI-535-Robotic-Arm-Edge/dp/B0017OFRCY  
 One for testing our learning algorithms; another one for backup/compare & contrast/baseline. They are only $40 each, so buying two is not a big deal.
 ![](https://i.imgur.com/4h032hj.jpg =250x)

* 2 OWI USB Interface for Robotic Arm: https://www.amazon.com/OWI-USB-Interface-Robotic-Arm/dp/B0028MBWS2




Ideally, we can put the 10 NUCs on the same network as the Bloomberg machines, i.e. put them in Bloomberg Physics building too. This way, our network speed topology can be well approximated. Alternatively, high speed optic fiber cables between the NUCs and the Bloomberg machines would be great. If neither of these options are feasible, we might need to limit the data size of observations sent by the actor to the learner in order to make the program not run too slowly.



###### tags: `VDL` `System Design`