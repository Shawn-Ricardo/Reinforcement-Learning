In 2016, Lillicrap, et al., published ["Continous Control With Deep Reinforcement Learning"](https://arxiv.org/pdf/1509.02971.pdf), which took the DQN algorithm as inspiration and applied the Deterministic Policy Gradient algorithm to continous spaces.

The algorithm is as follows:

![Alt text](images/ddpg_algo.PNG)


<p align="center" font="20">
  <b>Actor Critic</b>
</p>


For other reinforcement learning algorithms in this github (SARSA, DQN, Discretization), the goal of the agent was to populate a Q-Table (please refer to these algorithms for an explanation). From this state-action -> value table, the optimal policy (state -> action) could be derived. That is, given a state S, the agent should take action A in order to maximize expected returns.

As it turns out, we can use a neural network to directly approximation the policy function, circumventing the population of a value function (Q-Table). However, a direct approximation such as this introduces a high degree of variance into the system, as is common with policy based methods. 

In order to reduce the variance of the system, an actor-critic approach is implemented. The critic will use a neural network to obtain TD estimates and construct a baseline. This baseline will be used to evaluate the decisions of the actor - that is, the network populating the policy function.

Such a TD estimation method has much lower variance than policy based methods, but a higher bias. This is to say, that bias is being introduced into the system. However, it has been shown that even though bias is introduced into the system, the presence of both an actor and critic (i.e., value function estimation and policy based estimation) produces an agent that learns a higher quality policy faster than either method alone. 
