import random
import pygame
from typing import List, Tuple
from pygame.math import Vector2

from .loc_conf import cell_number, cell_size, cell_number


class Eatable:

    def __init__(self, screen, image_path):

        # Lade Textur für Futter
        self._load_texture(image_path)

        # Zufällige Koordinaten für Futter
        xPos = random.randint(1,cell_number - 2)
        yPos = random.randint(1,cell_number - 2)
        self.position = Vector2(xPos,yPos)
        self.pyScreen = screen

    def change_position(self):
        xPos = random.randint(1,cell_number - 2)
        yPos = random.randint(1,cell_number - 2)
        self.position = Vector2(xPos,yPos)

    def _load_texture(self, image_path):
        ''' Laden der Texutren '''
        self.food_texture = pygame.image.load(image_path).convert_alpha()

    def draw_food(self) -> None:
        food_obj = pygame.Rect(int(self.position.x*cell_size),int(self.position.y*cell_size),cell_size,cell_size)  
        self.pyScreen.blit(self.food_texture, food_obj)
