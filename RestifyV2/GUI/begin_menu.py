import tkinter as tk
from PIL import Image, ImageTk
from GUI.register_screen import RegisterScreen
from GUI.login_screen import LoginScreen


class BeginMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Restify - Menu Inicial")
        self.root.geometry("1200x1200")  # Definir tamanho fixo da janela
        self.root.resizable(False, False)  # Impedir redimensionamento

        # Aplicar imagem de fundo
        self.set_background()

        # Exibir logo
        self.show_logo()

        # Criar botões
        btn_register = tk.Button(self.root, text="Criar Conta", font=("Arial", 14), bg='white', fg='black', padx=20,
                                 pady=10, bd=2, relief="raised", command=self.go_to_register)
        btn_login = tk.Button(self.root, text="Login", font=("Arial", 14), bg='white', fg='black', padx=20,
                                 pady=10, bd=2, relief="raised", command=self.go_to_login)

        btn_register.place(relx=0.4, rely=0.4, anchor="center", width=200, height=50)
        btn_login.place(relx=0.6, rely=0.4, anchor="center", width=200, height=50)
    def set_background(self):
        """Define a imagem de fundo para a tela inicial."""
        try:
            img_path = "img/img.png"
            bg_image = Image.open(img_path).resize((1200, 1200), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(bg_image)

            label_fundo = tk.Label(self.root, image=self.bg_photo, borderwidth=0, highlightthickness=0)
            label_fundo.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Erro ao carregar imagem de fundo: {e}")

    def show_logo(self):
        """Exibe o logo centralizado no topo."""
        try:
            logo_path = "img/logo.png"
            logo_image = Image.open(logo_path).resize((200, 200), Image.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo_image)

            label_logo = tk.Label(self.root, image=self.logo_photo, bg='white', borderwidth=0, highlightthickness=0)
            label_logo.place(relx=0.5, rely=0.15, anchor="center")
        except Exception as e:
            print(f"Erro ao carregar logo: {e}")



    def go_to_register(self):
        """Abre a tela de registro."""
        self.root.destroy()
        register_root = tk.Tk()
        RegisterScreen(register_root)
        register_root.mainloop()

    def go_to_login(self):
        """Abre a tela de login."""
        self.root.destroy()
        login_root = tk.Tk()
        LoginScreen(login_root)
        login_root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = BeginMenu(root)
    root.mainloop()
