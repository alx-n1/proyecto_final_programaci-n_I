from Enemies import Enemy_stats
import tkinter as tk
from PIL import Image as PilImage, ImageTk as PilImageTk
from tkinter import NW
import time
from Attack_Boss import Attack_Boss
import random
from Game_Sound import *

class Final_Boss(Enemy_stats):
    def __init__(self, x, y, health, speed, canvas, window, ancho_fondo, alto_fondo):
        super().__init__(x, y, health)
        self.speed = speed
        self.canvas = canvas
        self.window = window
        
        self.ancho_fondo = ancho_fondo
        self.alto_fondo = alto_fondo
        
        
        #Creacion de la imagen del final boss
        self.image_final_boss = PilImage.open('final_boss.png')
        self.image_final_boss_resize = self.image_final_boss.resize((400, 250), PilImage.LANCZOS)
        self.FinalBoss_Photo_Image = PilImageTk.PhotoImage(self.image_final_boss_resize)
        
        self.x_inicial = (self.ancho_fondo - 400) // 2
        self.y_inicial = (self.alto_fondo - 250) // 4
        self.FinalBoss = self.canvas.create_image(self.x_inicial, self.y_inicial, image=self.FinalBoss_Photo_Image)
        
        
        #Crear shoot down del ataque
        self.last_shoot_time = time.time()
        self.shoot_cooldown = random.randint(4, 6)
        self.attacks = []
        self.attack_type = 1 #Para alternar entre ataques
        
        
    def move_boss(self):
        self.canvas.move(self.FinalBoss, self.speed, 0)
        boss_coords = self.canvas.bbox(self.FinalBoss)
        if boss_coords[0] <= 0 or boss_coords[2] >= self.canvas.winfo_width():
            self.speed = -self.speed
            
    def shoot(self):
        current_time = time.time()
        if current_time - self.last_shoot_time >= self.shoot_cooldown:
            x, y = self.canvas.coords(self.FinalBoss)
            if self.attack_type == 1:
                attack = Attack_Boss(self.canvas, (x + 430) // 2, y, 25, 1, self.window, attack_type = 1)
            else:
                attack = Attack_Boss(self.canvas, (x + 430) // 2, y, 25, 1, self.window, attack_type = 2)
                
            self.attacks.append(attack)
            attack_FinalBoss()
            self.last_shoot_time = current_time
            self.attack_type = 2 if self.attack_type == 1 else 1 #Alternar entre ataques
                
    def update_attacks(self):
        for attack in self.attacks[:]:
            attack.move_attack()
            if not attack.active:
                self.attacks.remove(attack)
            
    def remove(self):
        self.canvas.delete(self.FinalBoss)