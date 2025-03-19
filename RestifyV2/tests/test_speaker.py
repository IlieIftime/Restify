import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame  # Para reproduzir áudio
import socket  # Para comunicação Wi-Fi (opcional)

class Test_Speaker:
    def __init__(self, root):
        self.root = root
        self.root.title("Testar Speaker - Restify")

        # Configuração da janela
        self.root.geometry("1200x1200")
        self.root.resizable(False, False)

        # Carregar e redimensionar a imagem de fundo
        img = Image.open("img/img.png")
        resized_image = img.resize((1200, 1200), Image.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(resized_image)

        # Criar um label para o fundo
        self.label_fundo = tk.Label(root, image=self.tk_image)
        self.label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

        # Inicializar pygame para reprodução de áudio
        pygame.mixer.init()

        # Configurações de conexão com o Raspberry Pi (opcional)
        self.HOST = '192.168.1.100'  # Substitua pelo IP do Raspberry Pi
        self.PORT = 65432

        # Exibir logo e botão para testar o speaker
        self.show_logo()
        self.show_test_button()

        # Botão Voltar
        btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 14), bg='white', fg='black',
                               padx=20, pady=10, bd=2, relief="raised", command=self.go_back)
        btn_voltar.place(relx=0.5, rely=0.8, anchor="center", width=200, height=50)

    def show_logo(self):
        """Exibe o logo centralizado no topo."""
        try:
            logo_path = "img/logo.png"
            logo_image = Image.open(logo_path).resize((200, 200), Image.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo_image)

            label_logo = tk.Label(self.root, image=self.logo_photo, bg='white', borderwidth=0, highlightthickness=0)
            label_logo.place(relx=0.5, rely=0.1, anchor="center")
        except Exception as e:
            print(f"Erro ao carregar logo: {e}")

    def show_test_button(self):
        """Exibe o botão para testar o speaker."""
        btn_testar = tk.Button(self.root, text="Testar Speaker", font=("Arial", 14), bg='white', fg='black',
                               padx=20, pady=10, bd=2, relief="raised", command=self.testar_speaker)
        btn_testar.place(relx=0.5, rely=0.5, anchor="center", width=200, height=50)

    def testar_speaker(self):
        """Testa o speaker reproduzindo um áudio."""
        try:
            # Caminho do áudio de teste
            caminho_audio = "sounds/teste.mp3"  # Substitua pelo caminho do seu arquivo de áudio

            # Reproduzir o áudio localmente (no PC)
            pygame.mixer.music.load(caminho_audio)
            pygame.mixer.music.play()
            messagebox.showinfo("Teste Speaker", "Reproduzindo áudio de teste!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao testar speaker: {e}")

    def send_command_to_pi(self, command):
        """Envia um comando para o Raspberry Pi via Wi-Fi (opcional)."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.HOST, self.PORT))
                s.sendall(command.encode('utf-8'))
                data = s.recv(1024)
                print(f"Resposta do Raspberry Pi: {data.decode('utf-8')}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao enviar comando para o Raspberry Pi: {e}")

    def testar_speaker_no_pi(self):
        """Testa o speaker no Raspberry Pi enviando um comando."""
        try:
            # Caminho do áudio de teste no Raspberry Pi
            caminho_audio = "/home/pi/sounds/teste.mp3"  # Substitua pelo caminho no Raspberry Pi

            # Enviar comando para reproduzir áudio
            command = f"AUDIO:{caminho_audio}"
            self.send_command_to_pi(command)
            messagebox.showinfo("Teste Speaker", "Comando enviado para reproduzir áudio no Raspberry Pi!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao testar speaker no Raspberry Pi: {e}")

    def go_back(self):
        """Redireciona para a tela anterior."""
        self.root.destroy()
        from GUI.teste_sensor_atuador import Test_Hardware
        root = tk.Tk()
        hardware_screen = Test_Hardware(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Test_Speaker(root)
    root.mainloop()