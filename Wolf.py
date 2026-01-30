import random
from Square.py import Square    


class Wolf:
    def __init__(self, x, y, Grid, grid_size
                 WOLF_INITIAL_ENERGY, 
                 WOLF_ENERGY_LOSS_PER_TURN, 
                 WOLF_ENERGY_FROM_SHEEP, 
                 WOLF_REPRODUCTION_THRESHOLD,
                 REPRODUCTION_ENERGY_COST,
                 WOLF_MAX_AGE,):
        self.x = x
        self.y = y
        self.grid_size = grid_size
        self.energy = WOLF_INITIAL_ENERGY
        self.age = 0
        self.energy_loss_per_turn = WOLF_ENERGY_LOSS_PER_TURN
        self.energy_from_grass = WOLF_ENERGY_FROM_SHEEP
        self.reproduction_threshold = WOLF_REPRODUCTION_THRESHOLD
        self.reproduction_energy_cost = REPRODUCTION_ENERGY_COST
        self.max_age = WOLF_MAX_AGE
        self.directions = [(0,1), (1,0), (0,-1), (-1,0)]

    def move(self):
        x = self.x
        y = self.y
        grid_size = self.grid_size
        for dx, dy in directions:
            if 0 <= x + dx < grid_size and 0 <= y + dy < grid_size:  # on vérifie les limites de la grille
                x += dx
                y += dy


    def directions_possible(self):
        directions_possible = []
   
        for dx, dy in self.directions:
            if 0 <= self.x + dx < self.grid_size and 0 <= self.y + dy < self.grid_size and not (square_near.has_sheep() or square_near.has_wolf()):  # on vérifie les limites de la grille # on vérifie qu'il n'y a pas déjà un mouton ou un loup
                directions_possible.append((dx, dy)) # on ajoute la direction possible à la liste
        return directions_possible
    

    def move(self):
        x = self.x
        y = self.y
  
        cases_with_grass = []

        for dx, dy in self.directions_possible():
            square_near = Square(x +dx, y +dy)  # on crée une instance de Square pour la case voisine
            
            if square_near.has_sheep(): # on vérifie s'il y a de l'herbe
                cases_with_grass.append((x + dx, y + dy)) # on ajoute les coordonnées de la case avec herbe à la liste

        if cases_with_grass:
            self.x, self.y = random.choice(cases_with_sheep)  # on choisit une case avec de l'herbe au hasard

        else:
            dx, dy = random.choice(self.directions_possible())  # on choisit une direction au hasard
            self.x += dx
            self.y += dy
    

    def eat(self):
        square = Square(self.x, self.y)
        if square.has_sheep():
            sheep.remove_sheep()
            self.energy += self.energy_from_sheep
    

    def reproduce(self): 
        if self.energy >= self.reproduction_threshold:
            self.energy -= self.reproduction_energy_cost
            dx, dy = random.choice(self.directions_possible())
            return Wolf(self.x + dx, self.y + dy, self.grid_size,  # on crée un nouveau mouton 
                         self.energy_initial,         # on pourra modifier les caractéristiques plus tard
                         self.energy_loss_per_turn,
                         self.energy_from_grass,
                         self.reproduction_threshold,
                         self.reproduction_energy_cost,
                         self.max_age)
        return None

