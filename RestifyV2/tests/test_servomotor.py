import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import socket  # Para comunicação Wi-Fi

class Test_Servos:
    def __init__(self, root):
        self.root = root
        self.root.title("Testar Servos - Restify")

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

        # Exibir logo e botões para testar os servos
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
        """Exibe os botões para testar os servos."""
        # Botão para subir
        btn_subir = tk.Button(self.root, text="Subir", font=("Arial", 14), bg='white', fg='black',
                              padx=20, pady=10, bd=2, relief="raised", command=self.subir_servo)
        btn_subir.place(relx=0.4, rely=0.4, anchor="center", width=200, height=50)

        # Botão para descer
        btn_descer = tk.Button(self.root, text="Descer", font=("Arial", 14), bg='white', fg='black',
                               padx=20, pady=10, bd=2, relief="raised", command=self.descer_servo)
        btn_descer.place(relx=0.6, rely=0.4, anchor="center", width=200, height=50)

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

    def subir_servo(self):
        """Envia comando para subir o servo."""
        try:
            command = "SERVO:UP"
            self.send_command_to_pi(command)
            messagebox.showinfo("Teste Servo", "Comando para subir enviado!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao enviar comando para subir: {e}")

    def descer_servo(self):
        """Envia comando para descer o servo."""
        try:
            command = "SERVO:DOWN"
            self.send_command_to_pi(command)
            messagebox.showinfo("Teste Servo", "Comando para descer enviado!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao enviar comando para descer: {e}")

    def go_back(self):
        """Redireciona para a tela anterior."""
        self.root.destroy()
        from GUI.teste_sensor_atuador import Test_Hardware
        root = tk.Tk()
        hardware_screen = Test_Hardware(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Test_Servos(root)
    root.mainloop()