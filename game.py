import random
import arcade   # pip install arcade  #pip install arcade==2.5 ورژن دلخواه
from spaceship import Spaceship
from enemy import Enemy
from heart import Herat


class Game (arcade.Window):
    def __init__(self) :
        super().__init__(width=800 , height=600, title="Interstellar Game 2023")  # بک گراند سیاه رنگ
        arcade.set_background_color(arcade.color.BLACK)  # بک گراند سیاه رنگ
        self.background=arcade.load_texture(":resources:images/backgrounds/stars.png")   # عکس بک گراند ستاره
        self.me=Spaceship(self) #چون هواپیمای خودی بخشی از بازی است بهتراست این شی را یکی از پراپر تیهای کلاس گیم بسازیم 
                                #در اینجا سلف از کلاس گیم هست که به صورت یک پارامتر برای کلاس اسپیسشیپ  فرستاده میشود
        
        self.enemy_list= []
        self.heart_list = [] 
        self.score = 0
        for x in range(1,4):
            self.heart = Herat(x)
            self.heart_list.append(self.heart)
            
    def on_draw(self):  
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)   # عکس بک گراند ستاره
        self.me.draw() 
        arcade.draw_text(f"Score: {self.score}", 650,30,arcade.color.WHITE,20, font_name= "Titr")
        if len(self.heart_list)<=0 :
           arcade.draw_rectangle_filled(0, 0, 1800, 1500, arcade.color.BLACK)
           arcade.draw_text("GAME OVER", 280,300,arcade.color.YELLOW,33, font_name= "Arial")
           self.enemy_list = []
           
        for enemy in self.enemy_list:
            enemy.draw()  

        for bullet in self.me.bullet_list:
            bullet.draw()  

        for heart in self.heart_list:
            heart.draw()     
  
        arcade.finish_render()   

    def on_key_press(self, symbol: int, modifiers: int):  
        if symbol==arcade.key.RIGHT or symbol==arcade.key.D: 
            self.me.change_x = 1
        elif symbol==arcade.key.LEFT or symbol==arcade.key.A:  
            self.me.change_x = -1
        elif symbol== arcade.key.DOWN :
            self.me.change_x = 0    
        elif symbol==arcade.key.SPACE:  
               self.me.fire()  

    def on_key_release(self, symbol: int, modifiers: int):
          self.me.change_x = 0  

    def on_update(self, delta_time: float):  
        self.me.move()

        if random.randint(1, 130)==6: 
            self.new_enemy = Enemy(self)
            self.enemy_list.append(self.new_enemy)

        for enemy in self.enemy_list:
         enemy.move()    

        for enemy in self.enemy_list :
            if arcade.check_for_collision(self.me, enemy) :  # مقایسه برخورد هواپیمای خودی و دشمن
                print("Game Over !!!")
                exit(0)

        for enemy in self.enemy_list:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(enemy, bullet):
                    self.enemy_list.remove(enemy)
                    self.me.bullet_list.remove(bullet)
                    self.score+=1

                   
        for enemy in self.enemy_list:
            if enemy.center_y < 0:      
                self.enemy_list.remove(enemy)  
                if len(self.heart_list) > 0:
                  self.heart_list.pop(-1)      
                 

        for bullet in self.me.bullet_list:
            bullet.move()    

        


window=Game()   
arcade.run()  
        
