from powerup import Powerup 
from config import TIME_TO_REVERSE

class Peel(Powerup):

    image_path = "assets/Powerup/powerup_bananenschale.png"
    
    def __init__(self, screen):
        Powerup.__init__(self, screen, Peel.image_path)
        self.rev = False
        
    def reverse(self):
        self.rev = not self.rev

    def is_reversed(self):
        return self.rev