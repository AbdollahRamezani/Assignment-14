import arcade
from bullet import Bullet

class Spaceship(arcade.Sprite):

    def __init__(self, game) :  #در اینجا پارامتر گیم از کلاس گیم با پارامتر سلف فرستاده شده است 
       super().__init__(":resources:images/space_shooter/playerShip1_green.png")
       self.center_x=game.width//2  #پراپرتی سنتر از قبل تعریف شده
       self.center_y=80
       self.change_x=0
       self.change_y=0
       self.width=48
       self.height=48
       self.speed=4
       self.game_width=game.width  # برای اینکه بتوان از پارامتر گیم .وید در متدهای دیگر نیز مانند مت موو استفاده کرد 
                                   #باید آنرا داخل پراپرتی سلف از خود کلاس اسپیسشیپ ریخته شود
       self.bullet_list = []

    def move(self):
        if self.change_x == 1:
            if self.center_x < self.game_width :
                self.center_x+=self.speed
        elif self.change_x == -1: 
            if self.center_x > 0 :   
                self.center_x-=self.speed

    def fire(self):
        new_bullet = Bullet(self)  #در اينجا سلف به عنوان پارامتر به کلاس  بولت ارسال میشه و در کلاس بولت با پارامتر هاست دریافت میشود
        self.bullet_list.append(new_bullet)