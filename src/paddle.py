"""
Módulo que define la clase Paddle para el juego Pong.
"""

class Paddle:
    """
    Representa una raqueta en el juego de Pong.
    """

    def __init__(self, canvas, color, lado):
        """
        Inicializa la raqueta.

        Args:
            canvas (tkinter.Canvas): El lienzo donde se dibuja la raqueta.
            color (str): El color de la raqueta.
            lado (str): Posición inicial de la raqueta, usualmente 'left' o 'right'.
        """
        self.canvas = canvas
        # Crea la raqueta como un rectángulo
        self.id = canvas.create_rectangle(0, 0, 15, 100, fill=color)
        
        self.lado = lado
        self.y_speed = 20 # Velocidad de movimiento vertical

    def move_up(self):
        """
        Mueve la raqueta hacia arriba en el lienzo.
        """
        self.canvas.move(self.id, 0, -self.y_speed)

    def move_down(self):
        """
        Mueve la raqueta hacia abajo en el lienzo.
        """
        self.canvas.move(self.id, 0, self.y_speed)
