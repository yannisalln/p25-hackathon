from random import randint
import pygame as pg
from Ecosysteme import *


class Grid :
    def __init__(self,GRID_SIZE,CUBE):
        self.GRID_SIZE=GRID_SIZE
        self.cube= CUBE

    def trace_initial(self):
        """
        Affiche le terrain tout marron ( base du jeu )

        """
        pg.init()
        marron=(137, 81, 41 ) 
        screen = pg.display.set_mode((self.cube*self.GRID_SIZE, self.cube*self.GRID_SIZE))
        rect = pg.Rect(0,0 ,self.cube*self.GRID_SIZE, self.cube*self.GRID_SIZE)
        pg.draw.rect(screen, marron , rect)
        pg.display.update()

        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

        pg.quit()


if __name__ == "__main__":
    print("lancer")
    GRID_SIZE = 20
    CUBE = 30
    jeu=Grid(GRID_SIZE,CUBE)
    jeu.trace_initial()
