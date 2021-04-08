from powerup import Powerup 
from config import TIME_TO_REVERSE

class Poison(Powerup):

    image_path = "assets/Powerup/powerup__gift_v3.png"

    def __init__(self, screen):
        Powerup.__init__(self, screen, Poison.image_path)
