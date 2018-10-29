__SARSA - State, Action, Reward, Next State, Next Action__

SARSA is an approach that allows updating of the Q-Table without the need to complete an episode. This type of learning is valuable for real-world examples where discrete lines between active-state and end-state are not present or are fuzzy.

The following equation describes the SARSA approach:

IMAGE

Given a starting state (s0), choose an epsilon-greedy action (a0) and observe the reward (r0) and next state (s1). In this next state, use the Q-Table to obtain the best action moving forward (a1) using, again, the epsilon-greedy approach. Obtain the corresponding reward (r1) that would be *expected* given this State-Action pair. 

Use these values to update the Q-Table for (s0, a0) by evaluating the equation above. 

The main crux of this approach is that we do not rely on the completion of an episode in order to update the Q-Table. We rely on the current values of the Q-Table, which have been updated as the agent moves throughout the environment, making decisions and observing the rewards of those decisions. 
