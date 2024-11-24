import tkinter as tk
from PIL import Image as PilImage, ImageTk as PilImageTk
from tkinter import NW
import time
import random
class Attack_Boss:
    def __init__(self, canvas, x, y, speed, direction, window, attack_type):
        self.canvas = canvas
        
        # Cargar imágenes de ataque
        self.attack_image1 = PilImage.open('Projectile_final_boss.png')
        self.attack_image1_resize = self.attack_image1.resize((90, 130), PilImage.LANCZOS)
        self.attack_photo_image1 = PilImageTk.PhotoImage(self.attack_image1_resize)
        
        self.attack_image2 = PilImage.open('second_attack_final_boss.png')
        self.attack_image2_resize = self.attack_image2.resize((80, 70), PilImage.LANCZOS)
        self.attack_photo_image2 = PilImageTk.PhotoImage(self.attack_image2_resize)
        
        self.damage_for_attack = 0
        self.speed = speed
        self.direction = direction
        self.window = window
        
        # Seleccionar imagen ```python
        # Seleccionar imagen según el tipo de ataque
        if attack_type == 1:
            self.attack = self.canvas.create_image(x, y, image=self.attack_photo_image1, anchor='nw')
            self.damage_for_attack = 40
        else:
            self.attack = self.canvas.create_image(x, y-random.randint(-180,180), image=self.attack_photo_image2, anchor='nw')
            self.damage_for_attack = 25
        
        self.active = True

    def move_attack(self):
        if self.active:
            self.canvas.move(self.attack, 0, self.speed * self.direction)
            coords = self.canvas.coords(self.attack)
            if coords[1] < 0 or coords[1] > self.canvas.winfo_height():
                self.remove()

    def remove(self):
        self.canvas.delete(self.attack)
        self.active = False