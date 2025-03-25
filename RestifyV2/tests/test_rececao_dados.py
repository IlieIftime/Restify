import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import threading
import socket


class TestRececaoDados:
    def __init__(self, root):
        self.root = root
        self.root.title("Rececao de Dados - Restify")
        self.root.geometry("1200x1200")
        self.root.resizable(False, False)

        # Configuracoes de conexao
        self.HOST = '192.168.137.138'  # Substitua pelo IP do Raspberry Pi
        self.PORT = 65433  # Porta para comunicacao
        self.socket = None
        self.conexao_status = "Desconectado"

        # Iniciar interface
        self.set_background()
        self.show_logo()
        self.create_buttons()
        self.create_status_area()

        # Iniciar thread para receber dados
        self.iniciar_rececao_dados()

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
            label_logo.place(x=500, y=20)
        except Exception as e:
            print(f"Erro ao carregar logo: {e}")

    def create_buttons(self):
        """Cria os botoes para receber dados e voltar."""
        btn_receber_audio = tk.Button(self.root, text="Receber Audio", font=("Arial", 14), bg='white', fg='black',
                                      padx=20, pady=10, bd=2, relief="raised", command=self.receber_audio)
        btn_receber_audio.place(relx=0.5, rely=0.4, anchor="center", width=200, height=50)

        btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 14), bg='white', fg='black',
                               padx=20, pady=10, bd=2, relief="raised", command=self.go_back)
        btn_voltar.place(relx=0.5, rely=0.5, anchor="center", width=200, height=50)

    def create_status_area(self):
        """Cria a area para exibir o status de conexao."""
        self.status_frame = tk.Frame(self.root, bg='lightgray', bd=2, relief="groove")
        self.status_frame.place(relx=0.5, rely=0.6, anchor="center", width=400, height=100)

        self.status_label = tk.Label(self.status_frame, text="Status: Desconectado", font=("Arial", 12), bg='lightgray',
                                     fg='black')
        self.status_label.pack(pady=10)

    def iniciar_rececao_dados(self):
        """Inicia a thread para receber dados do Raspberry Pi."""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.HOST, self.PORT))
            self.conexao_status = "Conectado"
            self.atualizar_status()

            thread_receber = threading.Thread(target=self.receber_dados)
            thread_receber.daemon = True
            thread_receber.start()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao conectar ao Raspberry Pi: {e}")

    def receber_dados(self):
        """Recebe dados do Raspberry Pi."""
        while True:
            try:
                dados = self.socket.recv(1024)
                if dados:
                    if dados.startswith(b"TEXT_START"):
                        self.receber_arquivo_texto()
                    elif dados.startswith(b"AUDIO_START"):
                        self.receber_arquivo_audio()
                    else:
                        print(f"Dados recebidos: {dados.decode('utf-8')}")
                else:
                    break
            except Exception as e:
                print(f"Erro ao receber dados: {e}")
                break

    def receber_arquivo_texto(self):
        """Recebe um arquivo de texto do Raspberry Pi."""
        try:
            with open("texto_recebido.txt", "wb") as arquivo:
                while True:
                    dados = self.socket.recv(1024)
                    if dados.endswith(b"TEXT_END"):
                        arquivo.write(dados[:-9])  # Remove o marcador de fim
                        break
                    arquivo.write(dados)
            print("Texto recebido e salvo como 'texto_recebido.txt'.")
            messagebox.showinfo("Sucesso", "Texto recebido com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao receber texto: {e}")

    def receber_arquivo_audio(self):
        """Recebe um arquivo de audio do Raspberry Pi."""
        try:
            with open("audio_recebido.wav", "wb") as arquivo:
                while True:
                    dados = self.socket.recv(1024)
                    if dados.endswith(b"AUDIO_END"):
                        arquivo.write(dados[:-9])  # Remove o marcador de fim
                        break
                    arquivo.write(dados)
            print("Audio recebido e salvo como 'audio_recebido.wav'.")
            messagebox.showinfo("Sucesso", "Audio recebido com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao receber audio: {e}")

    def receber_audio(self):
        """Permite ao usuario escolher onde salvar o audio recebido."""
        caminho_arquivo = filedialog.asksaveasfilename(
            title="Salvar audio recebido",
            defaultextension=".wav",
            filetypes=(("Arquivos de audio", "*.wav"), ("Todos os arquivos", "*.*")))

        if caminho_arquivo:
            try:
                with open("audio_recebido.wav", "rb") as arquivo_origem:
                    with open(caminho_arquivo, "wb") as arquivo_destino:
                        arquivo_destino.write(arquivo_origem.read())
                messagebox.showinfo("Sucesso", f"Audio salvo em {caminho_arquivo}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar audio: {e}")

    def atualizar_status(self):
        """Atualiza o label de status."""
        self.status_label.config(text=f"Status: {self.conexao_status}")

    def go_back(self):
        """Redireciona para a tela anterior."""
        self.root.destroy()
        from GUI.teste_sensor_atuador import Test_Hardware
        root = tk.Tk()
        hardware_screen = Test_Hardware(root)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = TestRececaoDados(root)
    root.mainloop()