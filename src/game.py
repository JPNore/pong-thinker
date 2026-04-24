"""
Módulo que contiene la clase Game, la cual orquesta la lógica principal del juego Pong.
"""

import tkinter as tk
from src.ball import Ball
from src.paddle import Paddle
from src.scoreboard import Scoreboard

class Game:
    """
    Clase principal que controla la ventana, los elementos y el ciclo de juego.
    """

    def __init__(self, root):
        """
        Inicializa el juego.
        
        Args:
            root (tkinter.Tk): La ventana principal de la aplicación.
        """
        self.root = root
        self.root.title("Pong")
        self.root.resizable(False, False)
        
        # Crear lienzo de 800x600 con fondo negro
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="black", bd=0, highlightthickness=0)
        self.canvas.pack()

        # Instanciar el marcador
        self.scoreboard = Scoreboard(self.canvas)
        
        # Instanciar las raquetas y posicionarlas
        self.paddle_left = Paddle(self.canvas, "white", "left")
        self.canvas.move(self.paddle_left.id, 30, 250)
        
        self.paddle_right = Paddle(self.canvas, "white", "right")
        self.canvas.move(self.paddle_right.id, 755, 250)

        # Instanciar la pelota
        self.ball = Ball(self.canvas, "white")

        # Variables de puntuación
        self.score_left = 0
        self.score_right = 0

        # Control de teclas presionadas
        self.keys_pressed = {}
        self.root.bind("<KeyPress>", self._on_key_press)
        self.root.bind("<KeyRelease>", self._on_key_release)

        # Iniciar el game loop
        self._update()

    def _on_key_press(self, event):
        """Registra cuando una tecla es presionada."""
        self.keys_pressed[event.keysym] = True

    def _on_key_release(self, event):
        """Registra cuando una tecla es soltada."""
        self.keys_pressed[event.keysym] = False

    def check_collisions(self):
        """Verifica colisiones con las paredes y raquetas, y detecta los puntos."""
        ball_coords = self.canvas.coords(self.ball.id)
        # ball_coords = [x1, y1, x2, y2]
        
        # Colisión superior e inferior (Rebote en el eje Y)
        if ball_coords[1] <= 0 or ball_coords[3] >= 600:
            self.ball.bounce_y()
            # Asegurar que no se quede atrapada en el borde
            if ball_coords[1] <= 0:
                self.canvas.move(self.ball.id, 0, -ball_coords[1] + 1)
            else:
                self.canvas.move(self.ball.id, 0, 600 - ball_coords[3] - 1)
            
        # Detección de puntos (Pared izquierda y derecha)
        if ball_coords[0] <= 0:
            # Punto para el jugador de la derecha
            self.score_right += 1
            self.scoreboard.update(self.score_left, self.score_right)
            self.ball.reset_ball()
        elif ball_coords[2] >= 800:
            # Punto para el jugador de la izquierda
            self.score_left += 1
            self.scoreboard.update(self.score_left, self.score_right)
            self.ball.reset_ball()

        # Colisión con las raquetas
        overlapping = self.canvas.find_overlapping(*ball_coords)
        if self.paddle_left.id in overlapping or self.paddle_right.id in overlapping:
            self.ball.bounce_x()
            
            # Separar la pelota de la raqueta para evitar rebotes múltiples
            if self.paddle_left.id in overlapping:
                # Mover hacia la derecha un poco para evitar atascos
                self.canvas.move(self.ball.id, 5, 0)
            elif self.paddle_right.id in overlapping:
                # Mover hacia la izquierda un poco
                self.canvas.move(self.ball.id, -5, 0)

    def _update(self):
        """Ciclo principal del juego, se llama cada ~16ms."""
        # --- Movimiento de Raquetas ---
        # Raqueta Izquierda (W / S)
        left_coords = self.canvas.coords(self.paddle_left.id)
        if self.keys_pressed.get("w") or self.keys_pressed.get("W"):
            if left_coords[1] > 0:
                self.paddle_left.move_up()
        if self.keys_pressed.get("s") or self.keys_pressed.get("S"):
            if left_coords[3] < 600:
                self.paddle_left.move_down()

        # Raqueta Derecha (Flechas Up / Down)
        right_coords = self.canvas.coords(self.paddle_right.id)
        if self.keys_pressed.get("Up"):
            if right_coords[1] > 0:
                self.paddle_right.move_up()
        if self.keys_pressed.get("Down"):
            if right_coords[3] < 600:
                self.paddle_right.move_down()

        # --- Movimiento de Pelota ---
        self.ball.move()

        # --- Detección de Colisiones ---
        self.check_collisions()

        # Repetir el loop ~60 fps (1000ms / 60 ~ 16ms)
        self.root.after(16, self._update)
