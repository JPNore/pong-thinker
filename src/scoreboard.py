"""
Módulo que define la clase Scoreboard para el juego Pong.
"""

class Scoreboard:
    """
    Representa el marcador para llevar los puntos en el juego de Pong.
    """

    def __init__(self, canvas):
        """
        Inicializa el marcador en el lienzo.

        Args:
            canvas (tkinter.Canvas): El lienzo donde se dibuja el texto del marcador.
        """
        self.canvas = canvas
        
        # Crea el texto del marcador.
        # (Posición en X: 400 y en Y: 50 se pueden ajustar desde la lógica del juego)
        self.id = canvas.create_text(
            400, 50,
            text="0 - 0",
            font=("Courier", 40),
            fill="white"
        )

    def update(self, left_score, right_score):
        """
        Actualiza el texto del marcador con la puntuación proporcionada.

        Args:
            left_score (int): Puntuación del jugador de la izquierda.
            right_score (int): Puntuación del jugador de la derecha.
        """
        self.canvas.itemconfig(self.id, text=f"{left_score} - {right_score}")
