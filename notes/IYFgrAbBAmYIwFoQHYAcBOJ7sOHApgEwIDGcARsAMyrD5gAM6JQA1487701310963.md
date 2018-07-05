# VDL 2/15, explain random search

###### tags: `VDL`

Show the random policy of [the Cartpole](https://gym.openai.com/envs/CartPole-v0). [Detailed explaination of this environment](https://github.com/openai/gym/wiki/CartPole-v0)

---

- Action $a \in {0, 1}$: means move to left or right.

- Observation $x \in \mathbb{R}^4$: the status of the stick. 
    Four numbers (cart position, cart velocity, pole angle, pole velocity at tip)
    
![](https://cdn-images-1.medium.com/max/800/1*oMSg2_mKguAGKy1C64UFlw.gif)

---

Train a model to decide to move the stick to left or right. 


$$
a = \begin{cases}
0 & \text{if } w\cdot x < 0\\
1 & \text{if } w\cdot x \geq 0
\end{cases}
$$

Find a good $w$ to do this task.

Weight $w \in \mathbb{R}^4$: Parameters of the model

[More details here](
http://kvfrans.com/simple-algoritms-for-solving-cartpole/)

---

Naive solution. use random search to find $w$. Do it in a distributed way.

Show a demo

---