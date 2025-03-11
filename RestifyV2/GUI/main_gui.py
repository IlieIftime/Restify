import tkinter as tk

from PIL import Image, ImageTk


class MainGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Restify - Smart Pillow")
        self.geometry("800x800")  # Tamanho fixo da janela

        # Criar o canvas e aplicá-lo na janela
        self.canvas = tk.Canvas(self, width=800, height=800)
        self.canvas.pack(fill="both", expand=True)

        # Aplicar imagem de fundo
        self.set_background()

        # Exibir logo no topo da tela
        self.show_logo()

    def set_background(self):
        """Define a imagem de fundo para todas as telas utilizando o Canvas."""
        try:
            # Caminho absoluto para a imagem de fundo (corrigido)
            img_path = r"C:\Users\iliei\OneDrive - ISCTE-IUL\Ambiente de Trabalho\Universidade 2º ano\2º Semestre\Empreendedorimos e Inovaçao II\RestifyV1\img.png"
            bg_image = Image.open(img_path).resize((800, 800), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(bg_image)

            # Criar o fundo usando o Canvas
            self.canvas.create_image(0, 0, image=self.bg_photo, anchor=tk.NW)  # (0, 0) é a posição superior esquerda
        except Exception as e:
            print(f"Erro ao carregar imagem de fundo: {e}")

    def show_logo(self):
        """Exibe o logo (300x300 px) centralizado no topo das telas."""
        try:
            # Caminho do logo (ajustado conforme necessário)
            logo_path = r"C:\Users\iliei\OneDrive - ISCTE-IUL\Ambiente de Trabalho\Universidade 2º ano\2º Semestre\Empreendedorimos e Inovaçao II\RestifyV1\logo.png"
            logo_image = Image.open(logo_path).resize((300, 300), Image.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo_image)

            # Calcular a posição X para centralizar o logo
            logo_x = 250 # é a largura do logo
            #logo_Y
            # Exibir o logo no canvas, centralizado no topo
            self.canvas.create_image(logo_x, 20, image=self.logo_photo)  # 20 de distância do topo
        except Exception as e:
            print(f"Erro ao carregar logo: {e}")

    def update_logo_position(self, event):
        """Atualiza a posição do logo quando a janela é redimensionada."""
        logo_x = (self.winfo_width() - 300) // 2
        self.canvas.coords(self.logo, logo_x, 20)

    def show_welcome_screen(self):
        """Exibe a tela de boas-vindas e envia o fundo e o logo para o último plano."""
        self.clear_frame()
        self.show_logo()
        self.canvas.lower(self.bg_photo)
        tk.Label(self.main_frame, text="Bem-vindo ao Restify", font=("Arial", 24)).pack(pady=20)
        tk.Button(self.main_frame, text="Login", font=("Arial", 14), command=self.show_login_screen).pack(pady=10)
        tk.Button(self.main_frame, text="Criar Conta", font=("Arial", 14), command=self.show_registration_screen).pack(pady=10)

    def clear_frame(self):
        """Limpa o frame principal para exibir novos elementos."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_login_screen(self):
        """Exibe a tela de login."""
        self.clear_frame()
        tk.Label(self.main_frame, text="Login", font=("Arial", 24)).pack(pady=20)
        tk.Label(self.main_frame, text="Nome de Utilizador:", font=("Arial", 12)).pack(pady=5)
        username_entry = ttk.Entry(self.main_frame, width=30)
        username_entry.pack(pady=5)
        tk.Button(self.main_frame, text="Entrar", font=("Arial", 14), command=self.login).pack(pady=20)
    def login(self):
        """Lógica de login."""
        print("Lógica de login aqui")
    def show_registration_screen(self):
        """Exibe a tela de registro."""
        self.clear_frame()
        tk.Label(self.main_frame, text="Criar Conta", font=("Arial", 24)).pack(pady=20)
        tk.Label(self.main_frame, text="Nome de Utilizador:", font=("Arial", 12)).pack(pady=5)
        username_entry = ttk.Entry(self.main_frame, width=30)
        username_entry.pack(pady=5)
        tk.Button(self.main_frame, text="Criar Conta", font=("Arial", 14), command=self.register).pack(pady=20)
    def register(self):
        """Lógica de registro."""
        print("Lógica de criação de conta aqui")
if __name__ == "__main__":
    app = MainGUI()
    app.mainloop()
