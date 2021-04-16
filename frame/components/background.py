import random
import pygame
from pygame.math import Vector2

from .loc_conf import xSize, ySize, cell_size, cell_number

class Background:

    def __init__(self, screen):
        self.pyScreen = screen
        self.position = Vector2(0,0)
        
        image_path = "assets/Spielwelt/spielwelt.png"
        self._load_texture(image_path)

    def _load_texture(self, image_path):
        self.background_texture = self.food_texture = pygame.image.load(image_path).convert_alpha()

    def draw_background(self):
        background_obj = pygame.Rect(int(self.position.x),int(self.position.y),cell_size,cell_size)
        self.pyScreen.blit(self.background_texture,background_obj)