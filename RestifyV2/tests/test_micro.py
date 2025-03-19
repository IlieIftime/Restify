import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sounddevice as sd  # Para gravar e reproduzir áudio
import soundfile as sf    # Para salvar e carregar arquivos de áudio
import os
from datetime import datetime

class Test_Micro:
    def __init__(self, root):
        self.root = root
        self.root.title("Testar Microfone e Speaker - Restify")

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

        # Configurações de áudio
        self.fs = 44100  # Taxa de amostragem (44.1 kHz)
        self.duration = 10  # Duração da gravação em segundos
        self.audio_folder = "audio_records"  # Pasta para salvar os áudios
        self.create_audio_folder()  # Cria a pasta se não existir

        # Exibir logo e botões para testar microfone e speaker
        self.show_logo()
        self.show_test_buttons()

        # Botão Voltar
        btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 14), bg='white', fg='black',
                               padx=20, pady=10, bd=2, relief="raised", command=self.go_back)
        btn_voltar.place(relx=0.5, rely=0.8, anchor="center", width=200, height=50)

    def create_audio_folder(self):
        """Cria a pasta 'audio_records' se ela não existir."""
        if not os.path.exists(self.audio_folder):
            os.makedirs(self.audio_folder)
            print(f"Pasta '{self.audio_folder}' criada.")

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

    def show_test_buttons(self):
        """Exibe os botões para testar microfone e speaker."""
        # Botão para gravar áudio
        btn_gravar = tk.Button(self.root, text="Gravar Áudio", font=("Arial", 14), bg='white', fg='black',
                               padx=20, pady=10, bd=2, relief="raised", command=self.gravar_audio)
        btn_gravar.place(relx=0.4, rely=0.4, anchor="center", width=200, height=50)

        # Botão para reproduzir áudio
        btn_reproduzir = tk.Button(self.root, text="Reproduzir Áudio", font=("Arial", 14), bg='white', fg='black',
                                   padx=20, pady=10, bd=2, relief="raised", command=self.reproduzir_audio)
        btn_reproduzir.place(relx=0.6, rely=0.4, anchor="center", width=200, height=50)

    def gravar_audio(self):
        """Grava áudio de 10 segundos usando o microfone."""
        try:
            messagebox.showinfo("Gravação", "Gravação iniciada. Fale no microfone.")
            print("Gravando áudio...")

            # Gravar áudio
            gravacao = sd.rec(int(self.duration * self.fs), samplerate=self.fs, channels=2, dtype='float32')
            sd.wait()  # Aguarda o fim da gravação

            # Gerar nome único para o arquivo de áudio
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(self.audio_folder, f"gravacao_{timestamp}.wav")

            # Salvar áudio em um arquivo
            sf.write(filename, gravacao, self.fs)
            print(f"Áudio salvo em {filename}")
            messagebox.showinfo("Gravação", f"Gravação concluída! Arquivo salvo em {filename}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gravar áudio: {e}")

    def reproduzir_audio(self):
        """Reproduz o último áudio gravado."""
        try:
            # Verificar se há arquivos de áudio na pasta
            arquivos = os.listdir(self.audio_folder)
            if not arquivos:
                messagebox.showwarning("Aviso", "Nenhum áudio gravado encontrado!")
                return

            # Encontrar o arquivo mais recente
            arquivos.sort(reverse=True)
            ultimo_arquivo = os.path.join(self.audio_folder, arquivos[0])

            print(f"Reproduzindo áudio: {ultimo_arquivo}")
            # Carregar áudio do arquivo
            dados, fs = sf.read(ultimo_arquivo, dtype='float32')

            # Reproduzir áudio
            sd.play(dados, fs)
            sd.wait()  # Aguarda o fim da reprodução
            print("Reprodução concluída!")
            messagebox.showinfo("Reprodução", f"Áudio reproduzido: {ultimo_arquivo}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao reproduzir áudio: {e}")

    def go_back(self):
        """Redireciona para a tela anterior."""
        self.root.destroy()
        from GUI.teste_sensor_atuador import Test_Hardware
        root = tk.Tk()
        hardware_screen = Test_Hardware(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Test_Micro(root)
    root.mainloop()


"""
def gravar_audio(self):
    #Grava áudio de 10 segundos usando o microfone do Raspberry Pi.
    try:
        messagebox.showinfo("Gravação", "Gravação iniciada. Fale no microfone.")
        print("Gravando áudio...")

        # Comando para gravar áudio no Raspberry Pi
        command = "GRAVAR_AUDIO"
        self.send_command_to_pi(command)
        messagebox.showinfo("Gravação", "Gravação concluída!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gravar áudio: {e}")

def reproduzir_audio(self):
    #Reproduz o áudio gravado no Raspberry Pi.
    try:
        print("Reproduzindo áudio...")
        # Comando para reproduzir áudio no Raspberry Pi
        command = "REPRODUZIR_AUDIO"
        self.send_command_to_pi(command)
        messagebox.showinfo("Reprodução", "Áudio reproduzido!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao reproduzir áudio: {e}")

def send_command_to_pi(self, command):
    #Envia um comando para o Raspberry Pi via Wi-Fi.
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            s.sendall(command.encode('utf-8'))
            data = s.recv(1024)
            print(f"Resposta do Raspberry Pi: {data.decode('utf-8')}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao enviar comando para o Raspberry Pi: {e}")
"""