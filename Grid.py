from random import randint
import pygame as pg



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
        

if __name__ == "__main__":
    print("lancer")
    jeu=Grid
    