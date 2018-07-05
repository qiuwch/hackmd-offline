Integrate UnrealCV with Openai Gym for Reinforcement Learning(RL)
===
In this tutorial, we show how to get started with installing environment, adding new envirnnment for specific RL tasks and train a DQN model for visual navigation in a realistic room.

![search1](https://i.imgur.com/esXQ0tI.gif)![search2](https://i.imgur.com/fPVfRVt.gif)



Installation
===
Considering performance, we use [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) to run the unreal environment. For the reason that ```nvidia-docker``` supports ```Linux```  and ```Nvidia GPU```only , you will have to install and run our openai-gym environment in ```Linux``` system with ```Nvidida GPU```
## Docker
As the unreal environment with UnrealCV runs inside Docker containers, you are supposed to install [docker](https://docs.docker.com/engine/installation/linux/ubuntu/#install-from-a-package) first. If you use Linux, you can run scripts as below:
```
curl -sSL http://acs-public-mirror.oss-cn-hangzhou.aliyuncs.com/docker-engine/internet | sh -
```
Once docker is installed sucessfully, you are able to run ```docker ps``` and get something like this:
```
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

To speed up the frame rate of the environment, you need install [nvidia-docker](https://github.com/NVIDIA/nvidia-docker/wiki) to utilize NVIDIA GPU in docker.
```
wget -P /tmp https://github.com/NVIDIA/nvidia-docker/releases/download/v1.0.1/nvidia-docker_1.0.1-1_amd64.deb
sudo dpkg -i /tmp/nvidia-docker*.deb && rm /tmp/nvidia-docker*.deb
```
Test nvidia-docker
```
nvidia-docker run --rm nvidia/cuda nvidia-smi
```
You should be able to get the same result as you run ```nvidia-smi``` in your host.

## Openai Gym
Install openai gym
```
git clone https://github.com/openai/gym
cd gym
pip install -e . 
```
If you prefer, you can do a minimal install of the packaged version directly from PyPI:
```
pip install gym
```

Install gym-unrealcv
```
git clone https://github.com/zfw1226/gym-unreal.git
cd gym-unrealcv
pip install -e . 
```



Run a simple envirnment
===
Before you run any examples, please run
```
xhost +
```

Once ```gym-unrealcv``` is installed sucessfully, you will see that your agent walking randomly in first-person view, after you run:
```
cd example/random
python random_agent.py
```
It will take a few minutes for the image and realistic environment to pull the first time. After that, if all goes well，a simple predefined gym environment ```Unrealcv-Simple-v0``` wiil be launched.And then you will see that your agent is moving around the realistic room randomly.

Add a new UnrealCV Environment
===
In this section, we will show you how to add a new unrealcv environment in openai gym for your RL tasks, step by step.
1. Copy your new Unreal Environment to ```/gym-unrealcv/gym_unrealcv/envs/UnrealEnv```
2. Create a new python file in ```/gym-unrealcv/gym_unrealcv/envs```, Write your environment in this file. A simple environment in [unrealcv_simple.py]() is avliable for you.The details of the code are shown as below:
```python =
import gym # openai gym interface
from unrealcv_cmd import  UnrealCv # a lib for using unrealcv client command
import run_docker # a lib for run env in a docker container
import numpy as np
import math
'''
State :  color image
Action:  (linear velocity ,angle velocity)
Done :   Collision detected or get a target place
'''
class UnrealCvSimple(gym.Env):
    # init the Unreal Gym Environment
   def __init__(self,
                ENV_DIR_BIN = '/RealisticRendering/RealisticRendering/Binaries/Linux/RealisticRendering',
   ):
     self.cam_id = 0
     # run virtual enrionment in docker container
     self.docker = run_docker.RunDocker()
     env_ip, env_dir = self.docker.start(ENV_DIR_BIN=ENV_DIR_BIN)
     # connect unrealcv client to server
     self.unrealcv = UnrealCv(self.cam_id, ip=env_ip, env=env_dir)
     self.startpose = self.unrealcv.get_pose()
     # ACTION: (linear velocity ,angle velocity)
     self.ACTION_LIST = [
             (20,  0),
             (20, 15),
             (20,-15),
             (20, 30),
             (20,-30),
     ]
     self.count_steps = 0
     self.max_steps = 100
     self.target_pos = ( -60,   0,   50)
     self.action_space = gym.spaces.Discrete(len(self.ACTION_LIST))
     state = self.unrealcv.read_image(self.cam_id, 'lit')
     self.observation_space = gym.spaces.Box(low=0, high=255, shape=state.shape)

   # update the environment step by step
   def _step(self, action = 0):
        (velocity, angle) = self.ACTION_LIST[action]
        self.count_steps += 1
        collision =  self.unrealcv.move(self.cam_id, angle, velocity)
        reward, done = self.reward(collision)
        state = self.unrealcv.read_image(self.cam_id, 'lit')

        # limit max step per episode
        if self.count_steps > self.max_steps:
            done = True
            print 'Reach Max Steps'

        return state, reward, done, {}
        
   # reset the environment
   def _reset(self, ):
       x,y,z,yaw = self.startpose
       self.unrealcv.set_position(self.cam_id, x, y, z)
       self.unrealcv.set_rotation(self.cam_id, 0, yaw, 0)
       state = self.unrealcv.read_image(self.cam_id, 'lit')
       self.count_steps = 0
       return  state

   # close docker while closing openai gym
   def _close(self):
       self.docker.close()

   # calcuate reward according to your task
   def reward(self,collision):
       done = False
       reward = - 0.01
       if collision:
            done = True
            reward = -1
            print 'Collision Detected!!'
       else:
            distance = self.cauculate_distance(self.target_pos, self.unrealcv.get_pos())
            if distance < 50:
                reward = 10
                done = True
                print ('Get Target Place!')
       return reward, done

   # calcuate the 2D distance between the target and camera
   def cauculate_distance(self,target,current):
       error = abs(np.array(target) - np.array(current))[:2]# only x and y
       distance = math.sqrt(sum(error * error))
       return distance

```
**You should modify ```ENV_DIR_BIN``` to the path of your Unreal Binary**. The same to other gym environments, ```step()```,```reset()``` is necessary.```close()```will help you to close the unreal environment while you closing the gym environment. Differently, you need design your reward function in ```reward()``` for your own task.

3. Import your environment into the ```__init__.py``` file of the collection. This file will be located at ```/gym-unrealcv/gym_unrealcv/envs/__init__.py.``` Add ```from gym_unrealcv.envs.your_env import YourEnv``` to this file.
4. Register your env in ```gym-unrealcv/gym_unrealcv/_init_.py```
5. You can test your environment by using a random agent
```
cd example/random
python random_agent.py -e YOUR_ENV_NAME
```
You will see your agent take some actions randomly and get reward as you defined in the new environment.

Run a reinforcement learning example
===
Besides, we provide an example to train an agent to visual navigation by searching for specific object and avoiding obstacle simultaneously in [Unrealcv-Search-v0]() environement using [Deep Q-Learning](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf).
### Dependences
To run this example, you should make sure that you have installed all the dependences. We recommend you to use [anaconda](https://www.continuum.io/downloads) to install and manage your python environment.
- Keras(Tested with v1.2)
- Theano or thensorflow
- Openai gym(>=v0.7)
- cv2
- matplotlib
- numpy

To use Keras(v1.2), you should run
```
pip install keras==1.2
```

 
You can start the training process with default parameters by runinng the following script:
```
cd example/dqn
python run.py
```
You will see a window like this:
![show](https://i.imgur.com/HyOVKD4.png)
While the ```Collision``` button turning red, a collision is detected.
While the ```Trigger``` button turning red, the agent is taking an aciton to ask the environment if it is seeing the target in a right place. 
You can change some parameteters in [```example/dqn/constant.py```]()
You can change the architure of DQN in [```example/dqn/dqn.py```]() 

Visualization
===
You can display a graph showing the history episode rewards by running the following script:
```
cd example/utility
python reward.py 
```
![reward](https://i.imgur.com/W039bbs.jpg)


You can display a graph showing the trajectory by running the following script:
```
cd example/utility
python trajectory.py
```
![trajectory](https://i.imgur.com/PKpKHNR.png)

- The ```green points``` represent where the agents realized that they had found a good view to observe the target object and got positive reward from  the environment.At the same time, the episode is finished. 
- The ```purple points``` represnet where collision detected collision, agents got negative reward. At the same time, the episode terminated. 
- The ```red lines```  represent the trajectories that the agents found taget object sucessfully in the end.
- The ```black lines``` represent the trajectories of agents that did not find the target object in the end.



