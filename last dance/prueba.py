"""
from Interfaz_Main import create_game_frame, Main  # Elimina restar_game y ocultar_nivel
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Importa PIL para redimensionar la imagen
from bdost import reproducir_musica_inicio, select, reproduci_cancion_nivel, ajustar_volumen_musica, ajustar_volumen_sonido, sonido_x
from FondoAnimado import agregar_fondo_animado
from botones import boton_salir, boton_inicio, boton_volver_titulo, boton_cerrar_menu, boton_configurar_sonidos, boton_selec_level
from botones import boton_selec_x_nivel, boton_confi_salir, boton_volver_titulo_selec_level

class ventana_principal(tk.Tk):
    def __init__(self):
        super().__init__()
        # Título de la ventana
        self.title("Do you know FcF")
        # Tamaño de la ventana
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")  
        self.state('zoomed')
        
        # Instanciar solo una vez el método Main de Interfaz_Main
        self.main_game = Main(self)
        
        # Bind para que al pulsar ESC se llame al método para mostrar el frame de opciones
        self.bind("<Escape>", self.mostrar_frame_opciones)
        # Inicializa los distintos frames
        self.crear_frame_principal()
        self.crea_frame_opciones()
        self.crear_frame_juego()
        self.crear_ventana_control_volumen()
        self.crear_frame_SelecLevel()

    def crear_frame_principal(self):
        # Crear el frame principal
        self.frame_principal = tk.Frame(self)
        
        # Fondo animado
        agregar_fondo_animado(self.frame_principal, "fondo/fndo.mp4")
        
        # Música de fondo
        reproducir_musica_inicio()
        
        # Botones
        boton_inicio(self.frame_principal, self.mostrar_juego, 10, 200)
        boton_selec_level(self.frame_principal, self.mostrar_frame_selecLevel, 10, 300)
        boton_salir(self.frame_principal, self.salir, 10, 400)
        
        self.frame_principal.pack(fill="both", expand=True)

    def volver_frame_principal(self):
        sonido_x("sonidos/Files_MenuSelect.ogg")
        self.frame_opciones.place_forget()
        self.frame_selec_level.pack_forget()
        self.frame_iniciar_juego.pack_forget()
        self.main_game.hide_frame()  # Usar el método de la instancia de Main
        self.frame_principal.pack(fill="both", expand=True)
        reproducir_musica_inicio()

    def crear_frame_juego(self):
        self.frame_iniciar_juego = tk.Frame(self)
        self.frame_iniciar_juego = self.main_game.main_frame  # Usar la instancia de Main
        create_game_frame(self.frame_iniciar_juego)
        self.frame_iniciar_juego.pack_forget()

    def mostrar_juego(self):
        reproduci_cancion_nivel("ost/REVOLVANIA THE WORLD REVOLVING x Megalovania Remix.mp3")
        select()
        self.main_game.restart_game()  # Llamar al método de la instancia de Main
        
        self.frame_principal.pack_forget()
        self.frame_iniciar_juego.pack(fill="both", expand=True)

    def crea_frame_opciones(self):
        self.frame_opciones = tk.Frame(self, height=30, width=30)
        self.fondo_para_opciones = tk.PhotoImage(file="botones/logo2.png")
        self.label_fondo_opciones = tk.Label(self.frame_opciones, image=self.fondo_para_opciones)
        self.label_fondo_opciones .place(x=0, y=0, relwidth=1, relheight=1)
        
        boton_cerrar_menu(self.frame_opciones, self.cerrar_frame_opciones)
        boton_configurar_sonidos(self.frame_opciones, self.mostrar_frame_cotrolAudio)
        boton_volver_titulo(self.frame_opciones, self.volver_frame_principal)
        boton_confi_salir(self.frame_opciones, self.salir)
        
        self.frame_opciones.place_forget()

    def cerrar_frame_opciones(self):
        select()
        self.frame_opciones.place_forget()

    def mostrar_frame_opciones(self, event=None):
        frame_ancho = 390
        frame_alto = 670

        ventana_ancho = self.winfo_width()
        ventana_alto = self.winfo_height()

        pos_x = (ventana_ancho - frame_ancho) // 2
        pos_y = (ventana_alto - frame_alto) // 2

        self.frame_opciones.place(x=pos_x, y=pos_y, width=frame_ancho, height=frame_alto)
        self.frame_opciones.lift()

    def salir(self):
        self.destroy()

    def crear_ventana_control_volumen(self):
        self.frame_ajustar_sonido = tk.Frame(self)

        imagen_fondo = Image.open("botones/logo2.png")
        imagen_fondo = imagen_fondo.resize((390, 670), Image.LANCZOS)
        self.fondo = ImageTk.PhotoImage(imagen_fondo)
        label_fondo = tk.Label(self.frame_ajustar_sonido, image=self.fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        slider_musica = ttk.Scale(self.frame_ajustar_sonido, from_=0, to=1, orient="horizontal", command=lambda val: ajustar_volumen_musica(float(val)))
        slider_musica.set(0.5)  
        slider_musica.place(x=50, y=400)

        label_musica = tk.Label(self.frame_ajustar_sonido, text="Volumen Música", bg='lightgrey')
        label_musica.place(x=50, y=370)

        slider_sonido = ttk.Scale(self.frame_ajustar_sonido, from_=0, to=1, orient="horizontal", command=lambda val: ajustar_volumen_sonido(float(val)))
        slider_sonido.set(0.5)  
        slider_sonido.place(x=50, y=500)

        label_sonido = tk.Label(self.frame_ajustar_sonido, text="Volumen Sonido", bg='lightgrey')
        label_sonido.place(x=50, y=470)

        boton_sonido = tk.Button(self.frame_ajustar_sonido, text="Probar Sonido de Clic", command=select)
        boton_sonido.place(x=250, y=490)

        boton_cerrar = tk.Button(self.frame_ajustar_sonido, text="Cerrar", command=self.cerrar_frame_ajust_SonidoMusic)
        boton_cerrar.place(x=250, y=550)

        self.frame_opciones.place_forget()

    def mostrar_frame_cotrolAudio(self):
        select()
        frame_ancho = 390
        frame_alto = 670

        ventana_ancho = self.winfo_width()
        ventana_alto = self.winfo_height()

        pos_x = (ventana_ancho - frame_ancho) // 2
        pos_y = (ventana_alto - frame_alto) // 2
        self.frame_ajustar_sonido.place(x=pos_x, y=pos_y, width=frame_ancho, height=frame_alto)
        self.frame_ajustar_sonido.lift()

    def cerrar_frame_ajust_SonidoMusic(self):
        select()
        self.frame_ajustar_sonido.place_forget()

    def crear_frame_SelecLevel(self):
        self.frame_selec_level = tk.Frame(self)
        self.fondo_selecLevel = tk.PhotoImage(file="fondo/fodno_selec_level.png")
        self.fondo_label_selec_leve = tk.Label(self.frame_selec_level, image=self.fondo_selecLevel)
        self.fondo_label_selec_leve.place(x=0, y=0, relheight=1, relwidth=1)
        
        boton_volver_titulo_selec_level(self.frame_selec_level, self.volver_frame_principal, 550, 50)
        
        boton_selec_x_nivel(self.frame_selec_level, self.volver_frame_principal, "botones/bt_nivel_1.png", 20, 200)
        boton_selec_x_nivel(self.frame_selec_level, self.volver_frame_principal, "botones/bt_nivel_2.png", 550, 200)
        boton_selec_x_nivel(self.frame_selec_level, self.volver_frame_principal, "botones/bt_nivel_3.png", 1150, 200)
        boton_selec_x_nivel(self.frame_selec_level, self.volver_frame_principal, "botones/bt_nivel_4.png", 20, 350)
        boton_selec_x_nivel(self.frame_selec_level, self.volver_frame_principal, "botones/bt_nivel_5.png", 550, 350)
        boton_selec_x_nivel(self.frame_selec_level, self.volver_frame_principal, "botones/bt_boss_1.png", 1150, 350)
        boton_selec_x_nivel(self.frame_selec_level, self.volver_frame_principal, "botones/bt_nivel_6.png", 20, 500)
        boton_selec_x_nivel(self.frame_selec_level, self.volver_frame_principal, "botones/bt_nivel_7.png", 550, 500)
        boton_selec_x_nivel(self.frame_selec_level, self.volver_frame_principal, "botones/bt_nivel_8.png", 1150, 500)
        boton_selec_x_nivel(self.frame_selec_level, self.volver_frame_principal, "botones/bt_nivel_9.png", 20, 650)
        boton_selec_x_nivel(self.frame_selec_level, self.volver_frame_principal, "botones/bt_nivel_10.png", 550, 650)
        boton_selec_x_nivel(self.frame_selec_level, self.volver_frame_principal, "botones/bt_boss_2.png", 1150, 650)

        self.frame_selec_level.pack_forget()

    def mostrar_frame_selecLevel(self):
        self.frame_principal.pack_forget()
        self.frame_opciones.place_forget()
        self.frame_selec_level.pack(fill="both", expand=True)

# Crea la instancia para que se inicie la ventana
princip = ventana_principal()
# Inicia la ventana hasta que el usuario presione el botón de salir que se le presenta mediante botones o que cierre con la X de la ventana
princip.mainloop()
"""
import tkinter as tk
from PIL import Image as PilImage, ImageTk as PilImageTk
from Player import Player
import random
from Enemies import Enemy
from Bullet import Bullet
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
        
        # Condicionales para las oleadas y la generacion del final boss
        self.final_boss = None
        
        self.counter_wave = 0
        self.enemies_for_wave = 36
        self.conditional_by_wave = True
        
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
        
        # Botón para pausar el juego
        self.pause_button = tk.Button(self.main_frame, text='Pausar', command=self.toggle_pause)
        self.pause_button.place(x=self.ancho_fondo // 2, y=10)
        
        # Botón de reinicio (inicialmente oculto)
        self.restart_button = tk.Button(self.main_frame, text="Reiniciar Juego", command=self.restart_game)
        #self.restart_button.place(x=self.ancho_fondo // 2, y=self.alto_fondo // 2 + 50)  # Posición del botón
        if self.player.alive == True:
            self.restart_button.pack_forget()  # Oculta el botón al inicio
        
        # Actualizar el juego
        self.update_game()

    def hide_frame(self):
        """Oculta el frame principal"""
        self.main_frame.pack_forget()

    def restart_game(self):
        """Reinicia el juego desde cero"""
        for enemy in self.enemies:
            enemy.remove()
        self.enemies.clear()
        self.player.current_health = 100  # Reiniciar la salud del jugador
        self.player.alive = True
        self.counter_wave = 0  # Reiniciar el contador de oleadas
        self.enemies_for_wave = 36  # Reiniciar el número de enemigos por oleada
        self.conditional_by_wave = True  # Reiniciar la condición de oleadas
        if not self.final_boss is None:
            self.final_boss.remove()
        
        if self.game_over_text_or_victory is not None:
            self.canvas.delete(self.game_over_text_or_victory)
            self.game_over_text_or_victory = None
        
        self.restart_button.pack_forget()  # Ocultar el botón de reinicio
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
        if self.conditional_by_wave:
            gif_paths = ["enemies/enemy_1.png", 
                        "enemies/enemy_2.png", 
                        "enemies/enemy_3.png"]
            y = 50
            for i in range(self.enemies_for_wave):
                x = (i % 12) * 100 + 60
                y = 50 + (i // 12) * 100

                gif_path = random.choice(gif_paths)
                enemy = Enemy(x, y, health= 20, speed=1, gif_path=gif_path, 
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
        
        if not self.enemies and self.final_boss is None and self.conditional_by_wave:
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
                                
        if self.final_boss and self.final_boss.alive:
            for bullet in self.player.bullets[:]:
                bullet.move()
                if not bullet.active:
                    self.player.bullets.remove(bullet)
                else:
                    bullet_coords = self.canvas.bbox(bullet.bullet)
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
        
        if self.final_boss and self.final_boss.alive:
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
            self.final_boss = Final_Boss(x=0, y=0, health=3000, speed=50,
                                        canvas=self.canvas, window=self.main_frame, 
                                        ancho_fondo=self.ancho_fondo, alto_fondo=self.alto_fondo)

    def check_victory(self):
        if self.final_boss and not self.final_boss.alive:
            self.show_victory_message()

    def show_victory_message(self):
        self.game_over_text_or_victory = self.canvas.create_text(self.ancho_fondo // 2, self.alto_fondo // 2, 
                                text="¡ VICTORY !", 
                                font=("Arial", 48), 
                                fill="gold")
        self.player.alive = False
        activate_victory_sound()
        if self.player.alive == False:
            self.restart_button.pack() 
        if self.player.alive == True:
            self.restart_button.pack_forget()# Mostrar el botón de reinicio

    def end_game(self):
        self.game_over_text_or_victory = self.canvas.create_text(self.ancho_fondo // 2, self.alto_fondo // 2, 
                                text="¡ GAME OVER !", 
                                font=("Arial", 48), 
                                fill="red")
        self.player.alive = False
        activate_game_over_sound()
        #self.restart_button.pack()
        if self.player.alive == False:
            self.restart_button.pack()
            self.restart_button.place(x=self.ancho_fondo // 2, y=self.alto_fondo // 2 + 50)# Mostrar el botón de reinicio
        if self.player.alive == True:
            self.restart_button.pack_forget()
def check_collision(obj1, obj2):
    x1, y1, x2, y2 = obj1
    a1, b1, a2, b2 = obj2
    return not (x2 < a1 or x1 > a2 or y2 < b1 or y1 > b2)

def create_game_frame(padre):
    app = Main(padre)
    return app.main_frame

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()