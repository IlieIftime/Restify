import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import os


class Editar_conta:
    def __init__(self, root):
        self.root = root
        self.root.title("Editar Conta - Restify")

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

        # Carregar dados existentes (se houver)
        self.dados = self.carregar_dados()

        # Exibir os elementos da tela
        self.show_editar_conta_screen()

    def carregar_dados(self):
        """Carrega os dados do arquivo config/dados.json."""
        dados_path = os.path.join("config", "dados.json")
        if os.path.exists(dados_path):
            try:
                with open(dados_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao carregar dados: {e}")
                return {}
        return {}

    def salvar_dados(self, dados):
        """Salva os dados no arquivo config/dados.json."""
        dados_path = os.path.join("config", "dados.json")
        try:
            with open(dados_path, "w", encoding="utf-8") as f:
                json.dump(dados, f, indent=4, ensure_ascii=False)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar dados: {e}")

    def show_editar_conta_screen(self):
        """Exibe os elementos da tela de editar conta."""
        # Limpar widgets, mas manter o fundo
        for widget in self.root.winfo_children():
            if widget != self.label_fundo:
                widget.destroy()

        # Título
        tk.Label(self.root, text="Editar Conta", font=("Arial", 20), bg='lightgray', fg='black').place(
            relx=0.5, rely=0.1, anchor="center")

        # Campos para editar informações pessoais
        tk.Label(self.root, text="Idade:", font=("Arial", 12), bg='lightgray', fg='black').place(relx=0.3, rely=0.2, anchor="e")
        self.idade_entry = tk.Entry(self.root, width=20)
        self.idade_entry.place(relx=0.5, rely=0.2, anchor="center")
        if "idade" in self.dados:
            self.idade_entry.insert(0, self.dados["idade"])

        tk.Label(self.root, text="Peso (kg):", font=("Arial", 12), bg='lightgray', fg='black').place(relx=0.3, rely=0.3, anchor="e")
        self.peso_entry = tk.Entry(self.root, width=20)
        self.peso_entry.place(relx=0.5, rely=0.3, anchor="center")
        if "peso" in self.dados:
            self.peso_entry.insert(0, self.dados["peso"])

        tk.Label(self.root, text="Sexo:", font=("Arial", 12), bg='lightgray', fg='black').place(relx=0.3, rely=0.4, anchor="e")
        self.sexo_var = tk.StringVar(value=self.dados.get("sexo", "Masculino"))  # Valor padrão
        sexo_options = ["Masculino", "Feminino", "Outro"]
        self.sexo_menu = tk.OptionMenu(self.root, self.sexo_var, *sexo_options)
        self.sexo_menu.place(relx=0.5, rely=0.4, anchor="center")

        tk.Label(self.root, text="IMC:", font=("Arial", 12), bg='lightgray', fg='black').place(relx=0.3, rely=0.5, anchor="e")
        self.imc_entry = tk.Entry(self.root, width=20)
        self.imc_entry.place(relx=0.5, rely=0.5, anchor="center")
        if "imc" in self.dados:
            self.imc_entry.insert(0, self.dados["imc"])

        # Botão para salvar alterações
        btn_salvar = tk.Button(self.root, text="Guardar alterações", font=("Arial", 12), bg='white', fg='black', padx=20, pady=10,
                             bd=2, relief="raised", command=self.salvar_alteracoes)
        btn_salvar.place(relx=0.4, rely=0.8, anchor="center")

        # Botão para voltar
        btn_back = tk.Button(self.root, text="Voltar", font=("Arial", 12), bg='white', fg='black', padx=20, pady=10,
                             bd=2, relief="raised", command=self.go_back)
        btn_back.place(relx=0.6, rely=0.8, anchor="center", width=200, height=50)

    def salvar_alteracoes(self):
        """Salva as alterações feitas pelo usuário."""
        idade = self.idade_entry.get()
        peso = self.peso_entry.get()
        sexo = self.sexo_var.get()
        imc = self.imc_entry.get()

        # Validação básica dos campos
        if not idade or not peso or not sexo or not imc:
            messagebox.showwarning("Atenção", "Preencha todos os campos obrigatórios!")
            return

        # Atualizar os dados
        self.dados.update({
            "idade": idade,
            "peso": peso,
            "sexo": sexo,
            "imc": imc
        })

        # Salvar os dados no arquivo JSON
        self.salvar_dados(self.dados)

        messagebox.showinfo("Sucesso", "Alterações salvas com sucesso!")

    def go_back(self):
        """Retorna ao menu inicial."""
        from GUI.user import User_menu
        for widget in self.root.winfo_children():
            widget.destroy()
        User_menu(self.root)


# Exemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    app = Editar_conta(root)
    root.mainloop()