import arcade

class Herat(arcade.Sprite):
    def __init__(self, x):
        super().__init__("heart.png")
        self.center_x = 30*x
        self.center_y = 35
        self.width = 25
        self.height = 25