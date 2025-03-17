import tkinter as tk
from tkinter import messagebox  # Para exibir pop-ups de erro/sucesso
from PIL import Image, ImageTk
import json
import os


class LoginScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Restify")

        # Definir o tamanho da janela e impedir redimensionamento
        self.root.geometry("1200x1200")
        self.root.resizable(False, False)  # Impedir redimensionamento

        # Carregar e redimensionar a imagem de fundo
        img = Image.open("img/img.png")
        resized_image = img.resize((1200, 1200), Image.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(resized_image)

        # Criar um label para o fundo
        label_fundo = tk.Label(root, image=self.tk_image)
        label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

        # Carregar e redimensionar o logo
        logo = Image.open("img/logo.png")
        resized_logo = logo.resize((200, 200), Image.LANCZOS)
        self.tk_logo = ImageTk.PhotoImage(resized_logo)

        # Criar um label para o logo
        label_logo = tk.Label(root, image=self.tk_logo, bg='white')
        label_logo.place(x=500, y=0)

        # Criar labels para os campos de entrada
        label_email = tk.Label(root, text="Email:", font=("Arial", 14), bg='lightgray', fg='black', padx=10, pady=5)
        label_email.place(relx=0.4, rely=0.35, anchor="e")

        self.entry_login = tk.Entry(root, font=("Arial", 14), bd=2, relief="groove")
        self.entry_login.place(relx=0.5, rely=0.35, anchor="center", width=250, height=30)

        label_password = tk.Label(root, text="Password:", font=("Arial", 14), bg='lightgray', fg='black', padx=10, pady=5)
        label_password.place(relx=0.4, rely=0.45, anchor="e")

        self.entry_password = tk.Entry(root, font=("Arial", 14), bd=2, relief="groove", show="*")
        self.entry_password.place(relx=0.5, rely=0.45, anchor="center", width=250, height=30)

        # Criar botão de login
        btn_login = tk.Button(root, text="Login", font=("Arial", 14), bg='white', fg='black', padx=20, pady=10, bd=2, relief="raised", command=self.on_login)
        btn_login.place(relx=0.5, rely=0.55, anchor="center", width=200, height=50)

        # Botão para voltar ao menu inicial
        btn_back = tk.Button(self.root, text="Voltar", font=("Arial", 14), bg='white', fg='black', padx=20, pady=10, bd=2, relief="raised", command=self.go_back)
        btn_back.place(relx=0.5, rely=0.65, anchor="center", width=200, height=50)

    def go_back(self):
        """Retorna ao menu inicial."""
        from GUI.begin_menu import BeginMenu
        for widget in self.root.winfo_children():
            widget.destroy()
        BeginMenu(self.root)

    def salvar_utilizador_logado(self, email, password):
        """Salva o email e a password do utilizador logado em um ficheiro."""
        dados = {"email": email, "password": password}
        if not os.path.exists("config"):
            os.makedirs("config")
        with open("config/logado.json", "w") as f:
            json.dump(dados, f)

    def on_login(self):
        """Verifica as credenciais e redireciona para o menu se estiverem corretas."""
        email = self.entry_login.get()
        password = self.entry_password.get()

        if not email or not password:
            messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos.")
            return

        # Verificar se o ficheiro de contas existe
        if not os.path.exists("config/conta.json"):
            messagebox.showerror("Erro", "Nenhuma conta registada. Por favor, crie uma conta primeiro.")
            return

        # Ler o ficheiro de contas
        with open("config/conta.json", "r") as f:
            try:
                contas = json.load(f)
            except json.JSONDecodeError:
                messagebox.showerror("Erro", "Ficheiro de contas corrompido.")
                return

        # Verificar se as credenciais correspondem a uma conta existente
        if isinstance(contas, list):  # Se for uma lista de contas
            for conta in contas:
                if conta.get("email") == email and conta.get("password") == password:
                    # Salvar os dados do utilizador logado
                    self.salvar_utilizador_logado(email, password)
                    messagebox.showinfo("Sucesso", "Login bem-sucedido!")
                    self.root.destroy()  # Fechar a tela de login
                    from GUI.menu_screen import MenuScreen  # Importar MenuScreen aqui para evitar imports circulares
                    menu_root = tk.Tk()
                    menu_screen = MenuScreen(menu_root)
                    menu_root.mainloop()
                    return
        else:  # Se for um único dicionário (formato antigo)
            if contas.get("email") == email and contas.get("password") == password:
                # Salvar os dados do utilizador logado
                self.salvar_utilizador_logado(email, password)
                messagebox.showinfo("Sucesso", "Login bem-sucedido!")
                self.root.destroy()  # Fechar a tela de login
                from GUI.menu_screen import MenuScreen  # Importar MenuScreen aqui para evitar imports circulares
                menu_root = tk.Tk()
                menu_screen = MenuScreen(menu_root)
                menu_root.mainloop()
                return

        # Se as credenciais estiverem incorretas
        messagebox.showerror("Erro", "Email ou password incorretos.")


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginScreen(root)
    root.mainloop()