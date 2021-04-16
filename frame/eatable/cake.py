from .food import Food
from .loc_conf import STRECH_COUNT

class Cake(Food):

    eated_cake = False
    cake_countdown = STRECH_COUNT

    image_path = "assets/Powerup/powerup_kuchen.png"

    def __init__(self, screen):
        Food.__init__(self, screen, Cake.image_path)
    
    @staticmethod
    def got_cake():
        Cake.eated_cake = True

    @staticmethod
    def eated_the_cake():
        return Cake.eated_cake

    @staticmethod
    def remove_cake():
        Cake.eated_cake = False
        Cake.cake_countdown = STRECH_COUNT
    
    @staticmethod
    def decrase_cake_countdown():
        Cake.cake_countdown -= 1

    @staticmethod
    def get_cake_countdown():
        return Cake.cake_countdown
    
    

    
