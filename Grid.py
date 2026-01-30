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
        self.wolf_list=[]
        for _ in range(INITIAL_WOLVES):
            x = randint(0, GRID_SIZE)
            y = randint(0, GRID_SIZE)
            self.wolf_list.append(Wolf(WOLF_INITIAL_ENERGY, x, y))
        self.sheep_list=[]
        for _ in range(INITIAL_SHEEP):
            x = randint(0, GRID_SIZE)
            y = randint(0, GRID_SIZE)
            self.sheep_list.append(Sheep(SHEEP_INITIAL_ENERGY, x, y))
        self.grid = np.empty((self.GRID_SIZE, self.GRID_SIZE), dtype=object)
        self.vert=(20, 148, 20)
        for x in range(self.GRID_SIZE):
            for y in range(self.GRID_SIZE):
                self.grid[x,y]=Square(x,y)
            
    def run(self):
        pg.init()
        self.screen = pg.display.set_mode((self.cube*self.GRID_SIZE, self.cube*self.GRID_SIZE))
        self.loup_img = pg.image.load("loup.png").convert_alpha()
        self.loup_img = pg.transform.scale(self.loup_img,(self.cube, self.cube))
        self.mouton_img = pg.image.load("mouton.png").convert_alpha()
        self.mouton_img = pg.transform.scale(self.mouton_img,(self.cube, self.cube))

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

    def incrementer_age(self):
        for mouton in self.sheep_list:
            mouton.age+=1
        for loup in self.wolf_list:
            loup.age+=1
    
    def maj_animaux(self):
        for mouton in self.sheep_list:
            mouton.move_eat(self.grid)
            mouton.energy-=SHEEP_ENERGY_LOSS_PER_TURN
        for loup in self.wolf_list:
            self.sheep_list=loup.move_eat(self.grid,self.sheep_list)
            loup.energy-=WOLF_ENERGY_LOSS_PER_TURN
    
    def maj_mort(self): 
        self.sheep_list = [m for m in self.sheep_list if m.energy > 0 and m.age < SHEEP_MAX_AGE]
        self.wolf_list = [l for l in self.wolf_list if l.energy > 0 and l.age < SHEEP_MAX_AGE]
    
    
    def affiche_animaux(self):
        for mouton in self.sheep_list:
            x,y=mouton.x, mouton.y
            pixel_x = x * self.cube + self.cube // 2
            pixel_y = y * self.cube + self.cube // 2
            rect = self.mouton_img.get_rect(center=(pixel_x, pixel_y))
            self.screen.blit(self.mouton_img, rect)
        for loup in self.wolf_list:
            x,y=loup.x, loup.y
            pixel_x = x * self.cube + self.cube // 2
            pixel_y = y * self.cube + self.cube // 2
            rect = self.loup_img.get_rect(center=(pixel_x, pixel_y))
            self.screen.blit(self.loup_img, rect)
        
    def reproduction(self):
        for mouton in self.sheep_list:
            mouton.reproduce()
        for loup in self.wolf_list:
            loup.reproduce()






    



    
            
        







if __name__ == "__main__":
    print("lancer")
    GRID_SIZE = 20
    CUBE = 30
    jeu=Grid(GRID_SIZE,CUBE)
    jeu.run()


