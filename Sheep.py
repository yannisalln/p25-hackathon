import random
from Square.py import Square 

class Cheep:
    def __init__(self, x, y, grid_size, Grid,
                sheep_initial_energy, 
                sheep_energy_loss_per_turn, 
                sheep_energy_from_grass, 
                sheep_reproduction_threshold, 
                reproduction_energy_cost, 
                sheep_max_age
                ):
        self.x = x
        self.y = y
        self.grid_size = grid_size
        self.Grid = Grid
        self.energy_initial = sheep_initial_energy
        self.energy = sheep_initial_energy
        self.age = 0
        self.energy_loss_per_turn = sheep_energy_loss_per_turn
        self.energy_from_grass = sheep_energy_from_grass
        self.reproduction_threshold = sheep_reproduction_threshold
        self.reproduction_energy_cost = reproduction_energy_cost
        self.max_age = sheep_max_age
        self.directions = [(0,1), (1,0), (0,-1), (-1,0)]


    def directions_possible(self):
        directions_possible = []
   
        for dx, dy in self.directions:
            if 0 <= self.x + dx < self.grid_size and 0 <= self.y + dy < self.grid_size and not square_near.has_sheep() and not square_near.has_wolf():  # on vérifie les limites de la grille + pas loup ou mouton
                directions_possible.append((dx, dy)) # on ajoute la direction possible à la liste
        return directions_possible
    

    def move(self):
        x = self.x
        y = self.y
  
        cases_with_grass = []

        for dx, dy in self.directions_possible():
            if 0 <= x + dx < self.grid_size and 0 <= y + dy < self.grid_size:  # on vérifie les limites de la grille
            
                square_near = self.Grid[x +dx][y +dy]  # on crée une instance de Square pour la case voisine
                
            if square_near.has_grass(): # on vérifie s'il y a de l'herbe
                cases_with_grass.append((x + dx, y + dy)) # on ajoute les coordonnées de la case avec herbe à la liste

        if cases_with_grass:
            self.x, self.y = random.choice(cases_with_grass)  # on choisit une case avec de l'herbe au hasard

        if self.directions_possible():
            dx, dy = random.choice(self.directions_possible())  # on choisit une direction au hasard
            self.x += dx
            self.y += dy
    

    def eat(self):
        square = self.Grid[self.x][self.y]
        if square.has_grass():
            square.remove_grass()
            self.energy += self.energy_from_grass
    

    def reproduce(self): 
        if self.energy >= self.reproduction_threshold:
            self.energy -= self.reproduction_energy_cost
            dx, dy = random.choice(self.directions_possible())
            return Sheep(self.x + dx, self.y + dy, self.grid_size, self.Grid,  # on crée un nouveau mouton 
                         self.energy_initial,         # on pourra modifier les caractéristiques plus tard
                         self.energy_loss_per_turn,
                         self.energy_from_grass,
                         self.reproduction_threshold,
                         self.reproduction_energy_cost,
                         self.max_age)
        return None
    













import random
from Square import Square
from Grid import Grid
from Ecosysteme import *

class Sheep:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        #pompe ecosysteme
        self.grid_size = GRID_SIZE
        self.energy = SHEEP_INITIAL_ENERGY
        self.age = 0
        self.energy_loss_per_turn = SHEEP_ENERGY_LOSS_PER_TURN
        self.energy_from_grass = SHEEP_ENERGY_FROM_GRASS
        self.reproduction_threshold = SHEEP_REPRODUCTION_THRESHOLD
        self.reproduction_energy_cost = REPRODUCTION_ENERGY_COST
        self.max_age = SHEEP_MAX_AGE
        self.directions = [(0,1), (1,0), (0,-1), (-1,0)]


    def directions_possible(self):
        directions_possible = []
   
        for dx, dy in self.directions:
            if 0 <= self.x + dx < self.grid_size and 0 <= self.y + dy < self.grid_size and not (Square(self.x, self.y).sheep() or Square(self.x,self.y).wolf()):  # on vérifie les limites de la grille # on vérifie qu'il n'y a pas déjà un mouton ou un loup
                directions_possible.append((dx, dy)) # on ajoute la direction possible à la liste
        return directions_possible
    

    def move_eat(self):
  
        cases_with_grass = []

        for dx, dy in self.directions_possible():
            square_near = Square(self.x+dx, self.y+dy)  # on crée une instance de Square pour la case voisine
            
            if square_near.grass(): # on vérifie s'il y a un mouton
                cases_with_grass.append((x + dx, y + dy)) # on ajoute les coordonnées de la case avec mouton à la liste

        if cases_with_grass == []:
            dx, dy = random.choice(self.directions_possible())  # on choisit une direction au hasard
            self.x += dx
            self.y += dy

        else:
            dx, dy = random.choice(cases_with_grass)  # on choisit une direction miam
            self.x += dx
            self.y += dy
            self.energy += self.energy_from_grass
            Square.sheep_arrival


    def reproduce(self):

        if self.energy >= self.reproduction_threshold:
            self.energy -= self.reproduction_energy_cost
            if self.direction_possible()
            dx, dy = random.choice(self.directions_possible())
            Grid.sheep_list.append(Sheep(self.x + dx, self.y + dy, Grid, Square)) #changer la liste de la grid

