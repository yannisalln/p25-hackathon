from random import randint
import pygame as pg
from Ecosysteme import *
import Sheep
import Wolf 
from Grass import Square
import numpy as np 


class Grid :
    def __init__(self,GRID_SIZE,CUBE):
        self.running = True
        self.GRID_SIZE=GRID_SIZE
        self.cube= CUBE
        self.mouton_img = pg.image.load("mouton.png").convert_alpha()
        self.mouton_img = pg.transform.scale(self.mouton_img,(self.cube, self.cube))
        self.grid = np.empty((self.GRID_SIZE, self.GRID_SIZE), dtype=object)
        self.vert=(20, 148, 20)
        for x in range(self.GRID_SIZE):
            for y in range(self.GRID_SIZE):
                self.grid[x,y]=Square(x,y)
            
    def run(self):
        pg.init()
        self.screen = pg.display.set_mode((self.cube*self.GRID_SIZE, self.cube*self.GRID_SIZE))

        clock = pg.time.Clock()

        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            
            # moutons = self.ecosysteme.positionsmoutons()
            #à chaque boucle, on retrace tout
            #écran marron
            marron=(137, 81, 41)
            self.screen.fill(marron)
            #on dessine l'herbe
            #array de booleen( true = herbe)
            self.affiche_herbe()
            # #on dessine les moutons
            # self.affiche_moutons(moutons)
            # #on dessine les loups 
            # self.affiche_loups(loups)
            #on met à jour
            pg.display.update()
            clock.tick(60)

        pg.quit()
    
    def affiche_herbe(self):
        for x in range(self.GRID_SIZE):
            for y in range(self.GRID_SIZE):
                self.grid[x,y].growth()
                if self.grid[x,y].grass :
                    rect = pg.Rect(x*self.cube, y*self.cube, self.cube, self.cube)
                    pg.draw.rect(self.screen, self.vert, rect)
        







if __name__ == "__main__":
    print("lancer")
    GRID_SIZE = 20
    CUBE = 30
    jeu=Grid(GRID_SIZE,CUBE)
    jeu.run()


