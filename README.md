
<p align="center">
  <b> Blackjack </b>
</p>


Teach an agent to play blackjack in OpenAI Gym by implementing a Monte Carlo approach with a greedy policy.

<p align="center">
  <b> SARSA </b>
</p> 

An exploration of a Temporal Difference approach that aims to update an agent's state-value function during run-time.    SARSA, Q-Learning, and Expected SARSA are applied to OpenAI Gym's CliffWalking environment. In addition, Expected_SARSA is applied to OpenAI Gym's Taxi-v2 environment.

<p align="center">
  <b> Discretize Continuous Spaces </b>
</p>

SARSA algorithms are based on Markov Decision Processes, which operate on a assumption of a discrete state and action space. In many problems, the state and/or action space are continous and, as such, SARSA type algorithms cannot be applied. This collection discusses two approaches, 1. grid discretization and 2. tile coding, that aim to discretize a continous state space such that SARSA type algorithms (in this case, Q-Learning) can be applied to solve the problem with little to no modifications of the RL algorithm.

<p align="center">
  <b> Deep Q Network </b>
</p>

Another alternative to dealing with continous state spaces is to use a deep neural network to approximate the Q-Table, which is the optimal action-value function of an agent acting in an environment. This notebook implements a Deep Q-Network to solve OpenAI Gym's Lundar Lander environment by using a neural network in-place of a Q-Table. 

This approach is inspired by the work of Mnih, Volodomryh, et al. (2015) in "Human-Level Control Through Deep Reinforcement Learning". In which the authors trained a agent to play Atari video games much better than professional game testers.

<p align="center">
  <i> Double DQN (DDQN) </i>
</p>

This directory implements a *DDQN*, proposed by Hasselt, et al. (2015) in "Deep Reinforcement Learning with Double Q-Learning", as an improvment on the DQN architecture proposed by Mnih, et al. In this paper, the authors addressed the innate tendancy of Q-Learning to over-estimate action-values, which could harm network learning and performance. By decomposing the max-operation in the target into an action selection and an action evaluation processes, Hasselt, et al. obtained a better quality policy, more accurate values, and a more robust algorithm. 

<p align="center">
  <i> Prioritized Experience Replay (PER) </i>
</p>

Lastly, *PER* (Schaul, et al., 2016) is implemented within a 3D Unity Environment, where the goal of the agent is to collect yellow bananas while avoiding blue bananas. PER prioritized experiences by the greatest potential for learning. That is, the experiences that yield the largest Temporal-Difference errors. Intuitively, the experiences the have the greatest TD error must indicate the most significant potential for learning. In experimentation, Schaul, et al., prove that DDQN with PER produces higher quality policies and faster learning times. 


<p align="center">
  <b> Continous Spaces </b>
</p>


The above reinforcement learning algorithms either deal with discrete state/action spaces or continous state spaces with discrete action spaces. The following algorithms address environments containing both continuous state and action spaces. These types of spaces are critical to future applications, such as robotics, as most problems in the real world exist in this realm.


<p align="center">
  <i> Deep Deterministic Policy Gradient (DDPG) </i>
</p>


In, "Continuous Control With Deep Reinforcement Learning (2016)", Lillicrap, et al., adapt the Deep Q-Network to the continous action domain using an actor-critic, model-free algorithm based on the deterministic policy gradient that can operate over continous action spaces. DDPG is used to train an agent to manipulate a double jointed arm in order to place the joint's end point at a moving target location in space.

<p align="center">
  <i> Proximal Policy Optimization (PPO) </i>
</p>

In 2017, engineers at OpenAI developed a policy-based algorithm that operates within continuous observation and action spaces. The main crux of PPO is its simplicity, low hyper-parameter utilization, and generalization capability. In fact, OpenAI has deemed PPO as the [default reinforcement learning algorithm](https://blog.openai.com/openai-baselines-ppo/) for these very reasons and has deployed a version of the PPO algorithm that is [capable of defeating amateur Dota 2 teams](https://blog.openai.com/openai-five/). In this notebook, PPO is used to train an agent to crawl on the [Unity Crawler Environment](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Examples.md).


<p align="center">
  <b> Multi-Agent </b>
</p>

work in progress...
