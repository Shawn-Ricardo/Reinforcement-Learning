
__Blackjack__ - Teach an agent to play blackjack in OpenAI Gym by implementing a Monte Carlo approach with a greedy policy.

__SARSA__ - An exploration of a Temporal Difference approach that aims to update an agent's state-value function during run-time.    SARSA, Q-Learning, and Expected SARSA are applied to OpenAI Gym's CliffWalking environment. In addition, Expected_SARSA is applied to OpenAI Gym's Taxi-v2 environment.

__Discretize Continuous Spaces__ - SARSA algorithms are based on Markov Decision Processes, which operate on a assumption of a discrete state and action space. In many problems, the state and/or action space are continous and, as such, SARSA type algorithms cannot be applied. This collection discusses two approaches, 1. grid discretization and 2. tile coding, that aim to discretize a continous state space such that SARSA type algorithms (in this case, Q-Learning) can be applied to solve the problem with little to no modifications of the RL algorithm.

__Deep Q Network__ - Another alternative to dealing with continous state spaces is to use a deep neural network to approximate the Q-Table, which is the optimal action-value function of an agent acting in an environment. This notebook implements a Deep Q-Network to solve OpenAI Gym's Lundar Lander environment by using a neural network in-place of a Q-Table. 

This approach is inspired by the work of Mnih, Volodomryh, et al. (2015) in "Human-Level Control Through Deep Reinforcement Learning". In which the authors trained a agent to play Atari video games much better than professional game testers.

This directory also implements *Double DQN*, proposed by Hasselt, et al. (2015) in "Deep Reinforcement Learning with Double Q-Learning", as an improvment on the DQN architecture proposed by Mnih, et al. In this paper, the authors addressed the innate tendancy of Q-Learning to over-estimate action-values, which could harm network learning and performance. By decomposing the max-operation in the target into an action selection and an action evaluation processes, Hasselt, et al. obtained a better quality policy, more accurate values, and a more robust algorithm. 
