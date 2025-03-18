import tkinter as tk
from PIL import Image, ImageTk

class Test_Hardware: #checkpoint
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
        self.show_logo()
        btn_test_alarm = tk.Button(self.root, text="Teste alarme", font=("Arial", 14), bg='white', fg='black',
                                   padx=20, pady=10, bd=2, relief="raised", command=self.go_to_test_alarm) #botao redireciona test alarms
        btn_test_alarm.place(relx=0.5, rely=0.2, anchor="center", width=200, height=50)

        btn_test_conexion = tk.Button(self.root, text="Teste conexão", font=("Arial", 14), bg='white', fg='black',
                                       padx=20, pady=10, bd=2, relief="raised", command=self.go_to_test_conexion) #botao redireciona test conexion
        btn_test_conexion.place(relx=0.5, rely=0.29, anchor="center", width=200, height=50)

        btn_test_micro = tk.Button(self.root, text="Teste microfone", font=("Arial", 14), bg='white', fg='black',
                                       padx=20, pady=10, bd=2, relief="raised", command=self.go_to_test_micro) #botao redireciona test micro
        btn_test_micro.place(relx=0.5, rely=0.38, anchor="center", width=200, height=50)

        btn_test_servos = tk.Button(self.root, text="Teste servomotores", font=("Arial", 14), bg='white', fg='black',
                                       padx=20, pady=10, bd=2, relief="raised", command=self.go_to_test_servos) #botao redireciona test servos
        btn_test_servos.place(relx=0.5, rely=0.48, anchor="center", width=200, height=50)

        btn_test_speaker = tk.Button(self.root, text="Teste altifalantes", font=("Arial", 14), bg='white', fg='black',
                                       padx=20, pady=10, bd=2, relief="raised", command=self.go_to_test_speaker) #botao redireciona test speaker
        btn_test_speaker.place(relx=0.5, rely=0.58, anchor="center", width=200, height=50)

        btn_test_vib_motor = tk.Button(self.root, text="Teste motor vibratório", font=("Arial", 14), bg='white', fg='black',
                                       padx=20, pady=10, bd=2, relief="raised", command=self.go_to_test_vib_motor) #botao redireciona test vibraçao motor
        btn_test_vib_motor.place(relx=0.5, rely=0.68, anchor="center", width=200, height=50)

        btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 14), bg='white', fg='black',
                               padx=20, pady=10, bd=2, relief="raised", command=self.go_back) #botao redireciona para a pagina anterior
        btn_voltar.place(relx=0.5, rely=0.78, anchor="center", width=200, height=50)


    def go_to_test_alarm(self):
        """Redireciona para a tela de teste de alarme."""
        self.root.destroy()
        from tests.test_alarm import Test_Alarm
        test_alarm = tk.Tk()
        test_alarm_screen = Test_Alarm(test_alarm)
        test_alarm.mainloop()

    def go_to_test_conexion(self):
        """Redireciona para a tela de teste de conexão."""
        self.root.destroy()
        from tests.test_conexion import Test_conexao
        test_conexion_root = tk.Tk()
        test_conexion_screen = Test_conexao(test_conexion_root)
        test_conexion_root.mainloop()

    def go_to_test_micro(self):
        """Redireciona para a tela de teste de microfone"""
        self.root.destroy()
        from tests.test_micro import Test_Micro
        test_micro_root = tk.Tk()
        test_micro_screen = Test_Micro(test_micro_root)
        test_micro_root.mainloop()

    def go_to_test_servos(self):
        """Redireciona para a tela de teste de servos"""
        self.root.destroy()
        from tests.test_servomotor import Test_Servos
        test_servos_root = tk.Tk()
        test_servos_screen = Test_Servos(test_servos_root)
        test_servos_root.mainloop()

    def go_to_test_speaker(self):
        """Redireciona para a tela de teste de speaker"""
        self.root.destroy()
        from tests.test_speaker import Test_Speaker
        test_speaker_root = tk.Tk()
        test_speaker_screen = Test_Speaker(test_speaker_root)
        test_speaker_root.mainloop()

    def go_to_test_vib_motor(self):
        """Redireciona para a tela de teste de vibração motor"""
        self.root.destroy()
        from tests.test_vib_motor import Test_Vib_Motor
        test_vib_motor_root = tk.Tk()
        test_vib_motor_screen = Test_Vib_Motor(test_vib_motor_root)
        test_vib_motor_root.mainloop()

    def go_back(self):
        """Retorna ao menu de definições."""
        from GUI.definicoes_screen import DefinicoesScreen
        for widget in self.root.winfo_children():
            widget.destroy()
        DefinicoesScreen(self.root)

    def show_logo(self):
        """Exibe o logo centralizado no topo."""
        try:
            logo_path = "img/logo.png"
            logo_image = Image.open(logo_path).resize((200, 200), Image.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo_image)

            label_logo = tk.Label(self.root, image=self.logo_photo, bg='white', borderwidth=0, highlightthickness=0)
            label_logo.place(relx=0.5, rely=0.085, anchor="center")
        except Exception as e:
            print(f"Erro ao carregar logo: {e}")