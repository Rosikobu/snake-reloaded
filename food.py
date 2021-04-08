from eatable import Eatable

class Food(Eatable):   
     
    def __init__(self, screen, image_path):
        Eatable.__init__(self, screen, image_path)

