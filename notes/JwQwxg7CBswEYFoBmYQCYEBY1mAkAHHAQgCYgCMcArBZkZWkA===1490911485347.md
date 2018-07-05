# VDL plan 3/30

## TODO
Video communication speed, figure to draw
Contact kaphil
The list of experiments to do. 
    **The overhead for communication compared with experiment size**
    Supervised learning for robo pose 
    Crash challenges
Code
    
    
1. combine two communication parts
2. do larger scale experiment
3. virtual robo training.


---

1. multi-cast learners

Plot a figure to show the relationship between communication and computation. Simulate computation speed using sleep and try a few different model size.

In some applications, for example
          compute,   network
MNIST,    3ms,       20ms,           x
Face,     30ms,      35ms,          roughly ok
A3C,     300ms,     100ms,           ok

Had a discusssion about the difference between unicast and multi-cast. Multi-cast will be more robust but may introduce more overhead than parameter server. For example, in a 10 nodes system, the communication might be 10 * 2. In a unicast broadcast syste, the communication might be 10 * 10. In a multicast system, the cost will be much less than 10 * 10, but not sure what the number is.

2. Learner-actor system

Get a comparison for the overhead of the communication
         Multi-machine      Single machine 
CartPole 200FPS          << 1W FPS
Physics  100FPS          <  200FPS
Realistic  100FPS          <  30FPS
Real 


The realistic environment and the physics environment have simliar speed because the image size can be roughly the same. This means our design can support much more complex simulation.

To get this evaluation, we need to do 1. the learner-actor communication needs to support more than two actors. 2. The observation needs to be able to support much more complex data, such as images.

3. Virtual robo arm training

The first task is returning to original position, the second is reaching a certain postion.

To achieve this, we need to use supervised learning to recover the arm configuration from images. We will extract images and joint configuration as (x, y) pairs and use this to train a vision module to extract arm configuration. This configuration will be used to guide the motion planning.

The two state spaces can be $R^5$ and $R^{640x480}$.
