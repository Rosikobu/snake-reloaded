import pygame, sys
from typing import List, Tuple
import time
from pygame.math import Vector2

from .snake import Snake
from .eatable.mouse import Mouse
from .model import Model
from .eatable.sandglass import Sandglass
from .eatable.peel import Peel
from .components import sound_controller
from .eatable.saw import Saw
from .components.background import Background
from .config import FPS, xSize, ySize, SPEED
from .components.score import Score
from .noneatable.bush import Bush

class GUI(object):

    def __init__(self) -> None:
    
        # Fenstersetup
        self.screen = pygame.display.set_mode((xSize,ySize))

        #print(type(screen))
        self.SCREEN_UPDATE = pygame.USEREVENT
        self.clock = pygame.time.Clock()

        # Initialize pygame
        pygame.mixer.pre_init(44100,-16,2,512)
        pygame.init()
        pygame.time.set_timer(self.SCREEN_UPDATE, SPEED)  

        # Erstellen der Objekte
        self.snake = Snake(self.screen)

        # Hintergrund
        self.background = Background(self.screen)

        # Powerups
        self.sandglass = Sandglass(self.screen)
        self.saw = Saw(self.screen)
        self.peel = Peel(self.screen)

        # Score
        self.score = Score(self.screen)

        self.barrier_list = []
        self.food_list = []

        # Logik
        self.model = Model(self.screen, self.snake, self.sandglass, self.saw, self.score, self.food_list, self.barrier_list, self.peel) 

        # Speed Up
        self.speedup = False   

    def update(self) -> None:
        self.model.update_snake()                   # Snake in Gang setzen
        self.model.check_collision()                # Kollisionsprüfung Snake mit Maus
        self.model.check_fail()                     # Kollisionsprüfung mit sich selbst
        self.model.update_barriers()

    def draw_elements(self) -> None:        
        self.background.draw_background()
        
        self.snake.draw_snake()                     # Zeichne Snake
        
        for barrier in self.barrier_list:
            barrier.draw_barrier()
        
        for obj in self.food_list:                 # Zeichne Mäuse
            obj.draw_food()

        self.score.draw_score()

    # Hauptschleife
    def update_display(self) -> None:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:           # Fenster schließen
                pygame.quit()
                sys.exit()

            if event.type == self.SCREEN_UPDATE:    
                self.update()                       # Logik Spielelemente Update

            if event.type == pygame.KEYDOWN:        # Steuerung von Snake Update
                self.model.change_direction(event)

        
        self.draw_elements()                        # Zeiche alle statische Objekte
        pygame.display.update()                     # Update Display