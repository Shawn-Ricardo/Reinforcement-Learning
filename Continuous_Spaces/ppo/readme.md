# <p align="center"><b>Proximal Proxy Optimization</b></p>

In 2017, Schulman, et al., introduced PPO as a policy gradient algorithm that is scalable, robust, and data efficient. Using Trust Region Policy Optimization (TRPO) as inspiration, the authors designed PPO to be simplier to implement and better at generalization, all the while outperforming TRPO, DQN, and other "vanilla" policy gradient methods.

<p align="center">
<img src="images/ppo_performance.PNG">
</p>

In the figures above, PPO outperforms previous methods on nearly all continous control environments. That is, environments with both continous observation and action spaces.

PPO is an on-line method. One of the salient details of on-line learning involves the collection of a finite number of *sequential* experiences that are then learned from and discarded. As such, PPO (and policy gradient methods, in general) are less sample efficient than off-policy methods, such as Deep Q-Network. For contrast, a DQN stores experiences in a Replay Buffer and samples these experiences at *random*.

If you are unfamiliar with a DQN and/or Replay Buffer, please view my detailed explanation elsewhere in this github.

The highlighted region of the PPO algorithm showcases this bootstrapping...

<p align="center">
<img src="images/ppo_bootstrap.PNG" width="580" height="220">
</p>

The paper begins by discussing a common gradient estimator and it's corresponding objective function. The objective function is given as,

<p align="center">
<img src="images/ppo_obj_fn.PNG" >
</p>

This formula corresponds to equation (2). It is defined as the expectation over the log of the stochastic action policy multiplied by an *estimate* of the advantage function, A_hat. The goal, then, is to perform stochastic gradient ascent using this loss function which causes the agent to learn. 


### <p align="center"><b><i>PPO Actor Critic</i></b></p>

PPO implements an actor-critic method to populate the terms in the objective function. 

The actor is a neural network that takes as input the state of the environment and produces a Gaussian distribution for each action. In order to obtain a continous value for an action, the corresponding distribution is sampled. The actor is represented by the policy *pi* in the objective function above. 

The critic is used to estimate the value function, V(s) and is a neural network tha has only one output. The value function is responsible for mapping a given state to a value that reflects how "good" it is for the agent to be in that state. More specifically, the critic *estimates* the reward that the agent is most likely to receive from it's current state forward - until the end of the epsiode. In actor-critic terminology, the critic acts as a *baseline*.

The advantage function (A_hat) in the equation above is the difference between a *weighted* sum of all the rewards an agent receives during each timestep of an episode (known as "discounted rewards") and the *estimate* of the reward that the agent is most likely to receive from its current state forward (that is, the critic's output).

<p align="center">
<img src="images/discount_reward.PNG" width="150" height="150">
</p>

<p align="center">
  <sup> sum of weighted rewards </sup>
</p>

Since PPO is an online-policy that collects trajectories for some arbitrary period, the weighted rewards can be computed immediately after bootstrapping. In fact, this can be seen in the algorithm for PPO shown above, stated as "Compute Advantage Estimates".








