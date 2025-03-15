import tkinter as tk
from PIL import Image, ImageTk
from GUI.audio_screen import AudioScreen
from GUI.definicoes_screen import DefinicoesScreen
from GUI.begin_menu import BeginMenu
from GUI.ultimo_ciclo_screen import Ultimo_ciclo
from GUI.ultima_semana_screen import Ultima_semana

class MenuScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu - Restify")
        self.root.geometry("1200x1200")
        self.root.resizable(False, False)

        # Aplicar imagem de fundo
        self.set_background()

        # Exibir logo
        self.show_logo()

        # Criar botões do menu
        self.create_buttons()

    def set_background(self):
        """Define a imagem de fundo."""
        try:
            img = Image.open("img/img.png").resize((1200, 1200), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(img)
            label_fundo = tk.Label(self.root, image=self.bg_photo)
            label_fundo.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Erro ao carregar imagem de fundo: {e}")

    def show_logo(self):
        """Exibe o logo centralizado no topo."""
        try:
            logo = Image.open("img/logo.png").resize((200, 200), Image.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo)
            label_logo = tk.Label(self.root, image=self.logo_photo, bg='white')
            label_logo.place(x=500, y=0)
        except Exception as e:
            print(f"Erro ao carregar logo: {e}")

    def create_buttons(self):
        """Cria os botões do menu principal."""
        btn_ultimo_ciclo = tk.Button(self.root, text="Último Ciclo", font=("Arial", 14), bg='white', fg='black', padx=20, pady=10, bd=2, relief="raised",command=self.go_to_ultimo_ciclo)
        btn_ultimo_ciclo.place(relx=0.5, rely=0.3, anchor="center", width=200, height=50)

        btn_audio = tk.Button(self.root, text="Áudios", font=("Arial", 14), bg='white', fg='black', padx=20, pady=10, bd=2, relief="raised", command=self.open_audio_screen)
        btn_audio.place(relx=0.5, rely=0.4, anchor="center", width=200, height=50)

        btn_ultima_semana = tk.Button(self.root, text="Última Semana", font=("Arial", 14), bg='white', fg='black', padx=20, pady=10, bd=2, relief="raised", command=self.go_to_ulima_semana)
        btn_ultima_semana.place(relx=0.5, rely=0.5, anchor="center", width=200, height=50)

        btn_definicoes = tk.Button(self.root, text="Definições", font=("Arial", 14), bg='white', fg="black", padx=20, pady=10, bd=2, relief="raised", command=self.go_to_definicoes)
        btn_definicoes.place(relx=0.5, rely=0.6, anchor="center", width=200, height=50)

        btn_sair = tk.Button(self.root, text="Sair", font=("Arial", 14), bg='red', fg='white', padx=20, pady=10, bd=2, relief="raised", command=self.go_to_begin_menu)
        btn_sair.place(relx=0.5, rely=0.7, anchor="center", width=200, height=50)

    def open_audio_screen(self):
        """Abre a tela de gerenciamento de áudio."""
        for widget in self.root.winfo_children():
            widget.destroy()
        AudioScreen(self.root)

    def go_to_definicoes(self):
        """Abre a tela de definições."""
        for widget in self.root.winfo_children():
            widget.destroy()
        DefinicoesScreen(self.root)

    def go_to_begin_menu(self):
        """Retorna para a tela inicial."""
        for widget in self.root.winfo_children():
            widget.destroy()
        BeginMenu(self.root)

    def go_to_ultimo_ciclo(self):
        """Retorna para a tela inicial."""
        for widget in self.root.winfo_children():
            widget.destroy()
        Ultimo_ciclo(self.root)

    def go_to_ulima_semana(self):
        """Retorna para a tela inicial."""
        for widget in self.root.winfo_children():
            widget.destroy()
        Ultima_semana(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    app = MenuScreen(root)
    root.mainloop()