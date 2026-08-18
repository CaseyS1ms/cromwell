import numpy as np

from agents.agent import Agent


class Simulator:

    def __init__(self):
        self.tick = 0
        self.pop_list = []


    def setup(self, num_agents):
        self.pop_list = np.array([Agent(self) for _ in range(num_agents)])

    def step(self):
        for agent in self.pop_list:
            agent.step()

        if self.tick == 120:
            self.pop_list.append(Agent(self))

        self.pop_list = [agent for agent in self.pop_list if agent.alive]


        if self.tick % 8760 == 0:
            print("Year", self.tick // 8760)

        if self.tick % 730 == 0:
            print("Month", self.tick // 730)



        # self.pop_list = self.tempPopList



        self.tick += 1