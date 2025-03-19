import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import os
import pygame  # Para reproduzir áudio
import socket  # Para comunicação Wi-Fi

class Test_Alarm:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Despertadores - Restify")

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

        # Configurações de conexão com o Raspberry Pi
        self.HOST = '192.168.1.100'  # Substitua pelo IP do Raspberry Pi
        self.PORT = 65432

        # Exibir logo e lista de alarmes
        self.show_logo()
        self.show_alarms()

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

    def show_alarms(self):
        """Exibe a lista de alarmes com botões para testar."""
        try:
            # Verificar se a pasta config existe
            if not os.path.exists("config"):
                raise FileNotFoundError("Pasta 'config' não encontrada.")

            # Carregar alarmes normais
            if os.path.exists("config/config.json"):
                with open("config/config.json", "r") as f:
                    alarmes_normais = json.load(f)
                    if not isinstance(alarmes_normais, list):  # Verificar se é uma lista
                        raise ValueError("O arquivo config.json deve conter uma lista de alarmes.")
            else:
                raise FileNotFoundError("Arquivo 'config/config.json' não encontrado.")

            # Carregar alarmes inteligentes
            if os.path.exists("config/despertador_inteligente.json"):
                with open("config/despertador_inteligente.json", "r") as f:
                    alarmes_inteligentes = json.load(f)
                    if not isinstance(alarmes_inteligentes, list):  # Verificar se é uma lista
                        raise ValueError("O arquivo despertador_inteligente.json deve conter uma lista de alarmes.")
            else:
                raise FileNotFoundError("Arquivo 'config/despertador_inteligente.json' não encontrado.")

            # Exibir alarmes normais
            tk.Label(self.root, text="Alarmes Normais", font=("Arial", 16), bg='lightgray', fg='black').place(relx=0.3, rely=0.25, anchor="center")
            for i, alarme in enumerate(alarmes_normais):
                if not isinstance(alarme, dict) or "nome" not in alarme or "porta_motor" not in alarme:
                    raise ValueError("Formato inválido no arquivo config.json. Cada alarme deve ter 'nome' e 'porta_motor'.")
                tk.Label(self.root, text=alarme["nome"], font=("Arial", 12), bg='lightgray', fg='black').place(relx=0.3, rely=0.3 + i * 0.05, anchor="center")
                btn_testar = tk.Button(self.root, text="Testar", font=("Arial", 10), bg='white', fg='black',
                                       command=lambda a=alarme: self.testar_alarme_normal(a))
                btn_testar.place(relx=0.4, rely=0.3 + i * 0.05, anchor="center")

            # Exibir alarmes inteligentes
            tk.Label(self.root, text="Alarmes Inteligentes", font=("Arial", 16), bg='lightgray', fg='black').place(relx=0.7, rely=0.25, anchor="center")
            for i, alarme in enumerate(alarmes_inteligentes):
                if not isinstance(alarme, dict) or "nome" not in alarme or "caminho_audio" not in alarme:
                    raise ValueError("Formato inválido no arquivo despertador_inteligente.json. Cada alarme deve ter 'nome' e 'caminho_audio'.")
                tk.Label(self.root, text=alarme["nome"], font=("Arial", 12), bg='lightgray', fg='black').place(relx=0.7, rely=0.3 + i * 0.05, anchor="center")
                btn_testar = tk.Button(self.root, text="Testar", font=("Arial", 10), bg='white', fg='black',
                                       command=lambda a=alarme: self.testar_alarme_inteligente(a))
                btn_testar.place(relx=0.8, rely=0.3 + i * 0.05, anchor="center")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar alarmes: {e}")

    def send_command_to_pi(self, command):
        """Envia um comando para o Raspberry Pi via Wi-Fi."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.HOST, self.PORT))
                s.sendall(command.encode('utf-8'))
                data = s.recv(1024)
                print(f"Resposta do Raspberry Pi: {data.decode('utf-8')}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao enviar comando para o Raspberry Pi: {e}")

    def testar_alarme_normal(self, alarme):
        """Testa um alarme normal (aciona motor vibratório no Raspberry Pi)."""
        try:
            # Enviar comando para acionar o motor vibratório
            command = f"MOTOR:{alarme['porta_motor']}:ON"
            self.send_command_to_pi(command)
            messagebox.showinfo("Teste Alarme Normal", f"Motor vibratório acionado na porta {alarme['porta_motor']}!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao testar alarme normal: {e}")

    def testar_alarme_inteligente(self, alarme):
        """Testa um alarme inteligente (reproduz áudio no Raspberry Pi)."""
        try:
            # Enviar comando para reproduzir áudio
            command = f"AUDIO:{alarme['caminho_audio']}"
            self.send_command_to_pi(command)
            messagebox.showinfo("Teste Alarme Inteligente", f"Reproduzindo áudio: {alarme['nome']}!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao testar alarme inteligente: {e}")

    def go_back(self):
        """Redireciona para a tela anterior."""
        self.root.destroy()
        from GUI.teste_sensor_atuador import Test_Hardware
        root = tk.Tk()
        hardware_screen = Test_Hardware(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Test_Alarm(root)
    root.mainloop()