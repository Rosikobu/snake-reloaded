from gui import GUI
from config import FPS
import pygame

class Main(object):

    clock = pygame.time.Clock()

    def __init__(self):
        self.gui = GUI()

    def start(self):
        while True:
            Main.clock.tick(FPS)
            self.gui.update_display()

if __name__ == "__main__":
    Main().start()
