import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Importa PIL para redimensionar la imagen
from bdost import reproducir_musica_inicio, select, reproduci_cancion_nivel,ajustar_volumen_musica,ajustar_volumen_sonido,sonido_x
from FondoAnimado import agregar_fondo_animado
from botones import boton_salir, boton_inicio, boton_volver_titulo,boton_cerrar_menu,boton_configurar_sonidos,boton_selec_level
from botones import boton_selec_x_nivel,boton_confi_salir,boton_volver_titulo_selec_level

class ventana_principal(tk.Tk):
    def __init__(self):
        super().__init__()
        #titulo ¿provicional? de la ventana
        self.title("Do you know FcF")
        #se le da una forma a la ventana conforme al tamaño del monitor/pantalla de nuestro dispositivo
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")  
        #hace que inicialice en ventana completa
        self.state('zoomed')
        
        #self.bind hace que se bindee ESC para que al pulsarlo se llame el metodo para mostrar el frame opciones
        #junto con su variedad de opciones
        self.bind("<Escape>", lambda event: self.mostrar_frame_opciones())
        #se inicializa los distintos frames que tenemos
        self.crear_frame_principal()
        self.crea_frame_opciones()
        self.crear_frame_juego()
        self.crear_ventana_control_volumen()
        self.crear_frame_SelecLevel()

        
    def crear_frame_principal(self):
        
        """
        este frame es la ventana principal del juego, es la ventana donde se inicia el juego
        se le presentan varias opciones al usuario por medio de botones con imagenes
        """
        # Crear el frame principal dentro de la ventana principal del self
        self.frame_principal = tk.Frame(self)
        
        # Fondo animado
        agregar_fondo_animado(self.frame_principal, "fondo/fndo.mp4")
        
        # Música de fondo
        reproducir_musica_inicio()
        
        # Botón de inicio con imagen por medio de una función
        boton_inicio(self.frame_principal, self.mostrar_juego, 10, 200)
        #boton selec_level
        boton_selec_level(self.frame_principal,self.mostrar_frame_selecLevel,10,300)
        #boton para cerrar la ventana principal (con esto se cierra todos los frames)
        boton_salir(self.frame_principal, self.salir, 10, 400)
        
        self.frame_principal.pack(fill="both", expand=True)
        
    def volver_frame_principal(self):
        """
        metodo que ayuda a volver al frame principal, este metodo hace que los otros frames se eliminen de la vista del usuario
        de forma temporal hasta que vuelvan a ser llamados con sus respectivos metodos
        
        """
        #funcion que genera un sonido mediante pygame.sounds solo con agregar una ruta donde este un archivo de sonido
        sonido_x("sonidos/Files_MenuSelect.ogg")
        reproducir_musica_inicio()
        self.frame_opciones.place_forget()
        self.frame_selec_level.pack_forget()
        self.frame_iniciar_juego.pack_forget()
        self.frame_principal.pack(fill="both", expand=True)
        
    def crear_frame_juego(self):
        """
        aca debería estar el frame donde se empiece a reproducir un nivel del juego
        """
        self.frame_iniciar_juego = tk.Frame(self, bg="yellow")
        # Ocultar el frame del juego al inicio
        self.frame_iniciar_juego.pack_forget()
        
    def mostrar_juego(self):
        """
        este metodo muestra el frame donde debería estar el juego
        aca se le puede añadir musica con ayuda de una funcion llamada reproducir_cancion_nivel()
        
        """
        #sonido que se reproducira al hacer sonar el juego
        select()
        #cancion que se reproducira después de que se llame el frame mostrar juego
        reproduci_cancion_nivel("ost/REVOLVANIA THE WORLD REVOLVING x Megalovania Remix.mp3")
        #esto hace que el frame principal desaparezca de la visión
        self.frame_principal.pack_forget()
        #esto hace que el frame donde debe estar el juego aparezca
        self.frame_iniciar_juego.pack(fill="both", expand=True)
        
    def crea_frame_opciones(self):
        """
        frame para crear la ventana que le presentara una variedad de opciones al usuario, las cuales se pueden llamar con la tecla ESC
        dentro de este frame hay botones que se generan con una funcion la cual hace que tenga una imagen de fondo
        """
        # Crear el frame de opciones y su contenido (inicialmente oculto)
        self.frame_opciones = tk.Frame(self, height=30, width=30)
        #se le asigna una imagen de fondo
        self.fondo_para_opciones = tk.PhotoImage(file="botones/logo2.png")
        # Crear un label para contener la imagen de fondo
        self.label_fondo_opciones = tk.Label(self.frame_opciones, image=self.fondo_para_opciones)
        #se ajusta el label del fondo
        self.label_fondo_opciones.place(x=0, y=0, relwidth=1, relheight=1)
        
        #volver
        boton_cerrar_menu(self.frame_opciones,self.cerrar_frame_opciones)
        #configurar volumens
        boton_configurar_sonidos(self.frame_opciones,self.mostrar_frame_cotrolAudio)
        # Botón para volver al frame principal
        boton_volver_titulo(self.frame_opciones, self.volver_frame_principal)
        #boton para cerrar toda la ventana junto con todos su frames
        boton_confi_salir(self.frame_opciones, self.salir)
        
        # Ocultar el frame de opciones al inicio
        self.frame_opciones.place_forget()
        
    def cerrar_frame_opciones(self):
        """
        metodo que sirve para quitar temporalmente de la vista el frame de las opciones y su contenido
        tambien tiene un sonido que indica que el metodo fue usado
        """
        #funcion que reproduce un sonido
        select()
        #nos sirve para quitar el frame de la vista del usuaruario hasta que llame la funcion para mostrar el frame_opciones
        self.frame_opciones.place_forget()

    def mostrar_frame_opciones(self):
        
        """
        metodo para mostrar el frame de las opciones, con una posición y un tamño especifico
        """
        
        # Dimensiones del frame de opciones
        frame_ancho = 390
        frame_alto = 670

        # Obtener las dimensiones de la ventana principal
        ventana_ancho = self.winfo_width()
        ventana_alto = self.winfo_height()

        # Calcular la posición para centrar el frame
        pos_x = (ventana_ancho - frame_ancho) // 2
        pos_y = (ventana_alto - frame_alto) // 2

        # Colocar el frame en el centro
        self.frame_opciones.place(x=pos_x, y=pos_y, width=frame_ancho, height=frame_alto)
        self.frame_opciones.lift()  # Elevar el frame de opciones al frente
        
    def salir(self):
        """
        funcion para cerrar toda la ventana principal donde se estan ejecutando todos los frames
        """
        self.destroy()
    
    def crear_ventana_control_volumen(self):
        
        """
        Frame para ajustar el sonido y la musica del juego, tambien se le añade un fondo por medio el lavel, este frame estara hubicado
        en las opciones que se abren con ESC, posee sliders para que sea más simple al usuario gestionar el tema sonido
        """
        self.frame_ajustar_sonido = tk.Frame(self)
        

        
        imagen_fondo = Image.open("botones/logo2.png")
        imagen_fondo = imagen_fondo.resize((390, 670), Image.LANCZOS)
        self.fondo = ImageTk.PhotoImage(imagen_fondo)
        label_fondo = tk.Label(self.frame_ajustar_sonido, image=self.fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        # Crear controles deslizantes para el volumen de música y sonido
        slider_musica= ttk.Scale(self.frame_ajustar_sonido, from_=0, to=1, orient="horizontal", command=lambda val: ajustar_volumen_musica(float(val)))
        # Volumen inicial al 50%
        slider_musica.set(0.5)  
        slider_musica.place(x=50, y=400)

        label_musica= tk.Label(self.frame_ajustar_sonido, text="Volumen Música", bg='lightgrey')
        label_musica.place(x=50, y=370)
        
        #creando slider para sonidos
        
        slider_sonido= ttk.Scale(self.frame_ajustar_sonido, from_=0, to=1, orient="horizontal", command=lambda val: ajustar_volumen_sonido(float(val)))
        # Volumen inicial al 50%
        slider_sonido.set(0.5)  
        slider_sonido.place(x=50, y=500)

        label_sonido = tk.Label(self.frame_ajustar_sonido, text="Volumen Sonido", bg='lightgrey')
        label_sonido.place(x=50, y=470)

        # Botón para probar el sonido de clic
        boton_sonido = tk.Button(self.frame_ajustar_sonido, text="Probar Sonido de Clic", command=select)
        boton_sonido.place(x=250, y=490)

        # Botón para cerrar la ventana y detener la música
        boton_cerrar = tk.Button(self.frame_ajustar_sonido, text="Cerrar", command=self.cerrar_frame_ajust_SonidoMusic)
        boton_cerrar.place(x=250, y=550)

        #!!!
        self.frame_opciones.place_forget()

    def mostrar_frame_cotrolAudio(self):
        
        """
        metodo para ajustar el como se mostrara el frame de controlar audio y la posición en que se hubicara
        """
            # Dimensiones del frame de opciones
        select()
        frame_ancho = 390
        frame_alto = 670

        # Obtener las dimensiones de la ventana principal
        ventana_ancho = self.winfo_width()
        ventana_alto = self.winfo_height()

        # Calcular la posición para centrar el frame
        pos_x = (ventana_ancho - frame_ancho) // 2
        pos_y = (ventana_alto - frame_alto) // 2
        #configuramos el frame de ajuste de sonido
        self.frame_ajustar_sonido.place(x=pos_x, y=pos_y, width=frame_ancho, height=frame_alto)
        
        #lift es un metodo que trae un witget delante de todos los demas wifgets
        self.frame_ajustar_sonido.lift()
    
    def cerrar_frame_ajust_SonidoMusic(self):
        """
        funcion para cerrar el frame de ajustar sonido
        """
        #funcion que reproduce un sonido, especificamente el de "seleccion"
        select()
        #quita el frame de ajuste de sonido de la vista del usuario hasta que el usuario lo vuelva a llamar
        self.frame_ajustar_sonido.place_forget()
        
    def crear_frame_SelecLevel(self):
        """Método que crea el frame para seleccionar nivel, se le da un fondo
        y se le añaden todos los botones para que el player elija lo que quiera.
        """
        self.frame_selec_level = tk.Frame(self)
        
        # Fondo del frame de selección de nivel
        self.fondo_selecLevel = tk.PhotoImage(file="fondo/fodno_selec_level.png")
        self.fondo_label_selec_leve = tk.Label(self.frame_selec_level, image=self.fondo_selecLevel)
        self.fondo_label_selec_leve.place(x=0, y=0, relheight=1, relwidth=1)
        
        # Botón para volver al título
        boton_volver_titulo_selec_level(self.frame_selec_level, self.volver_frame_principal, 550, 50)
        
        # Crear una lista de botones con sus imágenes y posiciones
        self.botones_nivel = [
            {"imagen": "botones/bt_nivel_1.png", "x": 20, "y": 200},
            {"imagen": "botones/bt_nivel_2.png", "x": 550, "y": 200},
            {"imagen": "botones/bt_nivel_3.png", "x": 1150, "y": 200},
            {"imagen": "botones/bt_nivel_4.png", "x": 20, "y": 350},
            {"imagen": "botones/bt_nivel_5.png", "x": 550, "y": 350},
            {"imagen": "botones/bt_boss_1.png", "x": 1150, "y": 350},
            {"imagen": "botones/bt_nivel_6.png", "x": 20, "y": 500},
            {"imagen": "botones/bt_nivel_7.png", "x": 550, "y": 500},
            {"imagen": "botones/bt_nivel_8.png", "x": 1150, "y": 500},
            {"imagen": "botones/bt_nivel_9.png", "x": 20, "y": 650},
            {"imagen": "botones/bt_nivel_10.png", "x": 550, "y": 650},
            {"imagen": "botones/bt_boss_2.png", "x": 1150, "y": 650},
        ]
        
        # Crear los botones en base a la lista de posiciones
        self.botones_widgets = []
        for boton in self.botones_nivel:
            widget = boton_selec_x_nivel(self.frame_selec_level, self.volver_frame_principal, boton["imagen"], boton["x"], boton["y"])
            self.botones_widgets.append(widget)
        
        # Evento para redimensionar botones al cambiar tamaño de ventana
        self.frame_selec_level.bind("<Configure>", self.ajustar_posicion_botones)
        
        # Ocultar el frame de selección de nivel al inicio
        self.frame_selec_level.pack_forget()

    def ajustar_posicion_botones(self, event):
        """Ajusta la posición de los botones para que se mantengan dentro de la ventana."""
        ancho_ventana = self.frame_selec_level.winfo_width()
        alto_ventana = self.frame_selec_level.winfo_height()
        
    # Limitar las posiciones de los botones dentro de la ventana
        for i, boton in enumerate(self.botones_nivel):
            # Limitar posición en X e Y según el tamaño de la ventana
            pos_x = min(boton["x"], ancho_ventana - 100)  # 100 es un valor aproximado del ancho del botón
            pos_y = min(boton["y"], alto_ventana - 50)   # 50 es un valor aproximado de la altura del botón
            
            # Actualizar posición del widget
            self.botones_widgets[i].place(x=pos_x, y=pos_y)

        
        
    def mostrar_frame_selecLevel(self):
        """
        muestra el frame de seleccion de niveles junto con su contenido
        """
        #quita de la vista el frame del menu principal y el de opciones
        self.frame_principal.pack_forget()
        self.frame_opciones.place_forget()
        #muestra el frame de de seleccion de niveles
        #con fill both hacemos que el frame se expanda de forma verticual y horizontalmente, el expand true hace que se llene la ventana horizontal y verticalmente
        self.frame_selec_level.pack(fill="both",expand=True)
        

        
        
             
#crea la instancia para que se inicie la ventana
princip = ventana_principal()
#inicia la ventana hasta que el usuario precione el boton de salir que se le presenta mediante botones o que cierre con la x de la ventana
princip.mainloop()
