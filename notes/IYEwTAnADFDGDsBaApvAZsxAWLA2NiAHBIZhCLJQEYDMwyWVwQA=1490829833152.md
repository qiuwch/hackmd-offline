# *Reinforcement learning background*

###### tags: `VDL`


[The basic knowledge of OpenAI gym](https://hackmd.io/GYNgjGDMAcAMCGBaYYDGBWRAWExME4B2AI30VmJWmGKy32gBMg==)

## Resources

[David Silver RL course page](http://www0.cs.ucl.ac.uk/staff/D.Silver/web/Teaching.html) Follow all the notation and concepts from here. Do not get distracted by other information.

[A note recommended by Ethan](https://people.eecs.berkeley.edu/~pabbeel/nips-tutorial-policy-optimization-Schulman-Abbeel.pdf)

## Some questions

Answer these questions in my own words finally

[What is the relationship between policy gradient and q-learning](https://www.quora.com/What-is-difference-between-DQN-and-Policy-Gradient-methods).

[What is policy gradient](http://www.scholarpedia.org/article/Policy_gradient_methods)

How to integrate n-step, the difference with one-step.

When the gradient is accumulated, is the gradient applied to a very early model or applied to a recent model?

How to derivite gradient in the learning? Define the loss function then take derivative

What is [q-learning](https://en.wikipedia.org/wiki/Q-learning), a type of reinforcement learning, learn a $Q$ function. $Q : S \times A$, the Q function is learned during training. If I have a Q function, I can know which action to take in a certain state $s_t$. A simple version of the Q function is based on table, but this is hard to scale up.

What is policy network and action network? What is the hierarchy?

What are those variants covered in A3C? one-step q-learning, [Sarsa](https://en.wikipedia.org/wiki/State-Action-Reward-State-Action), n-step q-learning, actor-critic. What is the difference between these methods?

How to define reward in a learning system. It is task dependent. How can I know whether my task is defined well?

Why not ask several machines to search independently? This is what A3C did, right? 

## Example code/paper

[A basic example to solve cartpole](http://kvfrans.com/simple-algoritms-for-solving-cartpole/). This is simple enough, but not useful for our problem.

https://github.com/miyosuda/async_deep_reinforce
这个是A3C的 @ethan

DQN的我看过一个用keras写的，超级短，很容易改 @ethan
http://edersantana.github.io/articles/keras_rl/

## Study notes

Basic concepts: State $S$, Possible actions $A$, Environment $E$, time step $t$, Time t: $a_t$, $s_t$, policy $\pi$, a mapping from $s_t$ to $a_t$, receive state $s_{t+1}$ and $r_t$, Total accumulated return $R_t = \sum_{k=0}^{\inf} \gamma^k r_{t+k}$, discount factor $\gamma$.

The action value $Q^{\pi}(s,a)$, this is a Q function. The value of state s under policy $\pi$ $V^{\pi}(s)$. Define the loss function is very important for neural network, so that we can know how to do training.  

The challenges in reinforcement learning. Partial observation, probability control, high dimension space.



