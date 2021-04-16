import pygame

from .eatable import Eatable

class Powerup(Eatable):
    def __init__(self, screen, image_path):
        Eatable.__init__(self, screen, image_path)