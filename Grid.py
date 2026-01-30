from random import randint
import pygame as pg
from Ecosysteme import *
from Wolf import Wolf
from Sheep import Sheep
from Square import Square
import numpy as np


class Grid :
    def __init__(self,GRID_SIZE,CUBE):
        self.running = True
        self.GRID_SIZE=GRID_SIZE
        self.cube= CUBE
        self.wolf_list=[Wolf for _ in range(INITIAL_WOLVES)]
        self.sheep_list=[Sheep for _ in range(INITIAL_SHEEP)]
        # self.mouton_img = pg.image.load("mouton.png").convert_alpha()
        # self.mouton_img = pg.transform.scale(self.mouton_img,(self.cube, self.cube))
        self.grid = np.empty((self.GRID_SIZE, self.GRID_SIZE), dtype=object)
        self.vert=(20, 148, 20)
        for x in range(self.GRID_SIZE):
            for y in range(self.GRID_SIZE):
                self.grid[x,y]=Square(x,y)
        
            
    def run(self):
        pg.init()
        self.screen = pg.display.set_mode((self.cube*self.GRID_SIZE, self.cube*self.GRID_SIZE))
        self.loup_img = pg.image.load("loup.png").convert_alpha()
        self.mouton_img = pg.transform.scale(self.loup_img,(self.cube, self.cube))
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
            #on ajout l'age 
            self.incrementer_age()
            #array de booleen( true = herbe)
            self.affiche_herbe()
            self.maj_animaux()
            self.maj_mort()
            self.reproduction()
            self.affiche_animaux()
            
            #on met à jour
            pg.display.update()
            clock.tick(5)

        pg.quit()
    
    def affiche_herbe(self):
        for x in range(self.GRID_SIZE):
            for y in range(self.GRID_SIZE):
                self.grid[x,y].growth()
                if self.grid[x,y].grass :
                    rect = pg.Rect(x*self.cube, y*self.cube, self.cube, self.cube)
                    pg.draw.rect(self.screen, self.vert, rect)

    def incrementer_age(self):
        for i in range(len(self.sheep_list)):
            self.sheep_list[i].age+=1
        for j in range(len(self.wolf_list)):
            self.wolf_list[j].age+=1
    
    def maj_animaux(self):
        for mouton in self.sheep_list:
            mouton.move_eat(self.grid)
            mouton.energy-=SHEEP_ENERGY_LOSS_PER_TURN
        for loup in self.wolf_list_list:
            self.sheep_list=loup.move_eat(self.grid,self.sheep_list)
            loup.energy-=WOLF_ENERGY_LOSS_PER_TURN
    
    def maj_mort(self): 
        for mouton in self.sheep_list:
            if mouton.energy<=0 or mouton.age>=SHEEP_MAX_AGE :
                self.sheep_list.remove(mouton)
        for loup in self.sheep_list:
            if loup.energy<=0 or loup.age>=WOLF_MAX_AGE :
                self.sheep_list.remove(loup)
    
    
    def affiche_animaux(self):
        self.mouton_img = pg.image.load("mouton.png").convert_alpha()
        for mouton in self.sheep_list:
            x,y=mouton.x, mouton.y
            pixel_x = x * self.cube + self.cube // 2
            pixel_y = y * self.cube + self.cube // 2
            rect = self.mouton_img.get_rect(center=(pixel_x, pixel_y))
            self.screen.blit(self.mouton_img, rect)
        for loup in self.wolf_list_list:
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


