import tkinter as tk
from PIL import Image, ImageTk


class Conexao_Hardware:
    def __init__(self, root):
        self.root = root
        self.root.title("Conexão Hardware - Restify")
        self.root.geometry("1200x1200")
        self.root.resizable(False, False)

        # Aplicar imagem de fundo
        self.set_background()

        # Exibir logo
        self.show_logo()

        # Criar botões e áreas de status
        self.create_buttons()
        self.create_status_area()

        # Estado inicial da conexão e bateria
        self.conexao_status = "Desconectado"
        self.bateria_status = "N/A"

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
        """Cria os botões para conexão Wi-Fi/Bluetooth e voltar."""
        btn_wifi = tk.Button(self.root, text="Conectar via Wi-Fi", font=("Arial", 14), bg='white', fg='black', padx=20, pady=10, bd=2, relief="raised", command=self.conectar_wifi)
        btn_wifi.place(relx=0.5, rely=0.4, anchor="center", width=200, height=50)

        btn_bluetooth = tk.Button(self.root, text="Conectar via Bluetooth", font=("Arial", 14), bg='white', fg='black', padx=20, pady=10, bd=2, relief="raised", command=self.conectar_bluetooth)
        btn_bluetooth.place(relx=0.5, rely=0.5, anchor="center", width=200, height=50)

        btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 14), bg='white', fg='black', padx=20, pady=10, bd=2, relief="raised", command=self.voltar)
        btn_voltar.place(relx=0.5, rely=0.6, anchor="center", width=200, height=50)

    def create_status_area(self):
        """Cria a área para exibir o status de conexão e bateria."""
        self.status_frame = tk.Frame(self.root, bg='lightgray', bd=2, relief="groove")
        self.status_frame.place(relx=0.5, rely=0.7, anchor="center", width=400, height=100)

        self.status_label = tk.Label(self.status_frame, text="Status: Desconectado", font=("Arial", 12), bg='lightgray', fg='black')
        self.status_label.pack(pady=10)

        self.bateria_label = tk.Label(self.status_frame, text="Bateria: N/A", font=("Arial", 12), bg='lightgray', fg='black')
        self.bateria_label.pack(pady=10)

    def conectar_wifi(self):
        """Simula a conexão via Wi-Fi."""
        self.conexao_status = "Conectado (Wi-Fi)"
        self.bateria_status = "75%"  # Simulação de nível de bateria
        self.atualizar_status()

    def conectar_bluetooth(self):
        """Simula a conexão via Bluetooth."""
        self.conexao_status = "Conectado (Bluetooth)"
        self.bateria_status = "50%"  # Simulação de nível de bateria
        self.atualizar_status()

    def atualizar_status(self):
        """Atualiza os labels de status e bateria."""
        self.status_label.config(text=f"Status: {self.conexao_status}")
        self.bateria_label.config(text=f"Bateria: {self.bateria_status}")

    def voltar(self):
        """Volta para a tela de definições."""
        from GUI.definicoes_screen import DefinicoesScreen
        for widget in self.root.winfo_children():
            widget.destroy()
        DefinicoesScreen(self.root)

    def nome_ligação(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = Conexao_Hardware(root)
    root.mainloop()