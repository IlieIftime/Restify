import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import json
import os


class DespertadorScreen:
    def __init__(self, root, despertador=None, despertadores=None):
        self.root = root
        self.root.title("Despertador - Restify")
        self.despertador = despertador  # Recebe o despertador para edição (ou None para adição)
        self.despertadores = despertadores if despertadores is not None else []  # Lista de despertadores

        # Configuração da janela
        self.root.geometry("1200x1200")
        self.root.resizable(False, False)

        # Carregar e redimensionar a imagem de fundo
        img = Image.open("img/img.png")
        resized_image = img.resize((1200, 1200), Image.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(resized_image)

        # Criar um label para o fundo
        label_fundo = tk.Label(root, image=self.tk_image)
        label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

        # Exibir as configurações do despertador
        self.show_alarm_settings()

    def show_alarm_settings(self):
        # Limpar a tela (se necessário)
        for widget in self.root.winfo_children():
            widget.destroy()

        # Adicionar a imagem de fundo novamente
        label_fundo = tk.Label(self.root, image=self.tk_image)
        label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

        # Título
        tk.Label(self.root, text="Configuração de Alarmes", font=("Arial", 20), bg='lightgray', fg='black').place(
            relx=0.5, rely=0.1, anchor="center")

        # Entrada para o nome do alarme
        tk.Label(self.root, text="Nome do Alarme:", font=("Arial", 12), bg='lightgray', fg='black').place(relx=0.3,
                                                                                                        rely=0.2,
                                                                                                        anchor="e")
        self.nome_entry = ttk.Entry(self.root, width=20)
        self.nome_entry.place(relx=0.5, rely=0.2, anchor="center")
        if self.despertador:
            self.nome_entry.insert(0, self.despertador.get("nome", "Despertador"))  # Usar .get() para evitar KeyError
        else:
            self.nome_entry.insert(0, "Despertador")

        # Entrada para a hora do alarme
        tk.Label(self.root, text="Hora do Alarme (HH:MM):", font=("Arial", 12), bg='lightgray', fg='black').place(
            relx=0.3, rely=0.3, anchor="e")
        self.alarm_entry = ttk.Entry(self.root, width=20)
        self.alarm_entry.place(relx=0.5, rely=0.3, anchor="center")
        if self.despertador:
            self.alarm_entry.insert(0, self.despertador.get("hora", "07:00"))  # Usar .get() para evitar KeyError
        else:
            self.alarm_entry.insert(0, "07:00")

        # Dias ativos (checkboxes)
        tk.Label(self.root, text="Dias Ativos:", font=("Arial", 12), bg='lightgray', fg='black').place(relx=0.3, rely=0.4,
                                                                                                    anchor="e")
        days = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
        self.day_vars = []
        for i, day in enumerate(days):
            var = tk.BooleanVar(value=day in self.despertador.get("active_days", []) if self.despertador else False)
            chk = tk.Checkbutton(self.root, text=day, variable=var, bg='lightgray', fg='black')
            chk.place(relx=0.4 + 0.1 * (i % 3), rely=0.45 + 0.05 * (i // 3), anchor="w")
            self.day_vars.append(var)

        # Botão para salvar
        tk.Button(self.root, text="Salvar", command=self.save_alarm_settings, width=20, font=("Arial", 14), bg='white', fg="black",
                                   padx=20, pady=10, bd=2, relief="raised").place(relx=0.5, rely=0.6, anchor="center")

        # Botão para voltar
        tk.Button(self.root, text="Voltar", command=self.go_back, width=20, font=("Arial", 14), bg='white', fg="black",
                                   padx=20, pady=10, bd=2, relief="raised").place(relx=0.5, rely=0.7, anchor="center")

    def save_alarm_settings(self):
        # Obter os dados do formulário
        nome = self.nome_entry.get()
        hora = self.alarm_entry.get()
        dias_ativos = [day for day, var in
                       zip(['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'], self.day_vars) if
                       var.get()]

        # Criar ou atualizar o despertador
        novo_despertador = {"nome": nome, "hora": hora, "active_days": dias_ativos, "ativo": True}
        if self.despertador:
            # Atualiza o despertador existente
            self.despertador.update(novo_despertador)
        else:
            # Adiciona um novo despertador
            self.despertadores.append(novo_despertador)

        # Guardar as definições no ficheiro JSON
        self.save_config()

        messagebox.showinfo("Salvo", f"Despertador {nome} salvo com sucesso!")
        self.go_back()

    def save_config(self):
        """Guarda as definições no ficheiro config.json."""
        config_path = os.path.join("config", "config.json")
        try:
            with open(config_path, "w") as f:
                json.dump({"despertadores": self.despertadores}, f, indent=4)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao guardar configurações: {e}")

    def go_back(self):
        # Fechar a tela atual e voltar para a lista de despertadores
        self.root.destroy()
        from GUI.despertador_lista_screen import DespertadorListaScreen
        lista_root = tk.Tk()
        DespertadorListaScreen(lista_root)
        lista_root.mainloop()


# Exemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    app = DespertadorScreen(root)
    root.mainloop()