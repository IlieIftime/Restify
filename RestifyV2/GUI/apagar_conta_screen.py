import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import os


class Apagar_conta:
    def __init__(self, root):
        self.root = root
        self.root.title("Apagar Conta - Restify")

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

        # Exibir os elementos da tela
        self.show_apagar_conta_screen()

    def show_apagar_conta_screen(self):
        """Exibe os elementos da tela de apagar conta."""
        # Limpar widgets, mas manter o fundo
        for widget in self.root.winfo_children():
            if widget != self.label_fundo:
                widget.destroy()

        # Título
        tk.Label(self.root, text="Apagar Conta", font=("Arial", 20), bg='lightgray', fg='black').place(
            relx=0.5, rely=0.1, anchor="center")

        # Mensagem de confirmação
        tk.Label(self.root, text="Tem certeza que deseja apagar sua conta?", font=("Arial", 14), bg='lightgray',
                fg='black').place(relx=0.5, rely=0.3, anchor="center")

        # Botão para confirmar a exclusão da conta
        btn_confirmar = tk.Button(
            self.root,
            text="Confirmar",
            font=("Arial", 14),
            bg='white',
            fg='black',
            padx=20,
            pady=10,
            bd=2,
            relief="raised",
            command=self.confirmar_apagar_conta
        )
        btn_confirmar.place(relx=0.5, rely=0.5, anchor="center", width=200, height=50)

        # Botão para voltar
        btn_voltar = tk.Button(
            self.root,
            text="Voltar",
            font=("Arial", 14),
            bg='white',
            fg='black',
            padx=20,
            pady=10,
            bd=2,
            relief="raised",
            command=self.go_back
        )
        btn_voltar.place(relx=0.5, rely=0.65, anchor="center", width=200, height=50)

    def confirmar_apagar_conta(self):
        """Lógica para apagar a conta do usuário."""
        resposta = messagebox.askyesno("Confirmar", "Tem certeza que deseja apagar sua conta? Esta ação não pode ser desfeita.")
        if resposta:
            # Apagar a conta do utilizador logado
            if self.apagar_conta_logic():
                messagebox.showinfo("Sucesso", "Sua conta foi apagada com sucesso!")
                self.go_back()  # Voltar para a tela inicial após apagar a conta
            else:
                messagebox.showerror("Erro", "Não foi possível apagar a conta. Tente novamente.")

    def apagar_conta_logic(self):
        """Lógica para apagar a conta do usuário."""
        try:
            # Obter o email do utilizador logado
            email_logado = self.obter_email_logado()
            if not email_logado:
                messagebox.showerror("Erro", "Nenhum utilizador logado.")
                return False

            # Verificar se o ficheiro de contas existe
            if not os.path.exists("config/conta.json"):
                messagebox.showerror("Erro", "Nenhuma conta registada.")
                return False

            # Ler o ficheiro de contas
            with open("config/conta.json", "r") as f:
                contas = json.load(f)

            # Verificar se é uma lista de contas
            if not isinstance(contas, list):
                contas = [contas]  # Converter para lista se for um único dicionário

            # Procurar e remover a conta do utilizador logado
            contas_atualizadas = [conta for conta in contas if conta.get("email") != email_logado]

            # Verificar se a conta foi removida
            if len(contas_atualizadas) == len(contas):
                messagebox.showerror("Erro", "Conta não encontrada.")
                return False

            # Gravar as contas atualizadas no ficheiro
            with open("config/conta.json", "w") as f:
                json.dump(contas_atualizadas, f, indent=4)

            # Limpar os dados do utilizador logado após apagar a conta
            self.limpar_utilizador_logado()
            return True

        except Exception as e:
            print(f"Erro ao apagar conta: {e}")
            return False

    def obter_email_logado(self):
        """Lê o email do utilizador logado de um ficheiro."""
        try:
            with open("config/logado.json", "r") as f:
                dados = json.load(f)
                return dados.get("email")
        except FileNotFoundError:
            return None

    def limpar_utilizador_logado(self):
        """Remove o ficheiro com os dados do utilizador logado."""
        try:
            os.remove("config/logado.json")
        except FileNotFoundError:
            pass  # O ficheiro já não existe

    def go_back(self):
        """Fecha a tela atual e volta para a tela inicial."""
        self.root.destroy()
        from GUI.begin_menu import BeginMenu  # Substitua pelo nome correto da tela inicial
        inicio_root = tk.Tk()
        BeginMenu(inicio_root)
        inicio_root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = Apagar_conta(root)
    root.mainloop()