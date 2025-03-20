import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import socket


class TestPressaoProximidade:
    def __init__(self, root):
        self.root = root
        self.root.title("Testar Sensores de Pressão e Proximidade - Restify")

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

        # Configurações de conexão com o Raspberry Pi
        self.HOST = '192.168.1.100'  # Substitua pelo IP do Raspberry Pi
        self.PORT = 65432

        # Exibir logo e botões para testar os sensores
        self.show_logo()
        self.show_test_buttons()
        self.show_status()

        # Botão Voltar
        btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 14), bg='white', fg='black',
                               padx=20, pady=10, bd=2, relief="raised", command=self.go_back)
        btn_voltar.place(relx=0.5, rely=0.9, anchor="center", width=200, height=50)

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
        """Exibe os botões para testar os sensores."""
        btn_testar_pressao = tk.Button(self.root, text="Testar Pressão", font=("Arial", 14), bg='white', fg='black',
                                       padx=20, pady=10, bd=2, relief="raised", command=self.testar_pressao)
        btn_testar_pressao.place(relx=0.3, rely=0.5, anchor="center", width=200, height=50)

        btn_testar_proximidade = tk.Button(self.root, text="Testar Proximidade", font=("Arial", 14), bg='white', fg='black',
                                          padx=20, pady=10, bd=2, relief="raised", command=self.testar_proximidade)
        btn_testar_proximidade.place(relx=0.7, rely=0.5, anchor="center", width=200, height=50)

    def show_status(self):
        """Exibe o status da detecção de cabeça."""
        # Frame para organizar o status
        status_frame = tk.Frame(self.root, bg='white')
        status_frame.place(relx=0.5, rely=0.7, anchor="center")

        # Label para exibir o texto de status
        self.status_text = tk.Label(status_frame, text="Status: Aguardando dados...", font=("Arial", 14), bg='white', fg='black')
        self.status_text.pack()

    def testar_pressao(self):
        """Testa o sensor de pressão."""
        try:
            # Enviar comando para testar o sensor de pressão
            command = "TESTAR_PRESSÃO"
            response = self.send_command_to_pi(command)
            if response == "CABECA_DETECTADA":
                self.status_text.config(text="Status: Cabeça detectada (Pressão)", fg="green")
            else:
                self.status_text.config(text="Status: Nenhuma cabeça detectada (Pressão)", fg="red")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao testar sensor de pressão: {e}")

    def testar_proximidade(self):
        """Testa o sensor de proximidade."""
        try:
            # Enviar comando para testar o sensor de proximidade
            command = "TESTAR_PROXIMIDADE"
            response = self.send_command_to_pi(command)
            if response == "CABECA_DETECTADA":
                self.status_text.config(text="Status: Cabeça detectada (Proximidade)", fg="green")
            else:
                self.status_text.config(text="Status: Nenhuma cabeça detectada (Proximidade)", fg="red")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao testar sensor de proximidade: {e}")

    def send_command_to_pi(self, command):
        """Envia um comando para o Raspberry Pi e retorna a resposta."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.HOST, self.PORT))
                s.sendall(command.encode('utf-8'))
                data = s.recv(1024)
                return data.decode('utf-8')
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao enviar comando para o Raspberry Pi: {e}")
            return None

    def go_back(self):
        """Redireciona para a tela anterior."""
        self.root.destroy()
        from GUI.teste_sensor_atuador import Test_Hardware
        root = tk.Tk()
        hardware_screen = Test_Hardware(root)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = TestPressaoProximidade(root)
    root.mainloop()