#ficheiro que contem o codigo principal do programa
#Autores: Grupo B23 -
# Ilie Iftime 2ºano TDIA,
# Marin Cepeleaga 2ºano TDIA,
# Cristina Silva 2º ano TDE,
# Patricia Silva 2ºano TDE
from GUI.main_gui import MainGUI


if __name__ == "__main__":
    app = MainGUI()
    app.show_welcome_screen()
   # Troque para LoginScreen() ou RegisterScreen() para testar
    app.mainloop()
