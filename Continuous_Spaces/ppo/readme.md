# <p align="center"><b>Proximal Proxy Optimization</b></p>

In 2017, Schulman, et al., introduced PPO as a policy gradient algorithm that is scalable, robust, and data efficient. Using Trust Region Policy Optimization (TRPO) as inspiration, the authors designed PPO to be simplier to implement and better at generalization, all the while outperforming TRPO, DQN, and other "vanilla" policy gradient methods.

<p align="center">
<img src="images/ppo_performance.PNG">
</p>

In the figures above, PPO outperforms previous methods on nearly all continous control environments. That is, environments with both continous observation and action spaces.

PPO is an on-line method. A salient aspect of on-line learning involves the collection of a finite number of *sequential* experiences that are then learned from and discarded. This is in contrast to off-line methods, such as a Deep Q-Network, which stores experiences in a Replay Buffer and samples these experiences at random. If you are unfamiliar with a DQN and/or Replay Buffer, please view my detailed explanation elsewhere in this github.

