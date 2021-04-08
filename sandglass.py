import random
import pygame
from pygame.math import Vector2
from config import xSize, ySize, cell_size, cell_number, TIME_TO_SLOW
from food import Food
from powerup import Powerup

class Sandglass(Powerup):

    image_path = "assets/Powerup/powerup_sanduhr.png"
    def __init__(self, screen):
        Powerup.__init__(self, screen, Sandglass.image_path)
        self.slow = False
        self.countdown = 0

    #@staticmethod
    def ticks(self):
        self.countdown += 1
        if self.countdown % 2 == 0 and self.countdown < TIME_TO_SLOW:
            return True
        elif self.countdown > TIME_TO_SLOW:
            self.slow = False
            self.countdown = 0
            return True

    #@staticmethod
    def slowering(self):
        self.slow = True

    #@staticmethod
    def is_slowered(self):
        return self.slow