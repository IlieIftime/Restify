import tkinter as tk
from PIL import Image, ImageTk


class RegisterScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Criar Conta - Restify")
        self.root.geometry("1200x1200")
        self.root.resizable(False, False)

        # Aplicar imagem de fundo
        self.set_background()

        # Exibir logo
        self.show_logo()

        # Criar formulário de registro
        self.create_form()

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

    def create_form(self):
        """Cria os campos de entrada para registro."""
        label_username = tk.Label(self.root, text="Nome de Utilizador:", font=("Arial", 14), bg='lightgray', fg='black', padx=10, pady=5)
        label_username.place(relx=0.4, rely=0.35, anchor="e")

        self.entry_username = tk.Entry(self.root, font=("Arial", 14), bd=2, relief="groove")
        self.entry_username.place(relx=0.5, rely=0.35, anchor="center", width=250, height=30)

        label_password = tk.Label(self.root, text="Password:", font=("Arial", 14), bg='lightgray', fg='black', padx=10, pady=5)
        label_password.place(relx=0.4, rely=0.45, anchor="e")

        self.entry_password = tk.Entry(self.root, font=("Arial", 14), bd=2, relief="groove", show="*")
        self.entry_password.place(relx=0.5, rely=0.45, anchor="center", width=250, height=30)

        btn_register = tk.Button(self.root, text="Criar Conta", font=("Arial", 14), bg='white', fg='black', padx=20, pady=10, bd=2, relief="raised", command=self.on_register)
        btn_register.place(relx=0.5, rely=0.55, anchor="center", width=200, height=50)

        btn_back = tk.Button(self.root, text="Voltar", font=("Arial", 14), bg='white', fg='black', padx=20, pady=10, bd=2, relief="raised", command=self.go_back)
        btn_back.place(relx=0.5, rely=0.65, anchor="center", width=200, height=50)

    def register(self):
        print("Lógica de criação de conta aqui")

    def go_back(self):
        """Retorna ao menu inicial."""
        from GUI.begin_menu import BeginMenu
        for widget in self.root.winfo_children():
            widget.destroy()
        BeginMenu(self.root)

    def on_register(self):
        # Redirect to the menu screen without checking credentials
        self.root.destroy()  # Close the login screen
        from GUI.menu_screen import MenuScreen  # Import MenuScreen here to avoid circular imports
        menu_root = tk.Tk()
        menu_screen = MenuScreen(menu_root)
        menu_root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = RegisterScreen(root)
    root.mainloop()
