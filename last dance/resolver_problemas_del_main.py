import tkinter as tk
from PIL import Image as PilImage, ImageTk as PilImageTk
from tkinter import NW
from Player import Player
import random
from Enemies import Enemy
from Bullet import Bullet

class Main:
    def __init__(self):
        self.window = tk.Tk()
        self.ancho_fondo = self.window.winfo_screenwidth()
        self.alto_fondo = self.window.winfo_screenheight()
        self.frames = []
        
        self.current_frame = 0
        self.load_gif('gif_fondo.gif')
        
        self.canvas = tk.Canvas(self.window, width=self.ancho_fondo, height=self.alto_fondo)
        self.window.geometry(f"{self.ancho_fondo}x{self.alto_fondo}")
        self.canvas.pack()

        self.background_image = self.canvas.create_image(0, 0, image=self.frames[0], anchor = 'nw')

        self.animate_gif()
        
        player = Player(self.ancho_fondo,self.alto_fondo, self.canvas, self.window)
        
        self.player = player
        
        self.enemies = [] 
        self.create_enemies()
        
        self.update_game()
        
    def load_gif(self, gif_path):
        self.gif = PilImage.open(gif_path)
        for frame in range(0, self.gif.n_frames):
            self.gif.seek(frame)
            frame_image = PilImageTk.PhotoImage(self.gif.copy().resize((self.ancho_fondo,self.alto_fondo), PilImage.LANCZOS))
            self.frames.append(frame_image)
        

    def animate_gif(self):
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.canvas.itemconfig(self.background_image, image=self.frames[self.current_frame])
        self.window.after(100, self.animate_gif)

    def create_enemies(self):
        counter_for_x = 1
        y = 50
        for i in range(48):
            gif_paths = ["enemies/enemy1.gif", 
                        "enemies/enemy2.gif", 
                        "enemies/enemy3.gif"]
            if i % 12 == 0:
                counter_for_x = 0
            
            if i == 0 or i % 12 == 0 :
                x = 60 
            else:
                x = (counter_for_x + 1) * 100
            
            if i < 12:
                y = y
                counter_for_x += 1
                
            elif i >= 12 and i < 24:
                y = 150
                counter_for_x += 1
                
            elif i >= 24 and i < 36:
                y = 250
                counter_for_x += 1

            elif i >= 36 and i <= 48:
                y = 350
                counter_for_x += 1

            gif_path = random.choice(gif_paths)
            enemy = Enemy(x, y , health = 20, speed= 1, gif_path=gif_path, canvas= self.canvas, window= self.window ) 
            self.enemies.append(enemy)
            
    def update_game(self):
        for bullet in self.player.bullets[:]:
            bullet.move()
            if not bullet.active:
                self.player.bullets.remove(bullet)
            else:
                bullet_coords = self.canvas.bbox(bullet.bullet)
                for enemy in self.enemies[:]:
                    if enemy.alive:
                        enemy_coords = self.canvas.bbox(enemy.enemy)
                        if check_collision(bullet_coords, enemy_coords):
                            bullet.remove()
                            enemy.take_damage(10)
                            if not enemy.alive:
                                enemy.remove()
                                self.enemies.remove(enemy)
                                
        for enemy in self.enemies[:]:
            if enemy.alive:
                enemy.move_enemy()
                enemy.shoot()
                enemy.update_bullets()
                for enemy_bullet in enemy.bullets[:]:
                    enemy_bullet.move()
                    if not enemy_bullet.active:
                        enemy.bullets.remove(enemy_bullet)
                    else:
                        enemy_bullet_coords = self.canvas.bbox(enemy_bullet.bullet)
                        player_coords = self.canvas.bbox(self.player.player)
                        if check_collision(enemy_bullet_coords, player_coords):
                            enemy_bullet.remove()
                            self.player.current_health -= 10
                            self.player.update_health_bar()
                            if self.player.current_health <= 0:
                                self.player.alive = False
                                self.end_game()
                                
        self.check_victory()
        
        if self.player.alive:
            self.window.after(50, self.update_game)
    
    
    def check_victory(self):
        
        if not self.enemies:
            self.show_victory_message()
            
    def show_victory_message(self):
        
        self.canvas.create_text(self.ancho_fondo // 2, self.alto_fondo//2,
                                text = "¡ GOOD ENDIGN !",
                                font = ("Arial", 48),
                                fill="gold")
        self.player.alive = False
        
        
    def end_game(self):
        self.canvas.create_text(self.ancho_fondo // 2, self.alto_fondo//2,
                                text= "¡ GAME OVER !",
                                font=("Arial", 48),
                                fill="red")
        self.player.alive = False
    #@staticmethod
def check_collision(obj1, obj2):
    x1, y1, x2, y2 = obj1
    a1, b1, a2, b2 = obj2
    return not (x2 < a1 or x1 > a2 or y2 < b1 or y1 > b2)
        


if __name__ == "__main__":
    app = Main()
    app.window.mainloop()
