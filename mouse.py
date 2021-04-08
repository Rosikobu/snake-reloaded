from food import Food

class Mouse(Food):

    image_path = "assets/Maus/Maus1.png"

    def __init__(self, screen):
        Food.__init__(self, screen, Mouse.image_path)
