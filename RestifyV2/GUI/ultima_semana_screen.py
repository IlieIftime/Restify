import tkinter as tk

from PIL import Image, ImageTk

class Ultima_semana: #class da ultima semana
    def __init__(self, root):
        self.root = root
        self.root.title("Menu - Restify")
        self.root.geometry("1200x1200")
        self.root.resizable(False, False)

        # Aplicar imagem de fundo
        self.set_background()

        # Exibir logo
        self.show_logo()

        # Criar botões do menu
        self.create_buttons()

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

    def create_buttons(self):
        """Cria os botões do menu principal."""
        btn_horas_dormidas = tk.Button(self.root, text="Sono e movimento", font=("Arial", 14), bg='white', fg='black',
                                     padx=20, pady=10, bd=2, relief="raised", command=self.go_to_horas_dormidas)
        btn_horas_dormidas.place(relx=0.5, rely=0.3, anchor="center", width=200, height=50)

        btn_movimentos_almofada = tk.Button(self.root, text="Movimentos Almofada", font=("Arial", 14), bg='white', fg='black',
                                     padx=20,
                                     pady=10, bd=2, relief="raised", command=self.go_to_movimentos_almofada)
        btn_movimentos_almofada.place(relx=0.5, rely=0.4, anchor="center", width=200, height=50)
        btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 14), bg='white', fg="black",
                               padx=20, pady=10, bd=2, relief="raised", command=self.go_back)
        btn_voltar.place(relx=0.5, rely=0.5, anchor="center", width=200, height=50)

    def go_to_horas_dormidas(self):
        self.root.destroy()  # vai para a tela de horas dormidas
        from GUI.horas_sono_screen import Horas_dormidas  # Import here to avoid circular imports
        horas_dormidas_root = tk.Tk()
        horas_dormidas_screen = Horas_dormidas(horas_dormidas_root)
        horas_dormidas_root.mainloop()

    def go_to_movimentos_almofada(self):
        self.root.destroy()  # vai para a tela do historico de movimentos da almofada
        from GUI.movimento_almofada_screen import MovimentoAlmofada  # Import here to avoid circular imports
        movimento_almofada_root = tk.Tk()
        movimento_almofada_screen = MovimentoAlmofada(movimento_almofada_root)
        movimento_almofada_root.mainloop()

    def go_back(self):
        self.root.destroy()  # volta para a tela da ultima semana
        from GUI.menu_screen import MenuScreen # Import here to avoid circular imports
        menu_root = tk.Tk()
        menu_screen = MenuScreen(menu_root)
        menu_root.mainloop()

    """logica da exibição dos resultados"""

    def power_bi_show(self):
        pass
