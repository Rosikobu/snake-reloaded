from food import Food

class Cheese(Food):

    image_path = "assets/Powerup/powerup_kaese.png"

    def __init__(self, screen):
        Food.__init__(self, screen, Cheese.image_path)

    
