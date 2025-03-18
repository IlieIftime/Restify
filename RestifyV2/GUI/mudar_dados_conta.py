import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import os
import re  # Para validação de email


class Editar_Dados:
    def __init__(self, root):
        self.root = root
        self.root.title("Editar Dados - Restify")

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

        # Carregar dados da conta logada
        self.email_logado, self.password_logado = self.obter_utilizador_logado()

        # Exibir os elementos da tela
        self.show_editar_dados_screen()

    def obter_utilizador_logado(self):
        """Lê o email e a password do utilizador logado de um ficheiro."""
        try:
            with open("config/logado.json", "r") as f:
                dados = json.load(f)
                return dados.get("email"), dados.get("password")
        except FileNotFoundError:
            return None, None

    def show_editar_dados_screen(self):
        """Exibe os elementos da tela de editar dados."""
        # Limpar widgets, mas manter o fundo
        for widget in self.root.winfo_children():
            if widget != self.label_fundo:
                widget.destroy()

        # Título
        tk.Label(self.root, text="Editar Dados", font=("Arial", 20), bg='lightgray', fg='black').place(
            relx=0.5, rely=0.1, anchor="center")

        # Campo para editar email
        tk.Label(self.root, text="Novo Email:", font=("Arial", 12), bg='lightgray', fg='black').place(relx=0.3, rely=0.3, anchor="e")
        self.email_entry = tk.Entry(self.root, width=30)
        self.email_entry.place(relx=0.5, rely=0.3, anchor="center")
        if self.email_logado:
            self.email_entry.insert(0, self.email_logado)

        # Campo para editar password
        tk.Label(self.root, text="Nova Password:", font=("Arial", 12), bg='lightgray', fg='black').place(relx=0.3, rely=0.4, anchor="e")
        self.password_entry = tk.Entry(self.root, width=30, show="*")
        self.password_entry.place(relx=0.5, rely=0.4, anchor="center")
        if self.password_logado:
            self.password_entry.insert(0, self.password_logado)

        # Botão para salvar alterações
        btn_salvar = tk.Button(self.root, text="Guardar Alterações", font=("Arial", 12),width=20, bg='white', fg='black', padx=20, pady=10,
                             bd=2, relief="raised", command=self.salvar_alteracoes)
        btn_salvar.place(relx=0.4, rely=0.7, anchor="center")

        # Botão para voltar
        btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 12), bg='white',width=20, fg='black', padx=20, pady=10,
                             bd=2, relief="raised", command=self.go_back)
        btn_voltar.place(relx=0.6, rely=0.7, anchor="center")

    def validar_email(self, email):
        """Valida o formato do email."""
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, email) is not None

    def validar_password(self, password):
        """Valida o comprimento da password."""
        return len(password) >= 8

    def salvar_alteracoes(self):
        """Salva as alterações de email e password."""
        novo_email = self.email_entry.get()
        nova_password = self.password_entry.get()

        # Validar email
        if not self.validar_email(novo_email):
            messagebox.showerror("Erro", "O email deve estar no formato exemplo@dominio.com.")
            return

        # Validar password
        if not self.validar_password(nova_password):
            messagebox.showerror("Erro", "A password deve ter no mínimo 8 caracteres.")
            return

        # Verificar se o ficheiro de contas existe
        if not os.path.exists("config/conta.json"):
            messagebox.showerror("Erro", "Nenhuma conta registada.")
            return

        # Ler o ficheiro de contas
        with open("config/conta.json", "r") as f:
            try:
                contas = json.load(f)
            except json.JSONDecodeError:
                messagebox.showerror("Erro", "Ficheiro de contas corrompido.")
                return

        # Verificar se é uma lista de contas
        if not isinstance(contas, list):
            contas = [contas]  # Converter para lista se for um único dicionário

        # Procurar a conta do utilizador logado
        for conta in contas:
            if conta.get("email") == self.email_logado and conta.get("password") == self.password_logado:
                # Atualizar email e password
                conta["email"] = novo_email
                conta["password"] = nova_password
                break
        else:
            messagebox.showerror("Erro", "Conta não encontrada.")
            return

        # Gravar as contas atualizadas no ficheiro
        with open("config/conta.json", "w") as f:
            json.dump(contas, f, indent=4)

        # Atualizar o ficheiro logado.json com o novo email e password
        self.salvar_utilizador_logado(novo_email, nova_password)

        messagebox.showinfo("Sucesso", "Dados atualizados com sucesso!")
        self.go_back()  # Voltar para o menu após salvar

    def salvar_utilizador_logado(self, email, password):
        """Salva o email e a password do utilizador logado em um ficheiro."""
        dados = {"email": email, "password": password}
        if not os.path.exists("config"):
            os.makedirs("config")
        with open("config/logado.json", "w") as f:
            json.dump(dados, f)

    def go_back(self):
        """Fecha a tela atual e volta para a tela User_menu."""
        self.root.destroy()
        from GUI.user import User_menu  # Importar a tela User_menu
        user_root = tk.Tk()
        User_menu(user_root)
        user_root.mainloop()


# Exemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    app = Editar_Dados(root)
    root.mainloop()