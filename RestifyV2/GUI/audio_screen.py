import tkinter as tk
from tkinter import filedialog, Listbox
from PIL import Image, ImageTk
import pygame
import os


class AudioScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciar Áudio - Restify")
        self.root.geometry("1200x1200")
        self.root.resizable(False, False)

        # Inicializar mixer do pygame para reprodução de áudio
        pygame.mixer.init()

        # Aplicar imagem de fundo
        self.set_background()

        # Exibir logo
        self.show_logo()

        # Criar interface
        self.create_interface()

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

    def create_interface(self):
        """Cria os botões e lista de áudios."""
        btn_upload = tk.Button(self.root, text="Carregar Áudio", font=("Arial", 14), bg='white', fg='black', padx=20, pady=10, bd=2, relief="raised", command=self.upload_audio)
        btn_upload.place(relx=0.5, rely=0.3, anchor="center", width=200, height=50)

        self.listbox = Listbox(self.root, font=("Arial", 14), width=40, height=10)
        self.listbox.place(relx=0.5, rely=0.5, anchor="center")

        btn_play = tk.Button(self.root, text="Reproduzir Áudio", font=("Arial", 14), bg='white', fg='black', padx=20, pady=10, bd=2, relief="raised", command=self.play_audio)
        btn_play.place(relx=0.5, rely=0.7, anchor="center", width=200, height=50)

        btn_back = tk.Button(self.root, text="Voltar", font=("Arial", 14), bg='white', fg='black', padx=20, pady=10, bd=2, relief="raised", command=self.go_back)
        btn_back.place(relx=0.5, rely=0.8, anchor="center", width=200, height=50)

        self.load_audio_list()

    def upload_audio(self):
        """Permite selecionar um arquivo de áudio e armazená-lo na pasta."""
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
        if file_path:
            file_name = os.path.basename(file_path)
            dest_path = os.path.join("audio_records", file_name)
            os.rename(file_path, dest_path)
            self.load_audio_list()

    def load_audio_list(self):
        """Carrega a lista de arquivos de áudio disponíveis."""
        self.listbox.delete(0, tk.END)
        if not os.path.exists("audio_records"):
            os.makedirs("audio_records")

        for file in os.listdir("audio_records"):
            if file.endswith(".mp3") or file.endswith(".wav"):
                self.listbox.insert(tk.END, file)

    def play_audio(self):
        """Reproduz o áudio selecionado na lista."""
        selected_audio = self.listbox.get(tk.ACTIVE)
        if selected_audio:
            audio_path = os.path.join("audio_records", selected_audio)
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()

    def go_back(self):
        """Retorna ao menu inicial."""
        from GUI.menu_screen import MenuScreen
        for widget in self.root.winfo_children():
            widget.destroy()
        MenuScreen(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    app = AudioScreen(root)
    root.mainloop()
