import tkinter as tk

from PIL import Image, ImageTk


import tkinter as tk

from PIL import Image, ImageTk


class User_menu:

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
        btn_editar_conta = tk.Button(self.root, text="Editar Conta", font=("Arial", 14), bg='white', fg='black',
                                     padx=20, pady=10, bd=2, relief="raised", command=self.go_to_editar_conta)
        btn_editar_conta.place(relx=0.5, rely=0.3, anchor="center", width=200, height=50)

        btn_apagar_conta = tk.Button(self.root, text="Ajuste Almofada", font=("Arial", 14), bg='white', fg='black', padx=20,
                              pady=10, bd=2, relief="raised", command=self.go_to_apagar_conta)
        btn_apagar_conta.place(relx=0.5, rely=0.4, anchor="center", width=200, height=50)
        btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 14), bg='white', fg="black",
                                   padx=20, pady=10, bd=2, relief="raised", command=self.go_back)
        btn_voltar.place(relx=0.5, rely=0.6, anchor="center", width=200, height=50)



    def go_to_editar_conta(self):
        self.root.destroy()  # Close the definicoes screen
        from GUI.editar_conta_screen import Editar_conta  # Import here to avoid circular imports
        editar_conta_root = tk.Tk()
        editar_conta_screen = Editar_conta(editar_conta_root)
        editar_conta_root.mainloop()

    def go_to_apagar_conta(self):
        self.root.destroy()  # Close the definicoes screen
        from GUI.apagar_conta_screen import Apagar_conta  # Import here to avoid circular imports
        apagar_conta_root = tk.Tk()
        ajuste_almofada_screen = Apagar_conta(apagar_conta_root)
        apagar_conta_root.mainloop()


    def go_back(self):
        self.root.destroy()  # Close the definicoes screen
        from GUI.definicoes_screen import DefinicoesScreen  # Import here to avoid circular imports
        definicoes_root = tk.Tk()
        definicoes_screen = DefinicoesScreen(definicoes_root)
        definicoes_root.mainloop()