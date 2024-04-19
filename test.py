from simulationworld import SimulationWorld
from cell import Cell

import random

if __name__ == '__main__':
    simulation_world = SimulationWorld()
    simulation_world.cell_list = [Cell(random.randint(0,600), random.randint(0,600), simulation_world.world) for _ in range(10)]
    simulation_world.run_game()
