class Agent:

    def __init__(self,simulator):
        self.health = 100
        self.hunger = 0
        self.alive = True
        self.tick = simulator.tick
        # print("Agent Created at tick ", self.tick)

    def step(self):

        self.hunger = min(100, self.hunger + 4.16)
        # print("Hunger: ", self.hunger, " Health: ", self.health)

        if self.hunger == 100:
            self.health = max(0, self.health - 1)

        if self.health <= 0:
            # print("Agent Died at tick ", self.tick)
            self.alive = False
            return

        self.tick += 1

        #REST OF STEP TO HAPPEN EACH TICK



