from simulator import Simulator

simulator = Simulator()

simulator.setup(1)

for i in range(500000):
    if len(simulator.pop_list) == 0:
        print("No Agents Left - Simulation Complete at tick", + simulator.tick)
        break
    simulator.step()

