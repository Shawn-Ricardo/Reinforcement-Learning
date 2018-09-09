
__General Approach: Monte Carlo__

A characteristic of a Monte Carlo approach is that a large number of iterations/sessions are conducted in order to gain a solid understanding of a given environment. In the case of blackjack, a monte carlo approach involves playing a significant number of hands - *e.g., a few hundred thousand*.

__Learning__

An agent learns to play successively better hands of Blackjack through the continual updating of its *Q-Table*, which is a table that provides an estimated reward given a particular State/Action pair. The state represents the agent's current sum, the dealer's card, and whether or not the agent has a usable ace. The action can be 0 = stick or 1 = hit.

For example, if an agent's state is ([16, 5, False]) and the action is 1 = hit, the Q-table, after having been updated over many hands, may return a reward of -1, indicating that the agent should not perform this action. On the other hand, an action of 0 = stick may result in a reward of 1 which indicates that this action usually results in winning the hand. So, the agent should perform this action. 

It is the goal of an agent to maximize its reward - to win as many hands of Blackjack as possible. As such, the Q-Table aids the agent in choosing the action that is expected to lead to the largest reward. 

__Method__


