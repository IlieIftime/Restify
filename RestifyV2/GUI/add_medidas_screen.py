import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import json
import os


class add_medidas:
    """
    Descrição da Fórmula de Cálculo da Altura Ideal da Almofada:

    A altura ideal da almofada é calculada com base em várias métricas que influenciam o conforto e o alinhamento da coluna cervical durante o sono. A fórmula utilizada é:

    Altura ideal = (Largura dos ombros × Posição de dormir / 10) + Curvatura cervical + (Altura do colchão / 20) + (Altura da pessoa / 100) - (Maciez da almofada / 2)

    1. Largura dos ombros: Distância horizontal entre os ombros (cm).
    2. Posição de dormir: 1 (lado), 2 (barriga para cima), 3 (bruços).
    3. Curvatura cervical: Curvatura natural do pescoço (cm).
    4. Altura do colchão: Altura do colchão (cm).
    5. Altura da pessoa: Altura total da pessoa (cm).
    6. Maciez da almofada: Escala de 1 (firme) a 10 (macia).

    Exemplo:
    Largura dos ombros = 50 cm, Posição de dormir = 1, Curvatura cervical = 3 cm, Altura do colchão = 20 cm, Altura da pessoa = 170 cm, Maciez da almofada = 6.
    Altura ideal = (50 × 1 / 10) + 3 + (20 / 20) + (170 / 100) - (6 / 2) = 7,7 cm.
    """
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
        self.sleep_position = None
        self.neck_curvature = None
        self.mattress_height = None
        self.pillow_softness = None

        # Show initial settings by default
        self.show_initial_settings()

    def show_initial_settings(self):
        # Clear the frame (if needed)
        for widget in self.root.winfo_children():
            if widget != self.label_fundo:  # Keep the background image
                widget.destroy()

        # Title
        tk.Label(self.root, text="Configurações Iniciais", font=("Arial", 20), bg='lightgray', fg='black').place(
            relx=0.5, rely=0.1, anchor="center")

        # Sleep position selection
        tk.Label(self.root, text="Posição de Dormir:", font=("Arial", 12), bg='lightgray', fg='black').place(relx=0.3,
                                                                                                             rely=0.2,
                                                                                                             anchor="e")

        # Frame to hold the radio buttons horizontally
        sleep_position_frame = tk.Frame(self.root, bg='lightgray')
        sleep_position_frame.place(relx=0.5, rely=0.2, anchor="center")

        self.sleep_position_var = tk.StringVar()
        self.sleep_position_var.set("1")  # Default value
        sleep_position_options = [("Dormir de Lado", "1"), ("Dormir de Barriga para Cima", "2"),
                                  ("Dormir de Bruços", "3")]

        # Add radio buttons to the frame
        for text, value in sleep_position_options:
            tk.Radiobutton(sleep_position_frame, text=text, variable=self.sleep_position_var, value=value,
                           bg='lightgray').pack(side="left", padx=10)

        # Height input
        tk.Label(self.root, text="Altura (cm):", font=("Arial", 12), bg='lightgray', fg='black').place(relx=0.3,
                                                                                                       rely=0.35,
                                                                                                       anchor="e")
        self.height_entry = ttk.Entry(self.root, width=20)
        self.height_entry.place(relx=0.5, rely=0.35, anchor="center")
        self.height_entry.insert(0, self.height if self.height else "170")  # Default height

        # Shoulder width input
        tk.Label(self.root, text="Largura dos Ombros (cm):", font=("Arial", 12), bg='lightgray', fg='black').place(
            relx=0.3, rely=0.45, anchor="e")
        self.shoulder_width_entry = ttk.Entry(self.root, width=20)
        self.shoulder_width_entry.place(relx=0.5, rely=0.45, anchor="center")
        self.shoulder_width_entry.insert(0,
                                         self.shoulder_width if self.shoulder_width else "40")  # Default shoulder width

        # Neck curvature input
        tk.Label(self.root, text="Curvatura Cervical (cm):", font=("Arial", 12), bg='lightgray', fg='black').place(
            relx=0.3, rely=0.55, anchor="e")
        self.neck_curvature_entry = ttk.Entry(self.root, width=20)
        self.neck_curvature_entry.place(relx=0.5, rely=0.55, anchor="center")
        self.neck_curvature_entry.insert(0,
                                         self.neck_curvature if self.neck_curvature else "3")  # Default neck curvature

        # Mattress height input
        tk.Label(self.root, text="Altura do Colchão (cm):", font=("Arial", 12), bg='lightgray', fg='black').place(
            relx=0.3, rely=0.65, anchor="e")
        self.mattress_height_entry = ttk.Entry(self.root, width=20)
        self.mattress_height_entry.place(relx=0.5, rely=0.65, anchor="center")
        self.mattress_height_entry.insert(0,
                                          self.mattress_height if self.mattress_height else "20")  # Default mattress height

        # Pillow softness input
        tk.Label(self.root, text="Maciez da Almofada (1-10):", font=("Arial", 12), bg='lightgray', fg='black').place(
            relx=0.3, rely=0.75, anchor="e")
        self.pillow_softness_entry = ttk.Entry(self.root, width=20)
        self.pillow_softness_entry.place(relx=0.5, rely=0.75, anchor="center")
        self.pillow_softness_entry.insert(0,
                                          self.pillow_softness if self.pillow_softness else "6")  # Default pillow softness

        # Save button
        tk.Button(self.root, text="Salvar Medidas", command=self.save_initial_settings, font=("Arial", 14), bg='white',
                  fg="black",
                  padx=20, pady=10, bd=2, relief="raised").place(relx=0.3, rely=0.8, anchor="center")

        # Calculate button
        tk.Button(self.root, text="Calcular Altura Ideal", command=self.calculate_ideal_height, font=("Arial", 14),
                  bg='white', fg="black",
                  padx=20, pady=10, bd=2, relief="raised").place(relx=0.5, rely=0.8, anchor="center")

        # Back button
        tk.Button(self.root, text="Voltar", command=self.go_back, width=17, font=("Arial", 14), bg='white', fg="black",
                  padx=20, pady=10, bd=2, relief="raised").place(relx=0.7, rely=0.8, anchor="center")

    def save_initial_settings(self):
        # Save all settings
        self.height = self.height_entry.get()
        self.shoulder_width = self.shoulder_width_entry.get()
        self.sleep_position = self.sleep_position_var.get()
        self.neck_curvature = self.neck_curvature_entry.get()
        self.mattress_height = self.mattress_height_entry.get()
        self.pillow_softness = self.pillow_softness_entry.get()

        # Show confirmation message
        messagebox.showinfo("Configurações", "Medidas salvas com sucesso!")

    def calculate_ideal_height(self):
        try:
            # Get all values
            largura_ombros = float(self.shoulder_width_entry.get())
            posicao_dormir = int(self.sleep_position_var.get())
            curvatura_cervical = float(self.neck_curvature_entry.get())
            altura_colchao = float(self.mattress_height_entry.get())
            altura_pessoa = float(self.height_entry.get())
            maciez_almofada = int(self.pillow_softness_entry.get())

            # Calculate ideal height
            altura_ideal = (
                    (largura_ombros * posicao_dormir) / 10
                    + curvatura_cervical
                    + (altura_colchao / 20)
                    + (altura_pessoa / 100)
                    - (maciez_almofada / 2)
            )

            # Show result
            messagebox.showinfo("Altura Ideal", f"Altura ideal da almofada: {altura_ideal:.2f} cm")

            # Save to JSON
            self.save_to_json(altura_ideal)

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos em todos os campos.")

    def save_to_json(self, altura_ideal):
        data = {
            "altura_pessoa": self.height_entry.get(),
            "largura_ombros": self.shoulder_width_entry.get(),
            "posicao_dormir": self.sleep_position_var.get(),
            "curvatura_cervical": self.neck_curvature_entry.get(),
            "altura_colchao": self.mattress_height_entry.get(),
            "maciez_almofada": self.pillow_softness_entry.get(),
            "altura_ideal_almofada": f"{altura_ideal:.2f} cm"
        }

        # Ensure the config directory exists
        os.makedirs("config", exist_ok=True)

        # Save to JSON file
        with open("config/dados_almofada.json", "w") as f:
            json.dump(data, f, indent=4)

        messagebox.showinfo("Sucesso", "Dados salvos em config/dados_almofada.json")

    def go_back(self):
        self.root.destroy()  # Close the add_medidas screen
        from GUI.definicoes_screen import DefinicoesScreen
        menu_root = tk.Tk()
        menu_screen = DefinicoesScreen(menu_root)
        menu_root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = add_medidas(root)
    root.mainloop()


