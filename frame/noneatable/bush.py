from .non_eatable import NonEatable

class Bush(NonEatable):

    ip1 ="assets/Hindernis/bush.png"
    ip2 ="assets/Hindernis/bush.png"
    ip3 ="assets/Hindernis/bush.png"
    ip4 ="assets/Hindernis/bush.png"

    def __init__(self, screen):
        NonEatable.__init__(self, screen, Bush.ip1,Bush.ip2,Bush.ip3,Bush.ip4)