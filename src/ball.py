"""
Módulo que define la clase Ball para el juego Pong.
"""

import random

class Ball:
    """
    Representa la pelota en el juego de Pong.
    """

    def __init__(self, canvas, color):
        """
        Inicializa la pelota.

        Args:
            canvas (tkinter.Canvas): El lienzo donde se dibuja la pelota.
            color (str): El color de la pelota.
        """
        self.canvas = canvas
        # Crea la pelota como un óvalo (círculo) en el lienzo
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        
        # Inicializa su posición al centro y le da una dirección aleatoria
        self.reset_ball()

    def reset_ball(self):
        """
        Reinicia la pelota al centro con dirección y velocidad aleatorias.
        """
        # Centrar la pelota (asumiendo ventana de 800x600 y tamaño de pelota 15x15)
        self.canvas.coords(self.id, 392.5, 292.5, 407.5, 307.5)
        
        # Velocidad reducida a la mitad (1.5) y dirección aleatoria (1 o -1) para x e y
        self.x = 1.5 * random.choice([1, -1])
        self.y = 1.5 * random.choice([1, -1])

    def move(self):
        """
        Mueve la pelota en el lienzo de acuerdo a su velocidad actual en x e y.
        """
        self.canvas.move(self.id, self.x, self.y)

    def bounce_x(self):
        """
        Invierte la dirección horizontal de la pelota (para rebotar en las raquetas).
        """
        self.x = -self.x

    def bounce_y(self):
        """
        Invierte la dirección vertical de la pelota (para rebotar en los bordes superior e inferior).
        """
        self.y = -self.y
