SARSA - State, Action, Reward, Next State, Next Action

SARSA is an approach that allows updating of the Q-Table without the need to complete an episode. This type of learning is valuable for real-world examples where discrete lines between active-state and end-state are not present or are fuzzy.

The following equation describes the SARSA approach:

IMAGE

Given a starting state (s0), choose an epsilon-greedy action (a0) and observe the reward (r0) and next state (s1). In this next state, use the Q-Table to obtain the best action moving forward (a1) using, again, the epsilon-greedy approach. Obtain the corresponding reward (r1) that would be expected given this State-Action pair. 

The 

