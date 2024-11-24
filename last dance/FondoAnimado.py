# archivo: fondo_animado.py
import tkinter as tk
from tkinter import Label
import cv2
from PIL import Image, ImageTk, ImageSequence

def agregar_fondo_animado(ventana, video_ubi:str, velocidad=2):
    """
        funcion para reproducir un video de fondo en la ventana de tkinder,
        primero revisa si hay frames que recibe, esto sirve para saber cuando acabo el video
        si el video acabo procede a iniciar de nuevo, porque esta funcion repeti el video en bucle
    Args:
        ventana (tk/frame):  ventana o frame donde se repducira el video
        video_ubi (str): ruta de hubicacion del video
        velocidad (int, optional): velocidad a la que quieres que se reproduzca el video
    """
    # Carga el video
    cap = cv2.VideoCapture(video_ubi)

    # Función para actualizar cada fotograma en el label
    def actualizar_fondo():
        #aqui se trata de capturar los frames
        ret, frame = cap.read()
        # Si la captura fue exitosa, la variable ret devolvera un valor True y el if mostrar el frame
        if ret:
            # Cambiar el color BGR de OpenCV a RGB para Pillow
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Obtiene el tamaño actual de la ventana
            width = ventana.winfo_width()
            height = ventana.winfo_height()
            
            # Redimensiona el fotograma al tamaño de la ventana
            frame = cv2.resize(frame, (width, height))
            
            # Convierte el fotograma a un objeto de imagen de Tkinter
            img = ImageTk.PhotoImage(Image.fromarray(frame))
            
            # Configura el label para actualizar el fondo
            fondo.config(image=img)
            # Guarda la referencia de la imagen
            fondo.image = img  
        # si ret devolvio False entra en esta parte donde el else actura:    
        else:
            # Si el video terminó, reinicia desde el primer fotograma
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        
        # Llama a la función de nuevo para el siguiente fotograma
        ventana.after(velocidad, actualizar_fondo)  # Ajusta el tiempo para la velocidad del video

    # Crea un label para mostrar el video
    fondo = Label(ventana)
    fondo.place(x=0, y=0, relwidth=1, relheight=1)

    # Llama a la función para empezar a actualizar el video en el fondo
    actualizar_fondo()

