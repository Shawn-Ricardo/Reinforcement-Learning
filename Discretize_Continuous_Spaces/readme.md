In the follwing notebook, I use OpenAI Gym's Mountain Car environment to show how to deal with a continous space. 

This work follows my work on SARSA algorithms, which deal only in discrete spaces.

The Mountain Car environment has a continous state space and a discrete action space. By discretizing the state space, I can apply a SARSA style (in this case, Q-Learning) reinformcement learning algorithm to teach an agent to climb a mountain!

In *Tile_Encoding*, I use Acrobot-v1, which has a continuous state space and discrete action space. This state space is discretized using multiple tilings, each overlapping in differening regions in the state space. By using these tilings, better generaliztion is achieved than a uniform grid that was used to solve the Mountain Car environment. 
