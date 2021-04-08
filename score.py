from config import cell_size, cell_number, FONT_SIZE, PREVIEW_SIZE
from mouse import Mouse

import pygame

class Score():

    def __init__(self, screen):
        self.score_counter = 0
        self.pyScreen = screen
        self._load_texture()
        self.game_font = pygame.font.Font(None,FONT_SIZE)

    def _load_texture(self):
        self.mause_texture = pygame.image.load("assets/Maus/Maus1.png").convert_alpha()
        self.mause_texture = pygame.transform.scale(self.mause_texture, (PREVIEW_SIZE, PREVIEW_SIZE))

    def draw_score(self):
        score_text = str(self.score_counter)
        score_surface = self.game_font.render(score_text, True, (255,0,0))
        
        score_x = int(cell_size*2.5)
        score_y = int(cell_size)

        score_rect = score_surface.get_rect(center = (score_x,score_y))
        mause_rect = self.mause_texture.get_rect(midright = (score_rect.left, score_rect.centery))

        self.pyScreen.blit(score_surface,score_rect)
        self.pyScreen.blit(self.mause_texture,mause_rect)

    def get_score(self):
        return self.score_counter

    def set_score(self,score):
        self.score_counter = score
