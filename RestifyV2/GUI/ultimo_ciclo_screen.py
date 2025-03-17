import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class UltimoCiclo:
    def __init__(self, root):
        self.root = root
        self.root.title("Último Ciclo - Restify")

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

        # Dados sintéticos para os gráficos
        self.dados = {
            "qualidade": [80, 85, 90, 88, 92, 87, 91],
            "ruido": [30, 25, 20, 35, 40, 38, 33],
            "movimentos": [5, 7, 6, 8, 9, 7, 6]
        }

        # Exibir os elementos da tela
        self.show_ultimo_ciclo_screen()

    def show_ultimo_ciclo_screen(self):
        """Exibe os elementos da tela de último ciclo."""
        # Limpar widgets, mas manter o fundo
        for widget in self.root.winfo_children():
            if widget != self.label_fundo:
                widget.destroy()

        # Título
        tk.Label(self.root, text="Último Ciclo", font=("Arial", 20), bg='lightgray', fg='black').place(
            relx=0.5, rely=0.1, anchor="center")

        # Frame para os gráficos
        self.grafico_frame = tk.Frame(self.root, bg="white")
        self.grafico_frame.place(relx=0.5, rely=0.4, anchor="center", width=800, height=400)

        # Botões para alternar entre gráficos
        btn_qualidade = tk.Button(self.root, text="Qualidade do Sono", font=("Arial", 12), bg='white', fg='black',
                                  padx=20, pady=10, bd=2, relief="raised", command=lambda: self.mostrar_grafico("qualidade"))
        btn_qualidade.place(relx=0.2, rely=0.8, anchor="center")

        btn_ruido = tk.Button(self.root, text="Ruído Noturno", font=("Arial", 12), bg='white', fg='black',
                              padx=20, pady=10, bd=2, relief="raised", command=lambda: self.mostrar_grafico("ruido"))
        btn_ruido.place(relx=0.4, rely=0.8, anchor="center")

        btn_movimentos = tk.Button(self.root, text="Movimentos da Almofada", font=("Arial", 12), bg='white', fg='black',
                                   padx=20, pady=10, bd=2, relief="raised", command=lambda: self.mostrar_grafico("movimentos"))
        btn_movimentos.place(relx=0.6, rely=0.8, anchor="center")

        # Botão para voltar ao menu
        btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 12), bg='white', fg='black',
                               padx=20, pady=10, bd=2, relief="raised", command=self.go_to_menu)
        btn_voltar.place(relx=0.8, rely=0.8, anchor="center")

        # Exibir o gráfico inicial
        self.mostrar_grafico("qualidade")

    def mostrar_grafico(self, tipo):
        """Exibe o gráfico correspondente ao tipo selecionado."""
        # Limpar o frame do gráfico
        for widget in self.grafico_frame.winfo_children():
            widget.destroy()

        # Criar figura e eixos
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(self.dados[tipo], marker='o')
        ax.set_title(f"{tipo.capitalize()} durante a noite")
        ax.set_xlabel("Hora")
        ax.set_ylabel("Valor")
        ax.grid(True)

        # Integrar o gráfico ao Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.grafico_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def go_to_menu(self):
        """Fecha a tela atual e volta para o menu principal."""
        self.root.destroy()
        from GUI.menu_screen import MenuScreen  # Importar a tela do menu
        menu_root = tk.Tk()
        MenuScreen(menu_root)
        menu_root.mainloop()

    def go_back(self):
        """Retorna ao menu inicial."""
        from GUI.menu_screen import MenuScreen
        for widget in self.root.winfo_children():
            widget.destroy()
        MenuScreen(self.root)

    """logica da exibição dos resultados"""

    def power_bi_show(self):
        pass


# Exemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    app = UltimoCiclo(root)
    root.mainloop()