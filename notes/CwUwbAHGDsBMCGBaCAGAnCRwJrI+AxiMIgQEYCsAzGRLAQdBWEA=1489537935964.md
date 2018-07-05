# VDL 3/14 report

- Tried out the [Tensorflow machine learning tutorial](https://www.tensorflow.org/get_started/mnist/beginners) on the MNIST task of recognizing the true digit from images of handwritten digit. Turned this tutorial into a distributed version between two machines, but there was a significant drop of accurancy. It is probably a bug that we will be able to fix soon.
- Currently trying to realize a one-learner two-actor communication model with raw TCP connection. Actors need to send two parameters (observation, reward) to the learner per interaction with environment, and learner needs to send back the "action instrutction" which is learned after processing the received data. There are still more details in the message communication process that need to be well handled.
 
- Finish assembling the robot arm.
![](https://i.imgur.com/khXY6k9.jpg)

- Start the creation of the virtual arm
    Get the static model from [3D warehouse repository]( https://3dwarehouse.sketchup.com/model/u21290a3e-f8ef-46da-985c-9aa56b0dee53/Maplin-OWI-ROBOTIC-ARM), import into Maya and make it controlable.

![](https://i.imgur.com/Fcke5jp.png)

