import random
from Square import Square
from Grid import Grid

class Wolf:
    def __init__(self, x, y, Grid, Square):
        self.x = x
        self.y = y
        '''
        self.grid_size = grid_size
        self.energy = WOLF_INITIAL_ENERGY
        self.age = 0
        self.energy_loss_per_turn = WOLF_ENERGY_LOSS_PER_TURN
        self.energy_from_grass = WOLF_ENERGY_FROM_SHEEP
        self.reproduction_threshold = WOLF_REPRODUCTION_THRESHOLD
        self.reproduction_energy_cost = REPRODUCTION_ENERGY_COST
        self.max_age = WOLF_MAX_AGE
        '''
        self.directions = [(0,1), (1,0), (0,-1), (-1,0)]

    def move(self):
        x = self.x
        y = self.y
        grid_size = self.grid_size
        for dx, dy in Wolf.directions:
            if 0 <= x + dx < grid_size and 0 <= y + dy < grid_size:  # on vérifie les limites de la grille
                x += dx
                y += dy


    def directions_possible(self):
        directions_possible = []
   
        for dx, dy in self.directions:
            if 0 <= self.x + dx < self.grid_size and 0 <= self.y + dy < self.grid_size and not (Square.sheep or Square.wolf()):  # on vérifie les limites de la grille # on vérifie qu'il n'y a pas déjà un mouton ou un loup
                directions_possible.append((dx, dy)) # on ajoute la direction possible à la liste
        if directions_possible == [] :
            return False
        return directions_possible
    

    def move(self):
        x = self.x
        y = self.y
  
        cases_with_sheep = []

        for dx, dy in self.directions_possible():
            square_near = Square(x+dx, y+dy)  # on crée une instance de Square pour la case voisine
            
            if square_near.has_sheep(): # on vérifie s'il y a un mouton
                cases_with_sheep.append((x + dx, y + dy)) # on ajoute les coordonnées de la case avec mouton à la liste

        if cases_with_sheep:
            self.x, self.y = random.choice(square.has_sheep(x,y))  # on choisit une case avec de l'herbe au hasard

        else:
            dx, dy = random.choice(self.directions_possible())  # on choisit une direction au hasard
            self.x += dx
            self.y += dy
    

    def eat(self):
        square = Square(self.x, self.y)
        if square.has_sheep():
            i = 0
            for ship in Grid.sheep_list :
                i+=1
                if ship.x == self.x and ship.y == self.y :
                    Grid.sheep_list.pop(i)
                continue
            self.energy += self.energy_from_sheep
    

    def reproduce(self):

        if self.energy >= self.reproduction_threshold:
            self.energy -= self.reproduction_energy_cost
            dx, dy = random.choice(self.directions_possible())
            #changer la liste de la grid
            Grid.wolf_list.append(Wolf(self.x + dx, self.y + dy, Grid, Square))

