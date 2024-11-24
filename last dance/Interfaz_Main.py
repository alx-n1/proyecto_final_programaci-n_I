import tkinter as tk
from PIL import Image as PilImage, ImageTk as PilImageTk
from Player import Player
import random
from Enemies import Enemy
from Bullet import Bullet
from botones import boton_reiniciar
from Final_boss import Final_Boss
from Game_Sound import *
class Main:
    def __init__(self, parent):
        # Define el frame principal
        self.main_frame = parent
        
        # Configura el frame
        self.ancho_fondo = self.main_frame.winfo_screenwidth()
        self.alto_fondo = self.main_frame.winfo_screenheight()
        self.main_frame.config(width=self.ancho_fondo, height=self.alto_fondo)
        
        self.paused = True
        
        #Condicionales para las oleadas y la generacion del final boss
        self.final_boss = None
        
        self.counter_wave = 0
        self.enemies_for_wave = 48
        self.conditional_by_wave = True
        self.conditional_by_FinalBoss = True
        self.game_over_text_or_victory = None
        
        # Inicializar el juego
        self.frames = []
        self.current_frame = 0
        self.load_gif('gif_fondo.gif')
        
        self.canvas = tk.Canvas(self.main_frame, width=self.ancho_fondo, height=self.alto_fondo)
        self.canvas.pack()
        
        self.background_image = self.canvas.create_image(0, 0, image=self.frames[0], anchor='nw')
        self.animate_gif()
        
        # Inicializar el jugador y los enemigos
        self.player = Player(self.ancho_fondo, self.alto_fondo, self.canvas, self.main_frame)
        self.enemies = []
        
        #self.create_enemies()
        
        # Botón para reiniciar el juego
        #
        self.restart_button = tk.Button(self.main_frame, text="Reiniciar Juego", command=self.restart_game)
        self.restart_button.place(x = (self.ancho_fondo // 2) + 40, y = 10)
        
        
        self.pause_button = tk.Button(self.main_frame, text = 'Pausar', command= self.toggle_pause)
        self.pause_button.place(x = (self.ancho_fondo // 2) - 40, y = 10)
        
        
        # Actualizar el juego
        self.update_game()

    def hide_frame(self):
        """Oculta el frame principal"""
        self.main_frame.pack_forget()

    def restart_game(self):
        """Reinicia el juego desde cero"""
        #self.player.reset()
        for enemy in self.enemies:
            enemy.remove()
        self.enemies.clear()
        self.create_enemies()
        self.player.current_health = 100  
        self.player.update_health_bar()
        self.player.alive = True
        self.counter_wave = 0  
        self.enemies_for_wave = 48  
        self.conditional_by_wave = True
        self.final_boss = None
        if not self.final_boss is None:
            self.final_boss.remove()
        
        if self.game_over_text_or_victory is not None:
            self.canvas.delete(self.game_over_text_or_victory)
            self.game_over_text_or_victory = None
        
        self.update_game()
        
        

    def load_gif(self, gif_path):
        self.gif = PilImage.open(gif_path)
        for frame in range(0, self.gif.n_frames):
            self.gif.seek(frame)
            frame_image = PilImageTk.PhotoImage(self.gif.copy().resize((self.ancho_fondo, self.alto_fondo), PilImage.LANCZOS))
            self.frames.append(frame_image)

    def animate_gif(self):
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.canvas.itemconfig(self.background_image, image=self.frames[self.current_frame])
        self.main_frame.after(100, self.animate_gif)



    def create_enemies(self):
        if self.conditional_by_wave == True:
            gif_paths = ["enemies/enemy_1.png", 
                        "enemies/enemy_2.png", 
                        "enemies/enemy_3.png"]
            y = 50
            for i in range(self.enemies_for_wave):
                x = (i % 12) * 100 + 60
                y = 50 + (i // 12) * 100

                gif_path = random.choice(gif_paths)
                enemy = Enemy(x, y, health=20, speed=1, gif_path=gif_path, 
                            canvas=self.canvas, window=self.main_frame)
                self.enemies.append(enemy)

    def toggle_pause(self):
        
        self.paused = not self.paused
        if self.paused:
            self.pause_button.config(text="Reanudar")
        else:
            self.pause_button.config(text="Pausar")
            self.update_game()


    def update_game(self):
        if self.paused:
            return
        
        self.damege_player()
        self.damage_enemies_and_final_boss()
        
        if not self.enemies and self.final_boss is None and self.conditional_by_wave == True:
            self.counter_wave += 1
            
            if self.enemies_for_wave > 12:
                self.enemies_for_wave -= 12
            else:
                self.enemies_for_wave = 0
                
            if self.counter_wave < 3:
                self.create_enemies()
                if self.player.current_health < 100:
                    self.player.current_health += round(self.player.current_health * 0.30)
                    if self.player.current_health > 100:
                        self.player.current_health = 100
                    self.player.update_health_bar()
                
            if self.counter_wave == 3:
                self.conditional_by_wave = False
                
                self.create_FinalBoss()
        
        self.check_victory()

        if self.player.alive:
            self.main_frame.after(50, self.update_game)
    
    #Creamos un método para que el jugador pueda hacer daños a los enemigos y al final boss
    def damege_player(self):
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
                                activite_death_enemies()
                                self.enemies.remove(enemy)
                                
        if not self.final_boss is None and self.final_boss.alive ==True:
            for bullet in self.player.bullets[:]:
                bullet.move()
                if not bullet.active:
                    self.player.bullets.remove(bullet)
                else:
                    bullet_coords = self.canvas.bbox(bullet.bullet)
                    if self.final_boss.alive:
                        FinalBoss_coords = self.canvas.bbox(self.final_boss.FinalBoss)
                        if FinalBoss_coords is not None and check_collision(bullet_coords, FinalBoss_coords):
                            bullet.remove()
                            self.final_boss.take_damage(20)
                            if not self.final_boss.alive:
                                self.final_boss.remove()
                                activite_death_enemies()
    
    def damage_enemies_and_final_boss(self):
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
        
        if not self.final_boss is None:
            if self.final_boss.alive:
                self.final_boss.move_boss()
                self.final_boss.shoot()
                self.final_boss.update_attacks()
                for attack in self.final_boss.attacks[:]:
                    attack.move_attack()
                    if not attack.active:
                        self.final_boss.attacks.remove(attack)
                    else:
                        attack_coords = self.canvas.bbox(attack.attack)
                        player_coords = self.canvas.bbox(self.player.player)
                        if check_collision(attack_coords, player_coords):
                            attack.remove()
                            self.player.current_health -= attack.damage_for_attack
                            self.player.update_health_bar()
                            if self.player.current_health <= 0:
                                self.player.alive = False
                                self.end_game()
    
    def create_FinalBoss(self):
        if not self.enemies and self.final_boss is None:
            self.final_boss = Final_Boss(x = 0, y = 0, health = 3000, speed = 50,
                                        canvas = self.canvas, window = self.main_frame, 
                                        ancho_fondo = self.ancho_fondo, alto_fondo = self.alto_fondo)
    
    def check_victory(self):
        if self.final_boss is not None:
            if not self.final_boss.alive:
                self.show_victory_message()
                
            else:
                self.create_FinalBoss()

    def show_victory_message(self):
        self.game_over_text_or_victory = self.canvas.create_text(self.ancho_fondo // 2, self.alto_fondo // 2, 
                                text="¡ VICTORY !", 
                                font=("Arial", 48), 
                                fill="gold")
        self.player.alive = False
        activate_victory_sound()
        if self.player.alive == False:
            self.restart_button.pack()
        else:
            self.restart_button.pack_forget()
    def end_game(self):
        self.game_over_text_or_victory = self.canvas.create_text(self.ancho_fondo // 2, self.alto_fondo // 2, 
                                text="¡ GAME OVER !", 
                                font=("Arial", 48), 
                                fill="red")
        self.player.alive = False
        activate_game_over_sound()

def check_collision(obj1, obj2):
    x1, y1, x2, y2 = obj1
    a1, b1, a2, b2 = obj2
    return not (x2 < a1 or x1 > a2 or y2 < b1 or y1 > b2)


def create_game_frame(padre):
    app = Main(padre)
    return app.main_frame

def restar_game(padre):
    app = Main(padre)
    return app.restart_game()

def ocultar_nivel(padre):
    app = Main(padre)
    return app.hide_frame()

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()
