import tkinter as tk

from GUI.main_gui import MainGUI


class WelcomeScreen(MainGUI):
    def __init__(self):
        super().__init__()

        # Exibir logo no topo
        self.show_logo()

        # Criar título e botões de navegação
        tk.Label(self.main_frame, text="Bem-vindo ao Restify", font=("Arial", 24)).pack(pady=20)
        tk.Button(self.main_frame, text="Login", font=("Arial", 14), command=self.show_login).pack(pady=10)
        tk.Button(self.main_frame, text="Criar Conta", font=("Arial", 14), command=self.show_registration).pack(pady=10)

    def show_login(self):
        print("Ir para tela de login")  # Chamará a tela de login

    def show_registration(self):
        print("Ir para tela de registro")  # Chamará a tela de registro
