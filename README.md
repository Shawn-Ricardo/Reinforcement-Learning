
__Blackjack__ - Teach an agent to play blackjack in OpenAI Gym by implementing a Monte Carlo approach with a greedy policy.

__SARSA__ - An exploration of a Temporal Difference approach that aims to update an agent's state-value function during run-time.    SARSA, Q-Learning, and Expected SARSA are applied to OpenAI Gym's CliffWalking environment. In addition, Expected_SARSA is applied to OpenAI Gym's Taxi-v2 environment.

__Discretize Continuous Spaces__ - SARSA algorithms are based on Markov Decision Processes, which operate on a assumption of a discrete state and action space. In many problems, the state and/or action space are continous and, as such, SARSA type algorithms cannot be applied. This collection discusses two approaches, 1. grid discretization and 2. tile coding, that aim to discretize a continous state space such that SARSA type algorithms (in this case, Q-Learning) can be applied to solve the problem with little to no modifications of the RL algorithm.
