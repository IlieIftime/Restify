import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from GUI.conexao_hardware import Conexao_Hardware  # Importar a classe de conexão


class Test_conexao:
    def __init__(self, root):
        self.root = root
        self.root.title("Testar Conexão - Restify")

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

        # Instanciar a classe de conexão
        self.conexao = Conexao_Hardware(root)

        # Exibir logo, botão de teste e status da conexão
        self.show_logo()
        self.show_test_button()
        self.show_status()

        # Botão Voltar
        btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 14), bg='white', fg='black',
                               padx=20, pady=10, bd=2, relief="raised", command=self.go_back)
        btn_voltar.place(relx=0.5, rely=0.78, anchor="center", width=200, height=50)

    def show_logo(self):
        """Exibe o logo centralizado no topo."""
        try:
            logo_path = "img/logo.png"
            logo_image = Image.open(logo_path).resize((200, 200), Image.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo_image)

            label_logo = tk.Label(self.root, image=self.logo_photo, bg='white', borderwidth=0, highlightthickness=0)
            label_logo.place(relx=0.5, rely=0.1, anchor="center")
        except Exception as e:
            print(f"Erro ao carregar logo: {e}")

    def show_test_button(self):
        """Exibe o botão para testar a conexão."""
        btn_testar = tk.Button(self.root, text="Testar Conexão", font=("Arial", 14), bg='white', fg='black',
                               padx=20, pady=10, bd=2, relief="raised", command=self.testar_conexao)
        btn_testar.place(relx=0.5, rely=0.5, anchor="center", width=200, height=50)

    def show_status(self):
        """Exibe o status da conexão (ligado/desligado)."""
        # Carregar ícones de status
        self.status_on = ImageTk.PhotoImage(Image.open("img/status_on.png").resize((50, 50), Image.LANCZOS))
        self.status_off = ImageTk.PhotoImage(Image.open("img/status_off.png").resize((50, 50), Image.LANCZOS))

        # Frame para organizar o ícone e o texto de status
        status_frame = tk.Frame(self.root, bg='white')
        status_frame.place(relx=0.5, rely=0.6, anchor="center")

        # Label para exibir o ícone de status
        self.status_label = tk.Label(status_frame, image=self.status_off, bg='white')
        self.status_label.pack(side="left", padx=10)

        # Label para exibir o texto de status
        self.status_text = tk.Label(status_frame, text="Status: Desconhecido", font=("Arial", 14), bg='white', fg='black')
        self.status_text.pack(side="left", padx=10)

    def testar_conexao(self):
        """Testa a conexão e atualiza o status."""
        try:
            # Verificar o status da conexão
            status = self.conexao.nome_ligacao()  # Função que retorna True (ligado) ou False (desligado)

            # Atualizar ícone e texto de status
            if status:
                self.status_label.config(image=self.status_on)
                self.status_text.config(text="Status: Ligado", fg="green")
            else:
                self.status_label.config(image=self.status_off)
                self.status_text.config(text="Status: Desligado", fg="red")

            messagebox.showinfo("Teste Conexão", f"Conexão está {'ligada' if status else 'desligada'}!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao testar conexão: {e}")

    def go_back(self):
        """Redireciona para a tela anterior."""
        self.root.destroy()
        from GUI.teste_sensor_atuador import Test_Hardware
        root = tk.Tk()
        hardware_screen = Test_Hardware(root)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = Test_conexao(root)
    root.mainloop()