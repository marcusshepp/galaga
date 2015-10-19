class Alien:

    """ 2D game object. """

    def __init__(self, location_x, location_y):
        self.location_x = location_x
        self.location_y = location_y
        self.change_x = 0
        self.change_y = 0

    def move(self, change_x, change_y):
        if self.location_x > 649 or self.location_x < 0:
            self.change_x *= change_x
        if self.location_y > 449 or self.location_y < 0:
            self.change_y *= change_y
