from agent import Agent
from monitor import interact
import gym
import numpy as np

env = gym.make('Taxi-v2')
agent = Agent()
best_avg_reward_container = []

for i in range(100):
    ave_rewards, best_avg_reward = interact(env,agent)
    best_avg_reward_container.append(best_avg_reward)

mean_of_best_avg_reward = np.mean(best_avg_reward_container)
print('average best over 100 iterations: ', mean_of_best_avg_reward)
