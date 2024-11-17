import tkinter as tk
from PIL import Image as PilImage, ImageTk as PilImageTk
from tkinter import NW
import time
from Bullet import Bullet
import random

class Enemy_stats:
    def __init__(self, x, y, health):
        self.move_for_horizontal_x = x
        self.move_for_vertical_y = y
        self.health_enemies = health
        self.alive = True

    def move(self, dx, dy):
        self.move_for_horizontal_x += dx
        self.move_for_vertical_y += dy

    def take_damage(self, amount):
        self.health_enemies -= amount
        if self.health_enemies <= 0:
            self.alive = False


class Enemy(Enemy_stats):
    def __init__(self, x, y, health, speed, gif_path, canvas, window):
        super().__init__(x, y, health)
        self.speed = speed
        self.canvas = canvas
        self.window = window
        self.frames = []
        self.load_gif(gif_path)
        self.current_frame = 0
        self.enemy = self.canvas.create_image(self.move_for_horizontal_x, self.move_for_vertical_y, image=self.frames[0], anchor=NW)
        self.bullets = []

        # Disparo
        self.last_shoot_time = time.time()
        self.shot_cooldown = random.randint(6, 10)  # En segundos

        # Imagen de la bala
        self.bullet_image = PilImage.open('disparo_enemy.png')
        self.bullet_resized_image = self.bullet_image.resize((35, 45), PilImage.LANCZOS)
        self.bullet_photo_image = PilImageTk.PhotoImage(self.bullet_resized_image)

        self.animate_gif()

    def load_gif(self, gif_path):
        gif = PilImage.open(gif_path)
        for frame in range(gif.n_frames):
            gif.seek(frame)
            frame_image = PilImageTk.PhotoImage(gif.copy().resize((90, 70), PilImage.LANCZOS))
            self.frames.append(frame_image)

    def animate_gif(self):
        if self.alive:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.canvas.itemconfig(self.enemy, image=self.frames[self.current_frame])
            self.window.after(100, self.animate_gif)

    def move_enemy(self):
        self.move(self.speed, 0)
        self.canvas.move(self.enemy, self.speed, 0)
        enemy_coords = self.canvas.bbox(self.enemy)
        if enemy_coords[0] <= 0 or enemy_coords[2] >= self.canvas.winfo_width():
            self.speed = -self.speed

    def shoot(self):
        current_time = time.time()
        if current_time - self.last_shoot_time >= self.shot_cooldown:
            x, y = self.canvas.coords(self.enemy)
            bullet = Bullet(self.canvas, x + 45, y + 70, self.bullet_photo_image, 10, 1, self.window)
            self.bullets.append(bullet)
            self.last_shoot_time = current_time

    def update_bullets(self):
        for bullet in self.bullets[:]:
            bullet.move()
            if not bullet.active:
                self.bullets.remove(bullet)

    def remove(self):
        self.canvas.delete(self.enemy)

