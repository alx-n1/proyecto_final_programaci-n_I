import pygame
import random


# Inicializa Pygame para el sonido
pygame.mixer.init()

# Función para cargar el sonido de clic
sonido_click = pygame.mixer.Sound("sonidos/select.wav")  # Define el sonido aquí

# Funciones de sonido
def reproducir_musica_inicio():
    """
    mediante pygame 
    reproduce de forma aleatoria un variedad de canciones, principalmente se usa para la pantalla de inicio
    
    """
    #mete en una lista las direcciones de las canciones
    posiblesCanciones = [
        "ost/kille queen.mp3",
        "ost/Vitality Remix - Saku Ram (youtube).mp3",
        "ost/DOS-88 – Race to Mars [Synthwave] 🎵 from Royalty Free Planet™ - RoyaltyFreePlanet (youtube).mp3",
        "ost/The Toxic Avenger.mp3"
    ]
    #de forma aleatoria se selecciona 1
    a = random.choice(posiblesCanciones)
    #se carga la cancion aleatoria
    pygame.mixer.music.load(a)
    #se procede a reproducir en bucle
    pygame.mixer.music.play(loops=-1)

def reproduci_cancion_nivel(ruta_del_temazoInsano:str):
    """funcion para reproducir la musica en los niveles de los juegos, solo necesita la ruta donde este almacenada la cancion
       de preferencia debe estar almacenada en una carpeta que este junto al archivo .py
       por ejemplo "ost/nombre.mp3" 

    Args:
        ruta_del_temazoInsano (str): ruta de su cancion 
    """
    #carga la cancion que esta en la ruta introducida
    pygame.mixer.music.load(ruta_del_temazoInsano)
    #reproduce en bucle la cancion seleccionada
    pygame.mixer.music.play(loops=-1)

def select():
    """
    funcion que reproduce un sonido de seleccion antes establecido
    """
    # Usa el sonido de clic definido globalmente
    sonido_click.play()  

def cerrando_musica():
    """funcion para hacer que la musica se detenga
    """
    pygame.mixer.music.stop()
    
def sonido_x(ruta_del_sonido:str):
    """
        reproducira el sonido de la ruta que le proporciones
    Args:
        ruta_del_sonido (str): ruta donde esta ubicado el sonido
    """
    sonido_x=pygame.mixer.Sound(ruta_del_sonido)
    sonido_x.play()
# Funciones para ajustar el volumen NO TOCAR!!!!!!!!!!!!!!
def ajustar_volumen_musica(volumen):
    pygame.mixer.music.set_volume(float(volumen))

def ajustar_volumen_sonido(volumen):
    sonido_click.set_volume(float(volumen))  # Ajusta el volumen del sonido de clic

