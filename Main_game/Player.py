import tkinter as tk
from PIL import Image as PilImage, ImageTk as PilImageTk
from tkinter import NW
import time
from Bullet import Bullet

class Player():
    def __init__(self, ancho_image, alto_image, canvas, window):
        #Dimensiones de interfaz principal y diversos metodos
        self.ancho_image = ancho_image
        self.alto_image = alto_image
        self.window = window
        self.canvas = canvas
        self.time_sleep_bullet = 1
        
        self.frames = []
        self.load_gif('Main_game/nave_insana.gif')
        self.ancho_player = self.frames[0].width()
        self.alto_player = self.frames[0].height()
        self.x_inicial = (self.ancho_image - self.ancho_player) // 2
        self.y_inicial = self.alto_image - self.alto_player - 80
        self.player = self.canvas.create_image(self.x_inicial, self.y_inicial, image = self.frames[0], anchor = 'nw')
        self.speed_x = 30
        self.last_shoot_time = 0
        self.shot_cooldown = 0.4
        
        self.canvas.pack()
        
        
        #Balas do jogador
        
        
        self.bullet_image = PilImage.open('Main_game/disparo2.png')
        self.bullet_resize_image = self.bullet_image.resize((20, 30), PilImage.LANCZOS)
        self.bullet_photo_image = PilImageTk.PhotoImage(self.bullet_resize_image)
        self.bullets = []
        
        #Barra de vida y vida del jugador
        self.max_health = 100
        self.current_health = 100
        self.health_bar = self.canvas.create_rectangle(20,20,220,40, fill ="red")
        self.health_text = self.canvas.create_text(120, 30, text = f"{self.current_health}/{self.max_health}", font = ("Arial"), fill = "white")
        self.alive = True
        
        #Controles del jugador
        if self.alive ==True:
            self.window.bind('<Left>', self.move_left)
            self.window.bind('a', self.move_left)
            self.window.bind('A', self.move_left)
            self.window.bind('<Right>', self.move_right)
            self.window.bind('d', self.move_right)
            self.window.bind('D', self.move_right)
            self.window.bind('<space>', self.shoot)
            
        if self.alive == False:
            self.window.unbind('<Left>', self.move_left)
            self.window.unbind('a', self.move_left)
            self.window.unbind('A', self.move_left)
            self.window.unbind('<Right>', self.move_right)
            self.window.unbind('d', self.move_right)
            self.window.unbind('D', self.move_right)
            self.window.unbind('<space>', self.shoot)
        #self.update_bullets()
        
        
    def load_gif(self, path):
        self.gif = PilImage.open(path)
        for frame in range(0, self.gif.n_frames):
            self.gif.seek(frame)
            frame_image = PilImageTk.PhotoImage(self.gif.copy().resize((int(self.ancho_image * 0.1), int(self.alto_image * 0.1)),PilImage.LANCZOS))
            self.frames.append(frame_image)
        
    
    def animate_gif(self, frame_index):
        self.canvas.itemconfig(self.player, image=self.frames[(frame_index + 1) % len(self.frames)])
        self.window.after(100, self.animate_gif, (frame_index + 1) % len(self.frames))
        
    def move_left(self, event):
        x,y = self.canvas.coords(self.player)
        if x - self.speed_x >= 0:
            self.canvas.move(self.player, - self.speed_x, 0)
        
        
    def move_right(self, event):
        x,y = self.canvas.coords(self.player)
        if x + self.ancho_player + self.speed_x <= self.ancho_image:
            self.canvas.move(self.player, self.speed_x, 0)

    def shoot(self, event):
        current_time = time.time()
        if current_time - self.last_shoot_time >= self.shot_cooldown:    
            x, y = self.canvas.coords(self.player)
            bullet = Bullet(self.canvas,(x+1.8) + self.ancho_player // 2.8, (y-33), self.bullet_photo_image, 20, -2, self.window )
            self.bullets.append(bullet)
            self.last_shoot_time = current_time
            

    def update_health_bar(self):
        self.canvas.coords(self.health_bar, 20, 20, 20 + 2 * self.current_health, 40)
        self.canvas.itemconfig(self.health_text, text=f"{self.current_health}/{self.max_health}")










"""
        
    def shoot(self, event):
        current_time = time.time()
        if current_time - self.last_shoot_time >= self.shot_cooldown:
            x, y = self.canvas.coords(self.player)
            bullet = self.canvas.create_image((x+1.8) + self.ancho_player // 2.8, (y-33), image=self.bullet_photo_image, anchor=NW)
            self.bullets.append(bullet)
            self.last_shoot_time = current_time

    def update_bullets(self):
        for bullet in self.bullets:
            self.canvas.move(bullet, 0, -20)
            bullet_coords = self.canvas.coords(bullet)
            if bullet_coords[1] <= 0:
                self.canvas.delete(bullet)
                self.bullets.remove(bullet)
        self.window.after(50, self.update_bullets)
"""