# <p align="center"><b>Proximal Proxy Optimization</b></p>

In 2017, Schulman, et al., introduced PPO as a policy gradient algorithm that is scalable, robust, and data efficient. Using Trust Region Policy Optimization (TRPO) as inspiration, the authors designed PPO to be simplier to implement and better at generalization, all the while outperforming TRPO, DQN, and other "vanilla" policy gradient methods.

<p align="center">
<img src="images/ppo_performance.PNG">
</p>

In the figures above, PPO outperforms previous methods on nearly all continous control environments. That is, environments with both continous observation and action spaces.

PPO is an on-line method. One of the salient details of on-line learning involves the collection of a finite number of *sequential* experiences that are then learned from and discarded. As such, PPO (and policy gradient methods, in general) are less sample efficient than off-policy methods, such as Deep Q-Network. For contrast, a DQN stores experiences in a Replay Buffer and samples these experiences at *random*.

The highlighted region of the PPO algorithm showcases this bootstrapping,

<p align="center">
<img src="images/ppo_bootstrap.PNG">
</p>


If you are unfamiliar with a DQN and/or Replay Buffer, please view my detailed explanation elsewhere in this github.



