import random as rd

class Square:
    #Coordonnées
    x = 0
    y = 0
    #Paramètres d'état de la case
    grass = False
    sheep = False
    wolf = False
    time_before_regrowth = -1 #-1 si  ce temps n'est pas défini
    
    p_growth = 0.0 #Probabilité que l'herbe pousse sur la case
    GRASS_REGROWTH_TIME = 7
    
    def __init__ (self, x, y, p): #p est la probabilité que l'herbe pousse 
        self.x = x
        self. y = y
        self.p_growth = p
        self.grass = rd.choices([False, True], weights=[1 - p, p])[0]
        
    def growth (self) :
        "l'herbe repousse après un certain temps et de menière aléatoire"
        if self.time_before_regrowth == 0:
            self.grass = True
            self.time_before_regrowth = -1
       
    def sheep_arrival(self):
        "Lorsqu'un mouton arrive sur la case cette fonction est appelée, si elle renvoie True il gagne de l'énergie"
        if self.grass == True:
            self.grass = False
            self.time_before_regrowth = self.GRASS_REGROWTH_TIME
            return True
        return False