from snake import Snake
from mouse import Mouse
from sandglass import Sandglass
from cheese import Cheese
from saw import Saw
from cake import Cake
from bush import Bush
from rock import Rock
from peel import Peel
from poison import Poison

from config import SCOREPOINTS_CHEESE,SCOREPOINTS_MAUSE,SCOREPOINTS_SAW,SCOREPOINTS_SANDGLASS,SCOREPOINTS_CAKE
from config import cell_number, cell_size, SPAWNING_MOUSE_ON_CHEESE, PROBABILITY_FOR_CAKE 
from config import PROBABILITY_FOR_SANDGLASS, PROBABILITY_FOR_SAW, MAX_ELEMENTS_ON_MAP
from config import PROBABILITY_FOR_CHEESE, PROBABILITY_FOR_PEEL, PROBABILITY_FOR_POISON, PROBABILITY_FOR_MOUSE

from pygame.math import Vector2
import random
import pygame, sys
from typing import List
import sound_controller

class Model(object):

    def __init__(self, screen, snake, sandglass, saw, score, food_list, barrier_list, peel):
        
        self.score = score
        self.snake = snake
        self.screen = screen
        self.sandglass = sandglass
        self.peel = peel
        self.saw = saw     
        self.barrier_list = barrier_list
        self.food_list = food_list
        self.count = 0
        self.time_to_add_a_barrier = 0

        # add Eatable items
        self.add_food_item(Mouse(self.screen))
        self.add_food_item(Mouse(self.screen))
        self.add_food_item(Sandglass(self.screen))

        # add Non-Eatable items
        self.add_barrier_item(Bush(self.screen))
        self.add_barrier_item(Bush(self.screen))
        self.add_barrier_item(Bush(self.screen))

        self.calc_probability()

    def calc_probability(self):
        self.PROBABILITY = []
        for _ in range(PROBABILITY_FOR_CAKE):
            self.PROBABILITY.append(Cake)
        for _ in range(PROBABILITY_FOR_SANDGLASS):
            self.PROBABILITY.append(Sandglass)    
        for _ in range(PROBABILITY_FOR_CHEESE):
            self.PROBABILITY.append(Cheese) 
        for _ in range(PROBABILITY_FOR_SAW):
            self.PROBABILITY.append(Saw)
        for _ in range(PROBABILITY_FOR_PEEL):
            self.PROBABILITY.append(Peel)
        for _ in range(PROBABILITY_FOR_POISON):
            self.PROBABILITY.append(Poison)

    # Snake zeichnen lassen unter Berücksichtigung von bestimmten Powerups (Sanduhr, Kaffee)
    def update_snake(self) -> None:
       
        if self.sandglass.is_slowered():
            if self.sandglass.ticks():
                self.snake.move_snake()
        else:
            self.snake.move_snake()

    def update_barriers(self):
        if self.time_to_add_a_barrier > 10:
            self.add_barrier_item(Bush(self.screen))
            self.time_to_add_a_barrier = 0

    # Snake steuern
    def change_direction(self, event: pygame.event):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and Snake.is_moving == False:
                Snake.is_moving = True
                if self.peel.is_reversed():
                    if self.snake.direction.y != -1:
                        self.snake.set_direction(Vector2(0,1))
                else:
                    if self.snake.direction.y != 1:
                        self.snake.set_direction(Vector2(0,-1))

            if event.key == pygame.K_DOWN and Snake.is_moving == False:
                Snake.is_moving = True
                if self.peel.is_reversed():
                    if self.snake.direction.y != 1:   
                        self.snake.set_direction(Vector2(0,-1))
                else:
                    if self.snake.direction.y != -1:   
                        self.snake.set_direction(Vector2(0,1))

            if event.key == pygame.K_RIGHT and Snake.is_moving == False:
                Snake.is_moving = True
                if self.peel.is_reversed():
                    if self.snake.direction.x != 1:
                        self.snake.set_direction(Vector2(-1,0))
                else:
                    if self.snake.direction.x != -1:
                        self.snake.set_direction(Vector2(1,0)) 

            if event.key == pygame.K_LEFT and Snake.is_moving == False:
                Snake.is_moving = True
                if self.peel.is_reversed():
                    if self.snake.direction.x != -1:
                        self.snake.set_direction(Vector2(1,0))
                else:
                    if self.snake.direction.x != 1:
                        self.snake.set_direction(Vector2(-1,0))

    def put_new_food(self):

        probability_mause = random.uniform(0.0, 1.0)
        if probability_mause < PROBABILITY_FOR_MOUSE:

            obj = random.choice(self.PROBABILITY)(self.screen)
            poison_counter = len(list(filter(lambda x: isinstance(x,Poison),self.food_list)))

            while(isinstance(obj,Poison) and poison_counter > 0):
                obj = random.choice(self.PROBABILITY)(self.screen)
            else:
                self.add_food_item(obj)

        else:
            self.add_food_item(Mouse(self.screen))

    def add_food_item(self, food_item):
        not_added = True
        while(not_added):
            if self.is_spawn_ok(food_item):
                self.food_list.append(food_item)
                not_added = False
            else:
                food_item.change_position()
                continue

    def add_barrier_item(self, barrier_item):
        not_added = True
        while(not_added):
            if self.is_spawn_ok(barrier_item):
                self.barrier_list.append(barrier_item)
                not_added = False
            else:
                barrier_item.change_position()
                continue

    def is_spawn_ok(self, item):
        # Eatable
        if isinstance(item,(Mouse,Cake,Cheese,Saw,Sandglass,Peel,Poison)):
            for snake_block in self.snake.body:
                if item.position == snake_block:
                    return False
            for barrier in self.barrier_list:
                for barrier_block in barrier.lis:
                    if item.position == barrier_block:
                        return False 
            for food_item in self.food_list:
                if food_item.position == item.position:
                    return False 
                        
        # Non-Eatable
        elif isinstance(item,(Bush, Rock)):
            for barrier_block in item.lis:
                for snake_block in self.snake.body:
                    if barrier_block == snake_block:
                        return False
                for food_item in self.food_list:
                    if barrier_block == food_item.position:
                        return False
        return True        

    # Kollisionscheck mit Eatable
    def check_collision(self) -> None:
        for food_item in self.food_list:

            if food_item.position == self.snake.body[0]:
                
                score_points = self.check_food_for_score(food_item)
                self.score.set_score(self.score.get_score() + score_points)
                self.time_to_add_a_barrier += score_points

                self.food_list.remove(food_item)                # remove obj in ur collision
                                              
                if(len(self.food_list) < MAX_ELEMENTS_ON_MAP):
                    self.put_new_food()                         # Füge neues Objekt in die Liste der Essbaren Gegenstände
                                                                # in der Spielwelt
                self.check_powerup(food_item)                   # Check if powerup
                self.snake.add_block()                          # extend snake

        for barrier in self.barrier_list:
            for item in barrier.lis:
                if item == self.snake.body[0]:
                    self.game_over()
           
    # Check food for Score and play soundeffects
    def check_food_for_score(self,food_item):
        if isinstance(food_item,Cheese):
            sound_controller.cheese_sound.play()
            return SCOREPOINTS_CHEESE
        elif isinstance(food_item,Mouse):
            sound_controller.mouse_sound.play()
            return SCOREPOINTS_MAUSE
        elif isinstance(food_item,Saw):
            sound_controller.sage_sound.play()
            return SCOREPOINTS_SAW
        elif isinstance(food_item,Sandglass):
            sound_controller.timeglass_sound.play()
            return SCOREPOINTS_SANDGLASS
        elif isinstance(food_item,Cake):
            #sound_controller.cheese_sound.play()
            return SCOREPOINTS_CAKE
        else:
            return 0

    # Check for Powerups
    def check_powerup(self, obj) -> None:
        if isinstance(obj, Poison):
            self.game_over()
        elif(isinstance(obj,Sandglass)):
            self.sandglass.slowering()
        elif(isinstance(obj,Saw)):
            Saw.cutting()
        elif(isinstance(obj,Cheese)):
            self.spawn_new_mouses()
        elif(isinstance(obj,Cake)):
            self.cake_debuff()
        elif(isinstance(obj,Peel)):
            self.peel_debuff()
    
    def cake_debuff(self):
        Cake.got_cake()

    def peel_debuff(self):
        self.peel.reverse()

    def spawn_new_mouses(self):
        for _ in range(SPAWNING_MOUSE_ON_CHEESE):
            self.add_food_item(Mouse(self.screen))    
        

    # Kollisionscheck Wände
    def check_fail(self) -> None:
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
        
    def game_over(self) -> None:

        self.snake.direction = Vector2(1,0)
        self.food_list.clear()
        self.barrier_list.clear()
        for _ in range(3):
            self.add_food_item(Mouse(self.screen))
        for _ in range(3):
            self.add_barrier_item(Bush(self.screen))

        self.score.set_score(0)
        self.snake.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]

        if self.peel.is_reversed():
            self.peel.reverse()
        
    