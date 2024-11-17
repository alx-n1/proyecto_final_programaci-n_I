import tkinter as tk
import pygame

#TODAS ESTAS FUNCIONES SON PARA GENERAR BOTONES, CADA UNA GENERA UN BOTON EN CONCRETO Y TIENE 1 IMAGEN ASIGNADA PARA CADA UNO!
#HAY ALGUNOS QUE PARECEN QUE SON LO MISMO PERO REALMENTE VAN HUBICADOS EN FRAME DISTINTOS Y POR ESO ALGUNOS TIENEN POSICION 
#Y OTROS TIENEN UNA POSICION CENTRADA
from PIL import Image, ImageTk

def redimensionar_imagen(ruta, ancho, alto):
    """
    Redimensiona la imagen de acuerdo al tamaño especificado.
    """
    imagen = Image.open(ruta)
    imagen = imagen.resize((ancho, alto), Image.Resampling.LANCZOS)  # Usar LANCZOS en lugar de ANTIALIAS
    return ImageTk.PhotoImage(imagen)


def boton_inicio(ventana,funcion,x,y):
    
    imagen_inicio = tk.PhotoImage(file="botones/inicio.png")
    imagen_inicio = imagen_inicio.subsample(1, 1)
    btonInicio = tk.Button(ventana, image=imagen_inicio,command=funcion, borderwidth=0)
    btonInicio.image = imagen_inicio  
    btonInicio.place(x=x,y=y)

def boton_salir(ventana, funcion, x, y):
    imagen_salir = tk.PhotoImage(file="botones/salir.png")
    imagen_salir = imagen_salir.subsample(1, 1)
    botonSalir = tk.Button(ventana, image=imagen_salir, command=funcion, borderwidth=0)
    botonSalir.image = imagen_salir  
    botonSalir.place(x=x, y=y)
    
    
def boton_reiniciar(ventana,funcion):
    imagen_cargar = tk.PhotoImage(file="botones/cargar.png")
    imagen_cargar = imagen_cargar.subsample(1, 1)
    botonReiniciar = tk.Button(ventana, image=imagen_cargar, command=funcion, borderwidth=0)
    botonReiniciar.image = imagen_cargar
    botonReiniciar.place(x=50, y=50)

def boton_cerrar_menu(ventana,funcion):
    imagen_cerrar_menu=tk.PhotoImage(file="botones/cerrar_menu.png")
    imagen_cerrar_menu=imagen_cerrar_menu.subsample(1,1)
    boton_cerrar_menu=tk.Button(ventana,image=imagen_cerrar_menu,command=funcion,border=0)
    boton_cerrar_menu.image=imagen_cerrar_menu
    boton_cerrar_menu.pack(expand=True)
    
def boton_volver_titulo(ventan,funcion):
    imagen_volver_titulo= tk.PhotoImage(file="botones/volver_titulo.png")
    imagen_volver_titulo=imagen_volver_titulo.subsample(1,1)
    botonVolverTitulo=tk.Button(ventan,image=imagen_volver_titulo, command=funcion, border=0)
    botonVolverTitulo.image= imagen_volver_titulo
    #como este quiero que sea un boton para el menu de opciones hago que aprezca centrado con el expand=true
    botonVolverTitulo.pack(expand=True)
    
def boton_configurar_sonidos(ventana,funcion):
    imagen_configurar_sonido=tk.PhotoImage(file="botones/config.png")
    imagen_configurar_sonido=imagen_configurar_sonido.subsample(1,1)
    boton_configurar_sonidos=tk.Button(ventana,image=imagen_configurar_sonido,command=funcion,border=0)
    boton_configurar_sonidos.image=imagen_configurar_sonido
    boton_configurar_sonidos.pack(expand=True)
    
def boton_selec_level(ventana,funcion,x,y):
    imagene_selec_elevel=tk.PhotoImage(file="botones/selec_level.png")
    imagene_selec_elevel=imagene_selec_elevel.subsample(1,1)
    boton_selecLevel=tk.Button(ventana,image=imagene_selec_elevel,command=funcion,border=0)
    boton_selecLevel.image=imagene_selec_elevel
    boton_selecLevel.place(x=x,y=y)
    
    
def boton_selec_x_nivel(ventana, funcion, ruta_de_la_imagen,x,y):
    imagen_x_nivel=tk.PhotoImage(file=ruta_de_la_imagen)
    imagen_x_nivel=imagen_x_nivel.subsample(1,1)
    boton_x_nivel=tk.Button(ventana,image=imagen_x_nivel,command=funcion)
    boton_x_nivel.image=imagen_x_nivel
    boton_x_nivel.place(x=x,y=y)
    
def boton_confi_salir(ventana, funcion):
    imagen_salir = tk.PhotoImage(file="botones/salir.png")
    imagen_salir = imagen_salir.subsample(1, 1)
    botonSalir = tk.Button(ventana, image=imagen_salir, command=funcion, borderwidth=0)
    botonSalir.image = imagen_salir  
    botonSalir.pack(expand=True)
    
def boton_volver_titulo_selec_level(ventan,funcion,x,y):
    imagen_volver_titulo= tk.PhotoImage(file="botones/volver_titulo.png")
    imagen_volver_titulo=imagen_volver_titulo.subsample(1,1)
    botonVolverTitulo=tk.Button(ventan,image=imagen_volver_titulo, command=funcion, border=0)
    botonVolverTitulo.image= imagen_volver_titulo
    #como este quiero que sea un boton para el menu de opciones hago que aprezca centrado con el expand=true
    botonVolverTitulo.place(x=x,y=y)
    
def boton_reiniciar(ventana, funcion):
    imagen_reiniciar_juego=tk.PhotoImage(file="botones/reintentar.png")
    imagen_reiniciar_juego=imagen_reiniciar_juego.subsample(1,1)
    boton_reiniciar_juego=tk.Button(ventana,image=imagen_reiniciar_juego,command=funcion,border=0)
    boton_reiniciar_juego.image=imagen_reiniciar_juego
    boton_reiniciar_juego.pack(expand=True)