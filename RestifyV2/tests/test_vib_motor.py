import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import socket  # Para comunicação Wi-Fi

class Test_Vib_Motor:
    def __init__(self, root):
        self.root = root
        self.root.title("Testar Motores Vibratórios - Restify")

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

        # Exibir logo e botões para testar os motores
        self.show_logo()
        self.show_test_buttons()

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

    def show_test_buttons(self):
        """Exibe os botões para testar os motores vibratórios."""
        # Botão para testar o motor 1
        btn_motor1 = tk.Button(self.root, text="Testar Motor 1", font=("Arial", 14), bg='white', fg='black',
                               padx=20, pady=10, bd=2, relief="raised", command=lambda: self.testar_motor("GPIO17"))
        btn_motor1.place(relx=0.4, rely=0.4, anchor="center", width=200, height=50)

        # Botão para testar o motor 2
        btn_motor2 = tk.Button(self.root, text="Testar Motor 2", font=("Arial", 14), bg='white', fg='black',
                               padx=20, pady=10, bd=2, relief="raised", command=lambda: self.testar_motor("GPIO18"))
        btn_motor2.place(relx=0.6, rely=0.4, anchor="center", width=200, height=50)

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

    def testar_motor(self, porta_motor):
        """Testa um motor vibratório enviando um comando ao Raspberry Pi."""
        try:
            # Enviar comando para ligar o motor
            command = f"MOTOR:{porta_motor}:ON"
            self.send_command_to_pi(command)
            messagebox.showinfo("Teste Motor", f"Motor {porta_motor} acionado!")

            # Desligar o motor após 2 segundos
            self.root.after(2000, lambda: self.send_command_to_pi(f"MOTOR:{porta_motor}:OFF"))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao testar motor: {e}")

    def go_back(self):
        """Redireciona para a tela anterior."""
        self.root.destroy()
        from GUI.teste_sensor_atuador import Test_Hardware
        root = tk.Tk()
        hardware_screen = Test_Hardware(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Test_Vib_Motor(root)
    root.mainloop()