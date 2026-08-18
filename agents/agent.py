class Agent:

    def __init__(self):
        self.health = 100
        self.hunger = 100
        self.alive = True


    def step(self):

        self.hunger = min(100, self.hunger + 1)

        if self.hunger > 80:
            self.health -= 1

        if self.health <= 0:
            print("Agent Died")
            self.alive = False
            return

        #REST OF STEP TO HAPPEN EACH TICK



