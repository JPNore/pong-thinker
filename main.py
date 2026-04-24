"""
Punto de entrada principal para el juego Pong.
"""

import tkinter as tk
from src.game import Game

def main():
    """
    Inicializa la ventana principal de tkinter y arranca el juego.
    """
    root = tk.Tk()
    app = Game(root)
    root.mainloop()

if __name__ == "__main__":
    main()
