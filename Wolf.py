import random
from Square import Square
from Grid import Grid
from Ecosysteme import *

class Wolf:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        #pompe ecosysteme
        self.grid_size = GRID_SIZE
        self.energy = WOLF_INITIAL_ENERGY
        self.age = 0
        self.energy_loss_per_turn = WOLF_ENERGY_LOSS_PER_TURN
        self.energy_from_sheep = WOLF_ENERGY_FROM_SHEEP
        self.reproduction_threshold = WOLF_REPRODUCTION_THRESHOLD
        self.reproduction_energy_cost = REPRODUCTION_ENERGY_COST
        self.max_age = WOLF_MAX_AGE
        self.directions = [(0,1), (1,0), (0,-1), (-1,0)]


    def directions_possible(self):
        directions_possible = []
   
        for dx, dy in self.directions:
            if 0 <= self.x + dx < self.grid_size and 0 <= self.y + dy < self.grid_size and not Square(self.x,self.y).wolf():  # on vérifie les limites de la grille # on vérifie qu'il n'y a pas déjà un mouton ou un loup
                directions_possible.append((dx, dy)) # on ajoute la direction possible à la liste
        if directions_possible == [] :
            return False
        return directions_possible
    

    def move_eat(self):
  
        cases_with_sheep = []

        for dx, dy in self.directions_possible():
            square_near = Square(self.x+dx, self.y+dy)  # on crée une instance de Square pour la case voisine
            
            if square_near.sheep(): # on vérifie s'il y a un mouton
                cases_with_sheep.append((self.x + dx, self.y + dy)) # on ajoute les coordonnées de la case avec mouton à la liste

        if cases_with_sheep == []:
            dx, dy = random.choice(self.directions_possible())  # on choisit une direction au hasard
            self.x += dx
            self.y += dy

        else:
            dx, dy = random.choice(cases_with_sheep)  # on choisit une direction au hasard
            self.x += dx
            self.y += dy

            i = 0
            for ship in Grid.sheep_list :
                i+=1
                if ship.x == self.x and ship.y == self.y :
                    Grid.sheep_list.pop(i)
                continue
            self.energy += self.energy_from_sheep

        return Grid.sheep_list
    

    def reproduce(self):

        if self.energy >= self.reproduction_threshold:
            self.energy -= self.reproduction_energy_cost
            dx, dy = random.choice(self.directions_possible())
            Grid.wolf_list.append(Wolf(self.x + dx, self.y + dy)) #changer la liste de la grid

