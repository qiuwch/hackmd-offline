# Virtual environment memory usage

    pmap -x `pgrep python`

Nothing: 393348K,  FPS 2206644
CartPole: 393908K (+560KB), FPS 170563
BreakOut: 407260K (+13912KB), FPS 14142
Hopper-v1: 473652K (+80304KB), FPS 4530
Humanoid-v1: 474628K (+81280KB), FPS 1206
RealisticRendering: 2152132K (~2GB), FPS 200 (without physics simulation)

`python train-atari.py  --env Breakout-v0`

Training speed: 6-7 iter/second, in every iteration, process number of images? `BATCH_SIZE = 128`. Image size `84 * 84`.

![](https://i.imgur.com/Q6tQgee.png)
