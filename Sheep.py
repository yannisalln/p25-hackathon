import random

class Sheep:
    def __init__(self, x, y,
                 SHEEP_INITIAL_ENERGY, 
                 SHEEP_ENERGY_LOSS_PER_TURN, 
                 SHEEP_ENERGY_FROM_GRASS, 
                 SHEEP_REPRODUCTION_THRESHOLD,
                 REPRODUCTION_ENERGY_COST,
                 SHEEP_MAX_AGE,
                 ):
        self.x = x
        self.y = y
        self.energy = SHEEP_INITIAL_ENERGY
        self.age = 0
        self.energy_loss_per_turn = SHEEP_ENERGY_LOSS_PER_TURN
        self.energy_from_grass = SHEEP_ENERGY_FROM_GRASS
        self.reproduction_threshold = SHEEP_REPRODUCTION_THRESHOLD
        self.reproduction_energy_cost = REPRODUCTION_ENERGY_COST
        self.max_age = SHEEP_MAX_AGE

    def move(self, grid_size):
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for 