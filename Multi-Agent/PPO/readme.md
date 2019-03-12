## <p align="center"><b>PPO For Tennis</b></p>

This notebook applies the PPO algorithm to the Unity [Tennis environment](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Examples.md). 

The PPO algorithm is discussed in depth elsewhere in this GitHub. Please refer to that [notebook](https://github.com/Shawn-Ricardo/Reinforcement-Learning/tree/master/Continuous_Spaces/ppo) to familiarize yourself with the concepts of PPO.

This environment is a collaboration between two agents. That is, both agents must work together to achieve a goal, which is to keep the ball in play as long as possible.

The reward structure for each agent is identical and the PPO algorithm is successfully applied to this environment in the same way as the Unity Crawler environment.

### <p align="center"><b><i>Application & Results</i></b></p>

<p align="center">
  <sup> Application </sup>
</p>

The PPO algorithm was used to train a pair of agents to control each respective tennis racket.

The observation space is continuous and is a vector of size 8, corresponding to position and velocity of the ball and the racket. The action space is continuous and is a vector of size 2, corresponding to moving forward/backward and jumping.

The agents are to keep the ball in play for as long as possible. The agents receives a +0.1 each time the ball is hit over the net.

The environment is considered solved when the average score over 100 consecutive episodes is greater than or equal to +0.5.

The environment can be downloaded [here](https://github.com/udacity/deep-reinforcement-learning/tree/master/p3_collab-compet).

<p align="center">
  <sup> Results </sup>
</p>
