import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class MovimentoAlmofada:
    def __init__(self, root):
        self.root = root
        self.root.title("Movimento da Almofada - Restify")

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

        # Dados sintéticos para o histórico de ajustes da almofada
        self.dados = {
            "noites": ["Noite 1", "Noite 2", "Noite 3", "Noite 4", "Noite 5", "Noite 6", "Noite 7"],
            "ajustes": [5, 7, 6, 8, 9, 7, 6]  # Quantidade de ajustes por noite
        }

        # Exibir os elementos da tela
        self.show_movimento_almofada_screen()

    def show_movimento_almofada_screen(self):
        """Exibe os elementos da tela de movimento da almofada."""
        # Limpar widgets, mas manter o fundo
        for widget in self.root.winfo_children():
            if widget != self.label_fundo:
                widget.destroy()

        # Título
        tk.Label(self.root, text="Movimento da Almofada", font=("Arial", 20), bg='lightgray', fg='black').place(
            relx=0.5, rely=0.1, anchor="center")

        # Frame para o gráfico
        self.grafico_frame = tk.Frame(self.root, bg="white")
        self.grafico_frame.place(relx=0.5, rely=0.4, anchor="center", width=800, height=400)

        # Botão para voltar
        btn_back = tk.Button(self.root, text="Voltar", font=("Arial", 12), bg='white', fg='black', padx=20, pady=10,
                             bd=2, relief="raised", command=self.go_to_menu)
        btn_back.place(relx=0.5, rely=0.8, anchor="center", width=200, height=50)

        # Exibir o gráfico inicial
        self.mostrar_grafico()

    def mostrar_grafico(self):
        """Exibe o gráfico do histórico de ajustes da almofada."""
        # Limpar o frame do gráfico
        for widget in self.grafico_frame.winfo_children():
            widget.destroy()

        # Criar figura e eixos
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(self.dados["noites"], self.dados["ajustes"], color='blue')
        ax.set_title("Histórico de Ajustes da Almofada por Noite")
        ax.set_xlabel("Noite")
        ax.set_ylabel("Quantidade de Ajustes")
        ax.grid(True)

        # Integrar o gráfico ao Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.grafico_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def go_to_menu(self):
        """Fecha a tela atual e volta para o menu principal."""
        self.root.destroy()
        from GUI.ultima_semana_screen import Ultima_semana  # Importar a tela do menu
        menu_root = tk.Tk()
        Ultima_semana(menu_root)
        menu_root.mainloop()

    """logica da exibição dos resultados"""

    def power_bi_show(self):
        pass


# Exemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    app = MovimentoAlmofada(root)
    root.mainloop()