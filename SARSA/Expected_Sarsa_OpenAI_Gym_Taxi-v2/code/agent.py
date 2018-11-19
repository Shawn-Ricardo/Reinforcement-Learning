import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, nA=6, alpha=0.5, eps=0.0008, gamma=0.4):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.alpha = alpha
        self.epsilon = eps
        self.gamma = gamma
        self.Q = defaultdict(lambda: np.zeros(self.nA))

    def epsilon_greedy_probs(self, Q_state):
        
        state_policy = np.ones(self.nA) * self.epsilon / self.nA
        greedy_action = np.argmax(Q_state)
        state_policy[greedy_action] = 1 - self.epsilon + ( self.epsilon / self.nA )
        return state_policy

    def updateQ(self, Q_sa, Q_nsa, reward):
        return Q_sa + (self.alpha * (reward + (self.gamma * Q_nsa) - Q_sa))
    
    def select_action(self, state):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        
        eps_action_policy = self.epsilon_greedy_probs(self.Q[state])
        
        return np.random.choice(np.arange(self.nA), p=eps_action_policy)

    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        eps_action_policy = self.epsilon_greedy_probs(self.Q[next_state])
        expected_value = np.dot(self.Q[next_state], eps_action_policy)
        self.Q[state][action] = self.updateQ(self.Q[state][action], expected_value, reward)
