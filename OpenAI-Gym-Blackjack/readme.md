
__General Approach: Monte Carlo__

A characteristic of a Monte Carlo approach is that a large number of iterations/sessions are conducted in order to gain a solid understanding of a given environment. In the case of blackjack, a monte carlo approach involves playing a significant number of hands - *e.g., a few hundred thousand*.

__Learning__

An agent learns to play successively better hands of Blackjack through the continual updating of its *Q-Table*, which is a table that provides an estimated reward given a particular State/Action pair. The state represents the agent's current sum, the dealer's card, and whether or not the agent has a usable ace. The action can be 0 = stick or 1 = hit.

For example, if an agent's state is ([16, 5, False]) and the action is 1 = hit, the Q-table, after having been updated over many hands, may return a reward of -1, indicating that the agent should not perform this action. On the other hand, an action of 0 = stick may result in a reward of 1 which indicates that this action usually results in winning the hand. So, the agent should perform this action. 

It is the goal of an agent to maximize its reward - to win as many hands of Blackjack as possible. As such, the Q-Table aids the agent in choosing the action that is expected to lead to the largest reward. 

__Method: Greedy Policy Update__

A *policy* is the force guiding an agent's actions. A an example of a deterministic policy for Blackjack is a policy where the agent always hits when its sum is less than or equal to 16, and sticks otherwise. An example of a stoichastic policy is one where the agents hits with a probability of 0.8 when the sum is less than or equal to 16 and sticks with a probability of 80% when the sum is greater than 16.

After every hand of Blackjack, which is called an *episode*, the agent updates the expected reward for a given State/Action pair in the Q-Table based on the results of the hand. In this program, the Q-Table is updated greedily, such that State/Action pairs that generate a larger expected reward are favored more by the agent. 

__Exploitation vs Exploration__

Having a purely greedy approach to updating the Q-Table could lead the agent to only explore an environment space that it naively believes produces the largest reward. For example, suppose that "route A" produces an immediate reward than "route B". However, "route B" ultimately leads to the best policy and a maximized reward. A truly greedy approach would never explore "route B". 

As such, the use of a variable *epsilon* is used to favor exploration over exploitation early on in the agents training. As the number of episodes increases, the agent's understanding of the environment increases as well. When at a sufficiently large episode count, the agent should rely on its understanding of the environment, i.e., its Q-Table, to chose its next action.

View the function *get_probs()* in the Python Notebook for a deeper explanation.

__Results__

The following chart shows the estimated best policy that the agent produces given 500,000 hands of blackjack.

![Image of Blackjack Policy]
(image/policy.png)
