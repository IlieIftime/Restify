import tkinter as tk

from PIL import Image, ImageTk


class AjusteAlmofadaScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Ajuste da Almofada - Restify")

        # Set the window size to 1200x1200 and prevent resizing
        self.root.geometry("1200x1200")
        self.root.resizable(False, False)  # Disable resizing

        # Load and resize background image
        img = Image.open("img/img.png")
        resized_image = img.resize((1200, 1200), Image.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(resized_image)

        # Create a label for the background
        label_fundo = tk.Label(root, image=self.tk_image)
        label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a label for the title
        label_titulo = tk.Label(root, text="Ajuste da Almofada", font=("Arial", 24), bg='lightgray', fg='black', padx=10, pady=10)
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")

        # Create Up and Down buttons
        btn_up = tk.Button(root, text="Up", font=("Arial", 14), bg='green', fg='white', padx=20, pady=10, bd=2, relief="raised", command=self.move_up)
        btn_up.place(relx=0.5, rely=0.3, anchor="center", width=200, height=200)

        btn_down = tk.Button(root, text="Down", font=("Arial", 14), bg='red', fg='white', padx=20, pady=10, bd=2, relief="raised", command=self.move_down)
        btn_down.place(relx=0.5, rely=0.5, anchor="center", width=200, height=200)

        # Create a button to go back
        btn_voltar = tk.Button(root, text="Voltar", font=("Arial", 14), bg='white', fg="black",
                                   padx=20, pady=10, bd=2, relief="raised", command=self.go_back)
        btn_voltar.place(relx=0.5, rely=0.7, anchor="center", width=200, height=50)

    def move_up(self):
        print("Moving Up")  # Replace with actual functionality

    def move_down(self):
        print("Moving Down")  # Replace with actual functionality

    def go_back(self):
        self.root.destroy()  # Close the ajuste da almofada screen
        from GUI.definicoes_screen import DefinicoesScreen  # Import here to avoid circular imports
        definicoes_root = tk.Tk()
        definicoes_screen = DefinicoesScreen(definicoes_root)
        definicoes_root.mainloop()