import random as rd
from Ecosysteme import GRASS_GROWTH_PROBABILITY, GRASS_REGROWTH_TIME

class Square:
    #Coordonnées
    x = 0
    y = 0
    #Paramètres d'état de la case
    grass = False
    sheep = False
    wolf = False
    time_before_regrowth = -1 #-1 si  ce temps n'est pas défini

    def __init__ (self, x, y): #p est la probabilité que l'herbe pousse 
        "Initialisation de la case"
        self.x = x
        self. y = y
        self.grass = rd.random() < GRASS_GROWTH_PROBABILITY
        
    def growth (self) :
        "L'herbe repousse après un certain temps et de manière aléatoire"
        if self.time_before_regrowth == 0:
            self.grass = True
            self.time_before_regrowth = -1
        elif rd.random() < GRASS_GROWTH_PROBABILITY: #S'il y a déjà de l'herbe ça ne change rien
            self.grass = True
            self.time_before_regrowth = -1
       
    def sheep_arrival(self):
        "Lorsqu'un mouton arrive sur la case cette fonction est appelée, si elle renvoie True il gagne de l'énergie"
        if self.grass == True:
            self.grass = False
            self.time_before_regrowth = self.GRASS_REGROWTH_TIME
            return True
        return False