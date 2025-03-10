from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk

LARGURA = 1200
ALTURA = 1200

# === INTERFACE TKINTER ===
root = tk.Tk()
root.title("Login - Restify")

# Carregar e redimensionar a imagem de fundo
img = Image.open("img.png")
resized_image = img.resize((LARGURA, ALTURA), Image.LANCZOS)
tk_image = ImageTk.PhotoImage(resized_image)

# Criar um label para o fundo
label_fundo = tk.Label(root, image=tk_image)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

# Carregar e redimensionar o logo
logo = Image.open("logo.png")
resized_logo = logo.resize((200, 200), Image.LANCZOS)  # ajuste o tamanho conforme necessário
tk_logo = ImageTk.PhotoImage(resized_logo)

# Criar um label para o logo
label_logo = tk.Label(root, image=tk_logo, bg='white')  # bg='white' para remover transparência, ajuste conforme necessário
label_logo.place(x=500, y=0)  # posição x=500, y=0

# Criar etiquetas para os campos de entrada
label_email = tk.Label(root, text="Email:", font=("Arial", 14))
label_email.place(relx=0.4, rely=0.35, anchor="e")

entry_login = tk.Entry(root, font=("Arial", 14), bd=2, relief="groove")
entry_login.place(relx=0.5, rely=0.35, anchor="center", width=250, height=30)

label_password = tk.Label(root, text="Password:", font=("Arial", 14))
label_password.place(relx=0.4, rely=0.45, anchor="e")

entry_password = tk.Entry(root, font=("Arial", 14), bd=2, relief="groove", show="*")
entry_password.place(relx=0.5, rely=0.45, anchor="center", width=250, height=30)

# Criar botão de registro
btn_registro = tk.Label(root, text="Registro", font=("Arial", 12, "underline"), fg="blue", cursor="hand2")
btn_registro.place(relx=0.45, rely=0.9, anchor="center")  # Ajuste a posição x para adicionar espaçamento

# Criar etiqueta de login ao lado do botão de registro
label_login = tk.Label(root, text="Login", font=("Arial", 12), fg="black")
label_login.place(relx=0.55, rely=0.9, anchor="center")  # Ajuste a posição x para adicionar espaçamento

root.geometry(f"{LARGURA}x{ALTURA}")  # Definir tamanho da janela
root.mainloop()
