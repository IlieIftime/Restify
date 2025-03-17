import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Horas_dormidas:
    def __init__(self, root):
        self.root = root
        self.root.title("Horas Dormidas - Restify")

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

        # Dados sintéticos para o histórico de horas dormidas
        self.dados = {
            "7_dias": {
                "dias": ["Dia 1", "Dia 2", "Dia 3", "Dia 4", "Dia 5", "Dia 6", "Dia 7"],
                "qualidade": [80, 85, 90, 88, 92, 87, 91],
                "ruido": [30, 25, 20, 35, 40, 38, 33],
                "movimentos": [5, 7, 6, 8, 9, 7, 6]
            },
            "30_dias": {
                "dias": [f"Dia {i+1}" for i in range(30)],
                "qualidade": [80 + i % 5 for i in range(30)],
                "ruido": [30 + i % 10 for i in range(30)],
                "movimentos": [5 + i % 4 for i in range(30)]
            },
            "3_meses": {
                "meses": ["Mês 1", "Mês 2", "Mês 3"],
                "qualidade": [85, 88, 90],
                "ruido": [35, 30, 25],
                "movimentos": [7, 6, 5]
            },
            "6_meses": {
                "meses": ["Mês 1", "Mês 2", "Mês 3", "Mês 4", "Mês 5", "Mês 6"],
                "qualidade": [80, 82, 85, 88, 90, 92],
                "ruido": [40, 38, 35, 33, 30, 28],
                "movimentos": [8, 7, 6, 5, 4, 3]
            },
            "1_ano": {
                "meses": [f"Mês {i+1}" for i in range(12)],
                "qualidade": [80 + i % 5 for i in range(12)],
                "ruido": [30 + i % 10 for i in range(12)],
                "movimentos": [5 + i % 4 for i in range(12)]
            }
        }

        # Exibir os elementos da tela
        self.show_horas_dormidas_screen()

    def show_horas_dormidas_screen(self):
        """Exibe os elementos da tela de horas dormidas."""
        # Limpar widgets, mas manter o fundo
        for widget in self.root.winfo_children():
            if widget != self.label_fundo:
                widget.destroy()

        # Título
        tk.Label(self.root, text="Horas Dormidas", font=("Arial", 20), bg='lightgray', fg='black').place(
            relx=0.5, rely=0.1, anchor="center")

        # Frame para o gráfico
        self.grafico_frame = tk.Frame(self.root, bg="white")
        self.grafico_frame.place(relx=0.5, rely=0.4, anchor="center", width=800, height=400)

        # Botões para selecionar o período temporal
        btn_7_dias = tk.Button(self.root, text="7 Dias", font=("Arial", 12), bg='white', fg='black',
                               padx=20, pady=10, bd=2, relief="raised", command=lambda: self.mostrar_grafico("7_dias"))
        btn_7_dias.place(relx=0.2, rely=0.8, anchor="center")

        btn_30_dias = tk.Button(self.root, text="30 Dias", font=("Arial", 12), bg='white', fg='black',
                                padx=20, pady=10, bd=2, relief="raised", command=lambda: self.mostrar_grafico("30_dias"))
        btn_30_dias.place(relx=0.35, rely=0.8, anchor="center")

        btn_3_meses = tk.Button(self.root, text="3 Meses", font=("Arial", 12), bg='white', fg='black',
                                padx=20, pady=10, bd=2, relief="raised", command=lambda: self.mostrar_grafico("3_meses"))
        btn_3_meses.place(relx=0.5, rely=0.8, anchor="center")

        btn_6_meses = tk.Button(self.root, text="6 Meses", font=("Arial", 12), bg='white', fg='black',
                                padx=20, pady=10, bd=2, relief="raised", command=lambda: self.mostrar_grafico("6_meses"))
        btn_6_meses.place(relx=0.65, rely=0.8, anchor="center")

        btn_1_ano = tk.Button(self.root, text="1 Ano", font=("Arial", 12), bg='white', fg='black',
                              padx=20, pady=10, bd=2, relief="raised", command=lambda: self.mostrar_grafico("1_ano"))
        btn_1_ano.place(relx=0.8, rely=0.8, anchor="center")

        # Botão para voltar ao menu
        btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 12), bg='white', fg='black',
                               padx=20, pady=10, bd=2, relief="raised", command=self.go_to_menu)
        btn_voltar.place(relx=0.95, rely=0.8, anchor="center")

        # Exibir o gráfico inicial (7 dias)
        self.mostrar_grafico("7_dias")

    def mostrar_grafico(self, periodo):
        """Exibe o gráfico correspondente ao período selecionado."""
        # Limpar o frame do gráfico
        for widget in self.grafico_frame.winfo_children():
            widget.destroy()

        # Criar figura e eixos
        fig, ax = plt.subplots(figsize=(8, 4))
        dados_periodo = self.dados[periodo]

        # Plotar os dados
        ax.plot(dados_periodo["dias"] if "dias" in dados_periodo else dados_periodo["meses"], dados_periodo["qualidade"], label="Qualidade do Sono", marker='o')
        ax.plot(dados_periodo["dias"] if "dias" in dados_periodo else dados_periodo["meses"], dados_periodo["ruido"], label="Ruído Noturno", marker='o')
        ax.plot(dados_periodo["dias"] if "dias" in dados_periodo else dados_periodo["meses"], dados_periodo["movimentos"], label="Movimentos", marker='o')

        # Configurações do gráfico
        ax.set_title(f"Histórico de Dados ({periodo.replace('_', ' ')})")
        ax.set_xlabel("Dias" if "dias" in dados_periodo else "Meses")
        ax.set_ylabel("Valor")
        ax.grid(True)
        ax.legend()

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
    app = Horas_dormidas(root)
    root.mainloop()

