import tkinter as tk

from PIL import Image, ImageTk


class DefinicoesScreen:

    def __init__(self, root):
        self.root = root
        self.root.title("Menu - Restify")
        self.root.geometry("1200x1200")
        self.root.resizable(False, False)

        # Aplicar imagem de fundo
        self.set_background()

        # Exibir logo
        self.show_logo()

        # Criar botões do menu
        self.create_buttons()

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

    def create_buttons(self):
        """Cria os botões do menu principal."""
        btn_despertador = tk.Button(self.root, text="Despertador", font=("Arial", 14), bg='white', fg='black',
                                     padx=20, pady=10, bd=2, relief="raised", command=self.go_to_despertador)
        btn_despertador.place(relx=0.5, rely=0.2, anchor="center", width=200, height=50)

        btn_ajuste_almofada = tk.Button(self.root, text="Ajuste Almofada", font=("Arial", 14), bg='white', fg='black', padx=20,
                              pady=10, bd=2, relief="raised", command=self.go_to_ajuste_almofada)
        btn_ajuste_almofada.place(relx=0.5, rely=0.3, anchor="center", width=200, height=50)

        btn_conta = tk.Button(self.root, text="Conta", font=("Arial", 14), bg='white', fg='black',
                                      padx=20, pady=10, bd=2, relief="raised", command=self.go_to_conta)
        btn_conta.place(relx=0.5, rely=0.4, anchor="center", width=200, height=50)

        btn_add_medidas = tk.Button(self.root, text="Adicionar medidas", font=("Arial", 14), bg='white', fg='black',
                              padx=20, pady=10, bd=2, relief="raised", command=self.go_add_medidas)
        btn_add_medidas.place(relx=0.5, rely=0.5, anchor="center", width=200, height=50)

        btn_conectar_hardware = tk.Button(self.root, text="Conectar almofada", font=("Arial", 14), bg='white', fg='black',
                                    padx=20, pady=10, bd=2, relief="raised", command=self.go_to_conectar_h)
        btn_conectar_hardware.place(relx=0.5, rely=0.6, anchor="center", width=200, height=50)

        btn_test_hardware = tk.Button(self.root, text="Teste Hardware", font=("Arial", 14), bg='white', fg="black",
                               padx=20, pady=10, bd=2, relief="raised", command=self.go_to_test_hardware)
        btn_test_hardware.place(relx=0.5, rely=0.7, anchor="center", width=200, height=50)

        btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 14), bg='white', fg="black",
                                   padx=20, pady=10, bd=2, relief="raised", command=self.go_back)
        btn_voltar.place(relx=0.5, rely=0.8, anchor="center", width=200, height=50)

    def go_add_medidas(self):
        self.root.destroy()  # Close the definicoes screen
        from GUI.add_medidas_screen import add_medidas  # Import here to avoid circular imports
        medidas_root = tk.Tk()
        medidas_screen = add_medidas(medidas_root)
        medidas_root.mainloop()


    def go_to_despertador(self):
        self.root.destroy()  # Close the definicoes screen
        from GUI.despertador_lista_screen import DespertadorListaScreen # Import here to avoid circular imports
        despertador_lista_root = tk.Tk()
        despertador_lista_screen = DespertadorListaScreen(despertador_lista_root)
        despertador_lista_root.mainloop()


    def go_to_conectar_h(self):
        self.root.destroy()  # Close the definicoes screen
        from GUI.conexao_hardware import Conexao_Hardware # Import here to avoid circular imports
        hardware_root = tk.Tk()
        hardware_screen = Conexao_Hardware(hardware_root)
        hardware_root.mainloop()

    def go_to_ajuste_almofada(self):
        self.root.destroy()  # Close the definicoes screen
        from GUI.ajuste_almofada_screen import AjusteAlmofadaScreen  # Import here to avoid circular imports
        ajuste_almofada_root = tk.Tk()
        ajuste_almofada_screen = AjusteAlmofadaScreen(ajuste_almofada_root)
        ajuste_almofada_root.mainloop()

    def go_to_conta(self):
        self.root.destroy()  # Close the definicoes screen
        from GUI.user import User_menu  # Import here to avoid circular imports
        user_root = tk.Tk()
        user_screen = User_menu(user_root)
        user_root.mainloop()

    def go_to_test_hardware(self):
        self.root.destroy() #Vai para a tela de teste de hardware
        from GUI.teste_sensor_atuador import Test_Hardware
        test_hardware_root = tk.Tk()
        test_hardware_screen = Test_Hardware(test_hardware_root)
        test_hardware_root.mainloop()

    def go_back(self):
        self.root.destroy()  # Close the definicoes screen
        from GUI.menu_screen import MenuScreen  # Import here to avoid circular imports
        menu_root = tk.Tk()
        menu_screen = MenuScreen(menu_root)
        menu_root.mainloop()