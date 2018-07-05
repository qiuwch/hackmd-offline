# Tensorpack reading notes

Training code in `train-atari.py`. The model is defined as a ModelDesc.

The model will train a value network and a policy network `actor-critic`.

The optimizer is defined in `_get_optimizer`. How the optimizer is involked?

The simulator part, it contains a SimulatorMaster to collect simulation data from all.

trainer can be a `AsyncMultiGPUTrainer` and load config as its parameter. `AsyncMultiGPUTrainer` is defined in [here](https://github.com/ppwwyyxx/tensorpack/blob/master/tensorpack/train/multigpu.py). In `_start_async_thread`, each thread can be considered as one training machine? When to sync the gradient?

What is the meaning of tower in the code? The f in the code is where the learning is happening.

The grad_list is an operation, not a value. `    def _multi_tower_grads(towers, get_tower_grad_func)`

`_get_cost_and_grad` should be defined in a base class, in `SingleCostFeedfreeTrainer`.

LoopThread? Infinity loop?

## To read
`train-atari.py` 
    Model is defined in the Model class
    AsyncMultiGPUTrainer
    
`multigpu.py`
    Define AsyncMultiGPUTrainer.
    the task of each thread is done in the `f()` function
    
`feedfree.py`
    Define the function `_get_cost_and_grad`