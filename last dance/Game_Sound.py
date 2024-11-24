import pygame

pygame.mixer.init()

shooting_sound = pygame.mixer.Sound('Soniditos/shot 1.wav')

death_player = pygame.mixer.Sound('Soniditos/Super-Mario-World-Game-Over.wav')

death_enemies = pygame.mixer.Sound('Soniditos/enemy-death.wav')

attack_FinalBoss_sound = pygame.mixer.Sound('Soniditos/explosion.wav')

victory_sound = pygame.mixer.Sound('Soniditos/efecto-de-sonido-victoria-final.wav')

shooting_sound.set_volume(0.25) 

def activate_gunshot_sound():
    shooting_sound.play()
    
def activate_game_over_sound():
    death_player.play()

def activite_death_enemies():
    death_enemies.play()

def attack_FinalBoss():
    attack_FinalBoss_sound.play()
    
def activate_victory_sound():
    victory_sound.play()