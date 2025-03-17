import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

class add_medidas:
    def __init__(self, root):
        self.root = root
        self.root.title("Adicionar Medidas - Restify")

        # Set the window size to 1200x1200 and prevent resizing
        self.root.geometry("1200x1200")
        self.root.resizable(False, False)  # Disable resizing

        # Load and resize background image
        img = Image.open("img/img.png")
        resized_image = img.resize((1200, 1200), Image.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(resized_image)

        # Create a label for the background
        self.label_fundo = tk.Label(root, image=self.tk_image)
        self.label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

        # Initialize settings
        self.height = None
        self.shoulder_width = None

        # Show initial settings by default
        self.show_initial_settings()

    def show_initial_settings(self):
        # Clear the frame (if needed)
        for widget in self.root.winfo_children():
            if widget != self.label_fundo:  # Keep the background image
                widget.destroy()

        # Title
        tk.Label(self.root, text="Configurações Iniciais", font=("Arial", 20), bg='lightgray', fg='black').place(relx=0.5, rely=0.1, anchor="center")

        # Height input
        tk.Label(self.root, text="Altura (cm):", font=("Arial", 12), bg='lightgray', fg='black').place(relx=0.3, rely=0.2, anchor="e")
        self.height_entry = ttk.Entry(self.root, width=20)
        self.height_entry.place(relx=0.5, rely=0.2, anchor="center")
        self.height_entry.insert(0, self.height if self.height else "170")  # Default height

        # Shoulder width input
        tk.Label(self.root, text="Largura dos Ombros (cm):", font=("Arial", 12), bg='lightgray', fg='black').place(relx=0.3, rely=0.3, anchor="e")
        self.shoulder_width_entry = ttk.Entry(self.root, width=20)
        self.shoulder_width_entry.place(relx=0.5, rely=0.3, anchor="center")
        self.shoulder_width_entry.insert(0, self.shoulder_width if self.shoulder_width else "40")  # Default shoulder width

        # Save button
        tk.Button(self.root, text="Salvar Configurações", command=self.save_initial_settings,font=("Arial", 14), bg='white', fg="black",
                                   padx=20, pady=10, bd=2, relief="raised").place(relx=0.5, rely=0.5, anchor="center")

        # Back button
        tk.Button(self.root, text="Voltar", command=self.go_back,width=17, font=("Arial", 14), bg='white', fg="black",
                                   padx=20, pady=10, bd=2, relief="raised").place(relx=0.5, rely=0.6, anchor="center")

    def save_initial_settings(self):
        # Save height and shoulder width
        self.height = self.height_entry.get()
        self.shoulder_width = self.shoulder_width_entry.get()

        # Show confirmation message
        messagebox.showinfo("Configurações", "Configurações iniciais salvas com sucesso!")

        # Optionally, you can save these settings to a file or database here
        # self.save_config()

    def go_back(self):
        self.root.destroy()  # Close the add_medidas screen
        from GUI.definicoes_screen import DefinicoesScreen
        menu_root = tk.Tk()
        menu_screen = DefinicoesScreen(menu_root)
        menu_root.mainloop()
