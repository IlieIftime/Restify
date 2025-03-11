import json
import os
import tkinter as tk

import pygame  # Para reprodução de áudio
import ttkthemes  # Para temas aprimorados
from PIL import ImageTk

# Cores e dimensões da interface
BG_COLOR = "#ADD8E6"  # Cor de fundo azul claro
BTN_COLOR = "#7289da"  # Cor dos botões
HOVER_COLOR = "#5b6eae"  # Cor ao passar o mouse
LARGURA = 1200
ALTURA = 800
DATA_FILE = "config.json"  # Arquivo para persistência de dados
AUDIO_DIR = "audio_records"  # Diretório para armazenar áudios
fundo_ceu = "img.png"
img_tk = ImageTk.PhotoImage(fundo_ceu)
class SmartPillowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Pillow Interface")
        self.root.geometry(f"{LARGURA}x{ALTURA}")
        self.root.configure(bg=BG_COLOR)

        # Aplicar tema
        style = ttkthemes.ThemedStyle(self.root)
        style.set_theme("arc")  # Use um tema futurista

        # Frame principal onde os diferentes ecrãs serão exibidos
        self.main_frame = tk.Frame(self.root, bg=BG_COLOR)
        self.main_frame.pack(fill="both", expand=True)

        # Inicializando variáveis de usuário
        self.username = None
        self.alarm_time = None
        self.active_days = []
        self.height = None
        self.shoulder_width = None

        # Criar diretório de áudio se não existir
        if not os.path.exists(AUDIO_DIR):
            os.makedirs(AUDIO_DIR)

        # Carregar configurações se existirem
        self.load_config()

        # Inicializar Pygame
        pygame.mixer.init()

        # Mostrar tela de boas-vindas
        self.show_welcome_screen()

    def load_config(self):
        # Carregar configurações do arquivo JSON
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                data = json.load(file)
                self.username = data.get("username")
                self.alarm_time = data.get("alarm_time")
                self.active_days = data.get("active_days", [])
                self.height = data.get("height")
                self.shoulder_width = data.get("shoulder_width")

    def show_welcome_screen(self):

        label_fundo = tk.Label(self.root, image=img_tk)
        label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

        # Criar campos de entrada
        entry_login = tk.Entry(self.root, font=("Arial", 14), bd=2, relief="groove")
        entry_login.place(relx=0.5, rely=0.4, anchor="center", width=250, height=30)

        entry_password = tk.Entry(self.root, font=("Arial", 14), bd=2, relief="groove", show="*")
        entry_password.place(relx=0.5, rely=0.5, anchor="center", width=250, height=30)

        # Criar botão de registro
        btn_registro = tk.Label(self.root, text="Registro", font=("Arial", 12, "underline"), fg="blue", cursor="hand2")
        btn_registro.place(relx=0.5, rely=0.9, anchor="center")

        self.root.geometry(f"{LARGURA}x{ALTURA}")  # Definir tamanho da janela
        self.root.mainloop()