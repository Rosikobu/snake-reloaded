from .powerup import Powerup

class Saw(Powerup):

    cutted = False
    image_path = "assets/Powerup/powerup_saege.png"

    def __init__(self, screen):
        Powerup.__init__(self, screen, self.image_path)

    @staticmethod
    def cutting():
        Saw.cutted = True

    @staticmethod
    def get_cutted():
        return Saw.cutted

    @staticmethod
    def cutting_done():
        Saw.cutted = False