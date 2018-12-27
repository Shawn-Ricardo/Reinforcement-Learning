In 2016, Schaul, et al. developed a framework for prioritizing experience, so as to replay important transitions more frequently. The algorithm was presented in the paper, ["Prioritized Experience Replay"](https://arxiv.org/pdf/1511.05952.pdf).

The algorithm is an improvement over the method implemented in the Deep Q-Network by Mnih et al., which is discussed and implemented elsewhere in this GitHub. In that method, experiences were sampled uniformly, such that every transition in the memory bank has equal probability of being chosen for learning.

Schaul, et al. prioritized transitions according to TD error, which is the difference between the target TD value and the current TD value predicted by the network. The reasoning behind such a method is that transitions with a greater error implied a more significant potential for learning than transitions with a lower TD error. This claim is substantiated by numerous neurological studies, where experiences with significant TD errors appear to be replayed more often in the hippocampus of rodents.

The following graph shows

![](images/per_results.PNG)


