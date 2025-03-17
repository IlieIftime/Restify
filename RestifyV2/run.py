#ficheiro que contem o codigo principal do programa
#Autores: Grupo B23 -
# Ilie Iftime 2ºano TDIA,
# Marin Cepeleaga 2ºano TDIA,
# Cristina Silva 2º ano TDE,
# Patricia Silva 2ºano TDE
"""Falta por uma janela que estabeleça a ligação com a almofada via Wi-Fi ou Bluetooth a simular o processo que um comprador faz após adquirir o produto"""
from GUI.login_screen import LoginScreen
from GUI.begin_menu import BeginMenu
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = BeginMenu(root)
    root.mainloop()