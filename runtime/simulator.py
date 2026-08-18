import numpy as np

from agents.agent import Agent


class Simulator:

    def __init__(self):
        self.agent = Agent()
        self.pop_list = []
        self.tick = 0

    def setup(self, num_agents):
        self.pop_list = np.array([Agent() for _ in range(num_agents)])

    def step(self):
        for agent in self.pop_list:
            agent.step()

        self.tempPopList = [agent for agent in self.pop_list if agent.alive]
        self.pop_list = self.tempPopList



        self.tick += 1