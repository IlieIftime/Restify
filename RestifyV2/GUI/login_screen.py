import tkinter as tk

from PIL import Image, ImageTk


class LoginScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Restify")

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

        # Load and resize logo
        logo = Image.open("img/logo.png")
        resized_logo = logo.resize((200, 200), Image.LANCZOS)
        self.tk_logo = ImageTk.PhotoImage(resized_logo)

        # Create a label for the logo
        label_logo = tk.Label(root, image=self.tk_logo, bg='white')
        label_logo.place(x=500, y=0)

        # Create labels for input fields
        label_email = tk.Label(root, text="Email:", font=("Arial", 14), bg='lightgray', fg='black', padx=10, pady=5)
        label_email.place(relx=0.4, rely=0.35, anchor="e")

        self.entry_login = tk.Entry(root, font=("Arial", 14), bd=2, relief="groove")
        self.entry_login.place(relx=0.5, rely=0.35, anchor="center", width=250, height=30)

        label_password = tk.Label(root, text="Password:", font=("Arial", 14), bg='lightgray', fg='black', padx=10, pady=5)
        label_password.place(relx=0.4, rely=0.45, anchor="e")

        self.entry_password = tk.Entry(root, font=("Arial", 14), bd=2, relief="groove", show="*")
        self.entry_password.place(relx=0.5, rely=0.45, anchor="center", width=250, height=30)

        # Create login button
        btn_login = tk.Button(root, text="Login", font=("Arial", 14), bg='white', fg='black', padx=20, pady=10, bd=2, relief="raised",command=self.on_login)
        btn_login.place(relx=0.5, rely=0.55, anchor="center", width=200, height=50)

        btn_back = tk.Button(self.root, text="Voltar", font=("Arial", 14), bg='white', fg='black', padx=20, pady=10,
                             bd=2, relief="raised", command=self.go_back)
        btn_back.place(relx=0.5, rely=0.65, anchor="center", width=200, height=50)

    def go_back(self):
        """Retorna ao menu inicial."""
        from GUI.begin_menu import BeginMenu
        for widget in self.root.winfo_children():
            widget.destroy()
        BeginMenu(self.root)

    def on_login(self):
        # Redirect to the menu screen without checking credentials
        self.root.destroy()  # Close the login screen
        from GUI.menu_screen import MenuScreen  # Import MenuScreen here to avoid circular imports
        menu_root = tk.Tk()
        menu_screen = MenuScreen(menu_root)
        menu_root.mainloop()