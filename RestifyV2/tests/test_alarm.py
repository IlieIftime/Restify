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

        # Lista de despertadores (inicialmente vazia)
        self.despertadores = []
        self.despertadores_inteligentes = []

        # Carregar definições dos ficheiros JSON
        self.load_config()

        # Exibir a lista de despertadores
        self.show_despertadores_list()

    def load_config(self):
        """Carrega as definições dos ficheiros config.json e despertador_inteligente.json."""
        # Carregar despertadores normais
        config_path = os.path.join("config", "config.json")
        try:
            if os.path.exists(config_path):
                with open(config_path, "r") as f:
                    data = json.load(f)
                    if "despertadores" in data:
                        self.despertadores = data["despertadores"]
                    else:
                        self.despertadores = []
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar configurações: {e}")

        # Carregar despertadores inteligentes
        inteligente_path = os.path.join("config", "despertador_inteligente.json")
        try:
            if os.path.exists(inteligente_path):
                with open(inteligente_path, "r") as f:
                    data = json.load(f)
                    if "despertadores_inteligentes" in data:
                        self.despertadores_inteligentes = data["despertadores_inteligentes"]
                    else:
                        self.despertadores_inteligentes = []
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar despertadores inteligentes: {e}")

    def show_despertadores_list(self):
        """Atualiza a interface garantindo que apenas os elementos corretos sejam exibidos."""
        # Limpar widgets, mas manter o fundo
        for widget in self.root.winfo_children():
            if widget != self.label_fundo:
                widget.destroy()

        # Título
        tk.Label(self.root, text="Lista de Despertadores Ativos", font=("Arial", 20), bg='lightgray', fg='black').place(
            relx=0.5, rely=0.1, anchor="center")

        if not self.despertadores and not self.despertadores_inteligentes:
            # Exibir mensagem se não houver alarmes
            tk.Label(self.root, text="Nenhum alarme adicionado.", font=("Arial", 14), bg='lightgray', fg='black').place(
                relx=0.5, rely=0.3, anchor="center")
        else:
            # Criar um frame para os despertadores
            frame_lista = tk.Frame(self.root, bg="white")
            frame_lista.place(relx=0.5, rely=0.5, anchor="center")

            # Exibir despertadores normais
            if self.despertadores:
                tk.Label(frame_lista, text="Alarmes Normais", font=("Arial", 16), bg='lightgray', fg='black').pack(pady=10)
                for despertador in self.despertadores:
                    self.create_despertador_row(frame_lista, despertador, "Normal")

            # Exibir despertadores inteligentes
            if self.despertadores_inteligentes:
                tk.Label(frame_lista, text="Alarmes Inteligentes", font=("Arial", 16), bg='lightgray', fg='black').pack(pady=10)
                for despertador in self.despertadores_inteligentes:
                    self.create_despertador_row(frame_lista, despertador, "Inteligente")

        # Botão Voltar
        btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 14), bg='white', fg="black",
                               padx=20, pady=10, bd=2, relief="raised", command=self.go_back)
        btn_voltar.place(relx=0.5, rely=0.9, anchor="center")

    def create_despertador_row(self, frame, despertador, tipo):
        """Cria uma linha na lista de despertadores."""
        linha = tk.Frame(frame, bg="white")
        linha.pack(fill="x", pady=5)

        # Nome e hora do despertador
        lbl_nome = tk.Label(linha, text=f"{despertador.get('nome', 'Sem nome')} - {despertador.get('hora', '??:??')} ({tipo})",
                            font=("Arial", 12), bg='white', fg='black')
        lbl_nome.pack(side="left", padx=10)

        # Botão Testar
        btn_testar = tk.Button(linha, text="Testar", command=lambda d=despertador, t=tipo: self.testar_alarme(d, t),
                               width=10, bg='blue', fg='white', font=("Arial", 10))
        btn_testar.pack(side="left", padx=5)

    def testar_alarme(self, despertador, tipo):
        """Testa um alarme (aciona motor ou reproduz áudio)."""
        try:
            if tipo == "Normal":
                # Enviar comando para acionar o motor vibratório
                command = f"MOTOR:{despertador.get('porta_motor', '1')}:ON"  # Substitua 'porta_motor' pelo campo correto
                self.send_command_to_pi(command)
                messagebox.showinfo("Teste Alarme Normal", f"Motor vibratório acionado!")
            elif tipo == "Inteligente":
                # Enviar comando para reproduzir áudio
                audio_file = despertador.get("audio_file")
                if audio_file:
                    command = f"AUDIO:{audio_file}"
                    self.send_command_to_pi(command)
                    messagebox.showinfo("Teste Alarme Inteligente", f"Reproduzindo áudio: {despertador['nome']}!")
                else:
                    messagebox.showwarning("Aviso", "Nenhum arquivo de áudio definido para este alarme.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao testar alarme: {e}")

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

    def go_back(self):
        """Fecha a tela atual e volta para a tela anterior."""
        self.root.destroy()
        from GUI.definicoes_screen import DefinicoesScreen
        definicoes_root = tk.Tk()
        DefinicoesScreen(definicoes_root)
        definicoes_root.mainloop()


# Exemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    app = Test_Alarm(root)
    root.mainloop()