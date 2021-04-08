from non_eatable import NonEatable

class Rock(NonEatable):

    ip1 = "assets/Hindernis/rock.png"
    ip2 = "assets/Hindernis/rock.png"
    ip3 = "assets/Hindernis/rock.png"
    ip4 = "assets/Hindernis/rock.png"

    def __init__(self, screen):
        NonEatable.__init__(self, screen, Rock.ip1,Rock.ip2,Rock.ip3,Rock.ip4)