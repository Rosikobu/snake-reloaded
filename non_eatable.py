import pygame
import random
from pygame.math import Vector2
from config import xSize, ySize, cell_size, cell_number

class NonEatable():

    def __init__(self, screen, ip1,ip2,ip3,ip4):
        
        # Lade Textur 
        self._load_texture(ip1,ip2,ip3,ip4)

        # Zufällige Koordinaten für Futter
        
        xPos1 = random.randint(0,cell_number - 2)
        yPos1 = random.randint(0,cell_number - 2)

        while(not self.is_start_pos_ok(xPos1,yPos1)):
            xPos1 = random.randint(0,cell_number - 2)
            yPos1 = random.randint(0,cell_number - 2)
            
        xPos2 = xPos1
        yPos2 = yPos1 + 1

        xPos3 = xPos1 + 1 
        yPos3 = yPos1

        xPos4 = xPos1 + 1
        yPos4 = yPos1 + 1

        self.lis = [Vector2(xPos1,yPos1),Vector2(xPos2,yPos2),Vector2(xPos3,yPos3),Vector2(xPos4,yPos4)]

        self.pyScreen = screen
    
    def is_start_pos_ok(self,xPos1,yPos1):

        if(xPos1 == 6 and yPos1 == 10):
            return False
        if(xPos1 == 7 and yPos1 == 10):
            return False   
        if(xPos1 == 8 and yPos1 == 10):
            return False
        return True

    def _load_texture(self, ip1,ip2,ip3,ip4):
        ''' Laden der Texutren '''
        self.ft1 = pygame.image.load(ip1).convert_alpha()
        self.ft2 = pygame.image.load(ip2).convert_alpha()
        self.ft3 = pygame.image.load(ip3).convert_alpha()
        self.ft4 = pygame.image.load(ip4).convert_alpha()

    def draw_barrier(self):

        food_obj1 = pygame.Rect(int(self.lis[0].x*cell_size),int(self.lis[0].y*cell_size),cell_size,cell_size)
        food_obj2 = pygame.Rect(int(self.lis[1].x*cell_size),int(self.lis[1].y*cell_size),cell_size,cell_size)
        food_obj3 = pygame.Rect(int(self.lis[2].x*cell_size),int(self.lis[2].y*cell_size),cell_size,cell_size)
        food_obj4 = pygame.Rect(int(self.lis[3].x*cell_size),int(self.lis[3].y*cell_size),cell_size,cell_size)

        self.pyScreen.blit(self.ft1, food_obj1)
        self.pyScreen.blit(self.ft2, food_obj2)
        self.pyScreen.blit(self.ft3, food_obj3)
        self.pyScreen.blit(self.ft4, food_obj4)


    def change_position(self):
        xPos1 = random.randint(0,cell_number - 2)
        yPos1 = random.randint(0,cell_number - 2)
        self.lis = [Vector2(xPos1,yPos1),Vector2(xPos1,yPos1+1),Vector2(xPos1+1,yPos1),Vector2(xPos1+1,yPos1+1)]
    

