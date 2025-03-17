import tkinter as tk
from tkinter import messagebox  # Para exibir pop-ups de aviso
from PIL import Image, ImageTk
import json
import os
import re  # Para usar expressões regulares na validação de email


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

    def validate_email(self, email):
        """Valida o formato do email."""
        # Expressão regular para validar o formato de um email
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, email) is not None

    def validate_password(self, password):
        """Valida o comprimento da password."""
        return len(password) >= 8

    def register(self):
        """Lógica de criação de conta."""
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Verificar se os campos estão preenchidos
        if not username or not password:
            messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos.")
            return False

        # Validar o formato do email
        if not self.validate_email(username):
            messagebox.showwarning("Email Inválido", "O email deve estar no formato exemplo@dominio.com.")
            return False

        # Validar o comprimento da password
        if not self.validate_password(password):
            messagebox.showwarning("Password Inválida", "A password deve ter no mínimo 8 caracteres.")
            return False

        # Verificar se o ficheiro conta.json já existe
        if os.path.exists("config/conta.json"):
            with open("config/conta.json", "r") as f:
                try:
                    contas_existentes = json.load(f)
                    # Verificar se o utilizador já existe
                    if isinstance(contas_existentes, list):  # Se for uma lista de contas
                        for conta in contas_existentes:
                            if conta.get("email") == username:
                                messagebox.showwarning("Utilizador Existente", "Este nome de utilizador já está registado.")
                                return False
                    else:  # Se for um único dicionário (formato antigo)
                        if contas_existentes.get("email") == username:
                            messagebox.showwarning("Utilizador Existente", "Este nome de utilizador já está registado.")
                            return False
                except json.JSONDecodeError:
                    # Se o ficheiro estiver vazio ou corrompido, tratar como novo
                    contas_existentes = []
        else:
            # Se o ficheiro não existir, criar uma lista vazia
            contas_existentes = []

        # Criar a pasta config se não existir
        if not os.path.exists("config"):
            os.makedirs("config")

        # Criar nova conta
        nova_conta = {"email": username, "password": password}

        # Adicionar a nova conta à lista de contas existentes
        if isinstance(contas_existentes, list):
            contas_existentes.append(nova_conta)
        else:
            contas_existentes = [nova_conta]  # Converter para lista se não for

        # Gravar no ficheiro
        with open("config/conta.json", "w") as f:
            json.dump(contas_existentes, f, indent=4)  # Usar indent=4 para melhor legibilidade

        messagebox.showinfo("Sucesso", "Conta criada com sucesso!")  # Pop-up de sucesso
        return True

    def go_back(self):
        """Retorna ao menu inicial."""
        from GUI.begin_menu import BeginMenu
        for widget in self.root.winfo_children():
            widget.destroy()
        BeginMenu(self.root)

    def on_register(self):
        """Chama a função de registro e redireciona para o menu apenas se a conta for criada com sucesso."""
        if self.register():  # Só prossegue se a conta for criada com sucesso
            self.root.destroy()  # Fecha a tela de registro
            from GUI.begin_menu import BeginMenu  # Import MenuScreen aqui para evitar imports circulares
            menu_root = tk.Tk()
            menu_screen = BeginMenu(menu_root)
            menu_root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = RegisterScreen(root)
    root.mainloop()