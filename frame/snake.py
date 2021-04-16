import pygame, sys
import time
from pygame.math import Vector2

from .config import FPS, xSize, ySize, cell_size, cell_number, CUTTING
from .eatable.saw import Saw
from .eatable.cake import Cake

class Snake(object):

    is_moving = False

    def __init__(self, screen: pygame.Surface) -> None:

        self.load_snake_texture()

        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.pyScreen = screen
        self.direction = Vector2(1,0)
        self.new_block = False

        self.slowed = False

    def draw_snake_object(self) -> None:
        for index, block in enumerate(self.body):
            # rect for positioning
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            # what direction is tha face
            if index == 0:
                self.pyScreen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                self.pyScreen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    self.pyScreen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    self.pyScreen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        self.pyScreen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        self.pyScreen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        self.pyScreen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        self.pyScreen.blit(self.body_br, block_rect)

    def draw_snake(self) -> None:
        # Update Snake-Model
        self.update_head_graphics()
        self.update_tail_graphics()
        self.draw_snake_object()
        
    def update_tail_graphics(self) -> pygame.Surface:
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(-1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,1): self.tail = self.tail_down

    def update_head_graphics(self) -> pygame.Surface:
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(-1,0): self.head = self.head_left
        elif head_relation == Vector2(1,0): self.head = self.head_right
        elif head_relation == Vector2(0,-1): self.head = self.head_up
        elif head_relation == Vector2(0,1): self.head = self.head_down
        
    def move_snake(self) -> None:    
        if Saw.get_cutted() == False or len(self.body) < (abs(CUTTING)+1):
            if self.new_block == True:
                body_copy = self.body[:]
                body_copy.insert(0, body_copy[0] + self.direction)
                self.body = body_copy[:]
                
                if Cake.eated_the_cake():
                    if Cake.get_cake_countdown() != 0:
                        Cake.decrase_cake_countdown()
                    else:
                        Cake.remove_cake()
                        self.new_block = False
                else:
                    self.new_block = False        
            else:
                body_copy = self.body[:-1]
                body_copy.insert(0, body_copy[0] + self.direction)
                self.body = body_copy[:]      
        else:
            self.new_block = False
            body_copy = self.body[:CUTTING]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

        Saw.cutting_done()
        Snake.is_moving = False

    def set_direction(self, vec) -> pygame.Surface:
        #Snake.is_moving = True
        self.direction = vec

    def add_block(self) -> None:
        self.new_block = True

    def load_snake_texture(self) -> pygame.Surface:

        # Kopf
        self.head_up = pygame.image.load('assets/Schlange/Schlange_Kopf_oben.png')
        self.head_right = pygame.image.load('assets/Schlange/Schlange_Kopf_rechts.png')
        self.head_left = pygame.image.load('assets/Schlange/Schlange_Kopf_links.png')
        self.head_down = pygame.image.load('assets/Schlange/Schlange_Kopf_unten.png')

        # Schwanz
        self.tail_up = pygame.image.load('assets/Schlange/Schlange_Schwanz_oben.png')
        self.tail_down = pygame.image.load('assets/Schlange/Schlange_Schwanz_unten.png')
        self.tail_right = pygame.image.load('assets/Schlange/Schlange_Schwanz_rechts.png')
        self.tail_left = pygame.image.load('assets/Schlange/Schlange_Schwanz_links.png')

        # Körper
        self.body_vertical = pygame.image.load('assets/Schlange/Schlange_vertikal.png')
        self.body_horizontal = pygame.image.load('assets/Schlange/Schlange_horizontal.png')

        # Directions
        self.body_tr = pygame.image.load('assets/Schlange/Schlange_Ecke_rechts_oben.png')
        self.body_tl = pygame.image.load('assets/Schlange/Schlange_Ecke_links_oben.png')
        self.body_br = pygame.image.load('assets/Schlange/Schlange_Ecke_rechts_unten.png')
        self.body_bl = pygame.image.load('assets/Schlange/Schlange_Ecke_links_unten.png')