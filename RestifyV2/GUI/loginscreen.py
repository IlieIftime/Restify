import tkinter as tk
from tkinter import ttk

from GUI.main_gui import MainGUI


class LoginScreen(MainGUI):
    def __init__(self):
        super().__init__()

        # Exibir logo no topo
        self.show_logo()

        # Criar título e campos de login
        tk.Label(self.main_frame, text="Login", font=("Arial", 24)).pack(pady=20)
        tk.Label(self.main_frame, text="Nome de Utilizador:", font=("Arial", 12)).pack(pady=5)
        username_entry = ttk.Entry(self.main_frame, width=30)
        username_entry.pack(pady=5)

        tk.Button(self.main_frame, text="Entrar", font=("Arial", 14), command=self.login).pack(pady=20)

    def login(self):
        print("Lógica de login aqui")
