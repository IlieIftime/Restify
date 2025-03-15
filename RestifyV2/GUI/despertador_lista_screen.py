import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import os


class DespertadorListaScreen:
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

        # Lista de despertadores (inicialmente vazia)
        self.despertadores = []

        # Carregar definições do ficheiro JSON
        self.load_config()

        # Exibir a lista de despertadores
        self.show_despertadores_list()

    def load_config(self):
        """Carrega as definições do ficheiro config.json corretamente."""
        config_path = os.path.join("config", "config.json")
        try:
            if os.path.exists(config_path):
                with open(config_path, "r") as f:
                    dados = json.load(f)
                    if isinstance(dados, list):  # Verificar se os dados são uma lista de despertadores
                        self.despertadores = dados
                    else:
                        self.despertadores = [dados]  # Caso seja um único despertador
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar configurações: {e}")

    def show_despertadores_list(self):
        """Atualiza a interface garantindo que apenas os elementos corretos sejam exibidos."""
        # Limpar widgets, mas manter o fundo
        for widget in self.root.winfo_children():
            if widget != self.label_fundo:
                widget.destroy()

        # Título
        tk.Label(self.root, text="Lista de Despertadores Ativos", font=("Arial", 20), bg='lightgray', fg='black').place(
            relx=0.5, rely=0.1, anchor="center")

        if not self.despertadores:
            # Exibir mensagem se não houver alarmes
            tk.Label(self.root, text="Nenhum alarme adicionado.", font=("Arial", 14), bg='lightgray', fg='black').place(
                relx=0.5, rely=0.3, anchor="center")
        else:
            # Criar um frame para os despertadores
            frame_lista = tk.Frame(self.root, bg="white")
            frame_lista.place(relx=0.5, rely=0.5, anchor="center")

            for i, despertador in enumerate(self.despertadores):
                var = tk.BooleanVar(value=despertador.get("ativo", False))

                # Criar container para cada linha
                linha = tk.Frame(frame_lista, bg="white")
                linha.pack(fill="x", pady=5)

                # Checkbox
                chk = tk.Checkbutton(linha,
                                     text=f"{despertador.get('nome', 'Sem nome')} - {despertador.get('hora', '??:??')}",
                                     variable=var, bg='white', fg='black')
                chk.pack(side="left", padx=10)

                # Botão Editar
                btn_editar = tk.Button(linha, text="Editar", command=lambda d=despertador: self.editar_despertador(d),
                                       width=10, bg='orange', fg='white', font=("Arial", 10))
                btn_editar.pack(side="left", padx=5)

                # Botão Apagar
                btn_apagar = tk.Button(linha, text="Apagar", command=lambda d=despertador: self.apagar_despertador(d),
                                       width=10, bg='red', fg='white', font=("Arial", 10))
                btn_apagar.pack(side="left", padx=5)

        # Botão para adicionar novo despertador
        btn_adicionar = tk.Button(self.root, text="Adicionar Alarme", command=self.adicionar_despertador,
                                  width=20, bg='blue', fg='white', font=("Arial", 12))
        btn_adicionar.place(relx=0.5, rely=0.8, anchor="center")

        # Botão para voltar
        btn_voltar = tk.Button(self.root, text="Voltar", command=self.go_back,
                               width=20, bg='red', fg='white', font=("Arial", 12))
        btn_voltar.place(relx=0.5, rely=0.9, anchor="center")

    def editar_despertador(self, despertador):
        """Fecha a tela atual e abre a tela de edição de despertador."""
        self.root.destroy()
        from GUI.despertador_screen import DespertadorScreen
        despertador_root = tk.Tk()
        DespertadorScreen(despertador_root, despertador, self.despertadores)
        despertador_root.mainloop()

    def apagar_despertador(self, despertador):
        """Remove o despertador da lista e atualiza a exibição."""
        self.despertadores = [d for d in self.despertadores if d != despertador]
        messagebox.showinfo("Apagado", f"Despertador {despertador['nome']} apagado com sucesso!")
        self.show_despertadores_list()

    def adicionar_despertador(self):
        """Fecha a tela atual e abre a tela de adição de despertador."""
        self.root.destroy()
        from GUI.despertador_screen import DespertadorScreen
        despertador_root = tk.Tk()
        DespertadorScreen(despertador_root, None, self.despertadores)
        despertador_root.mainloop()

    def go_back(self):
        """Fecha a tela atual e volta para a tela de definições."""
        self.root.destroy()
        from GUI.definicoes_screen import DefinicoesScreen
        definicoes_root = tk.Tk()
        DefinicoesScreen(definicoes_root)
        definicoes_root.mainloop()


# Exemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    app = DespertadorListaScreen(root)
    root.mainloop()