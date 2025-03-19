import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import json
import os
import threading
import time
from pygame import mixer  # Para reprodução de áudio


class Despertador_Inteligente:
    def __init__(self, root, despertador=None, despertadores_inteligentes=None):
        self.root = root
        self.root.title("Despertador Inteligente - Restify")

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

        # Inicializar o mixer de áudio
        mixer.init()

        # Variáveis de controle
        self.audio_file = None
        self.volume = 0
        self.vibration_intensity = 0
        self.pillow_height = 0
        self.is_running = False

        # Exibir os elementos da tela
        self.show_logo()
        self.show_alarm_settings()

        # Botão para voltar
        tk.Button(self.root, text="Voltar", command=self.go_back, width=20, font=("Arial", 14), bg='white', fg="black",
                  padx=20, pady=10, bd=2, relief="raised").place(relx=0.75, rely=0.75, anchor="center")

        # Botão para guardar despertador
        tk.Button(self.root, text="Guardar Despertador", command=self.guardar_despertador, width=20, font=("Arial", 14), bg='white', fg="black",
                  padx=20, pady=10, bd=2, relief="raised").place(relx=0.25, rely=0.75, anchor="center")

        # Variáveis para armazenar o despertador e a lista de despertadores inteligentes
        self.despertador = despertador
        self.despertadores_inteligentes = despertadores_inteligentes if despertadores_inteligentes else []

        # Se estiver editando um despertador, carregar os dados
        if self.despertador:
            self.carregar_dados_despertador()
        else:
            # Define o nome padrão como "Despertador"
            self.nome_var.set("Despertador")

    def carregar_dados_despertador(self):
        """Carrega os dados do despertador existente na interface."""
        self.nome_var.set(self.despertador.get("nome", ""))
        hora, minuto = self.despertador.get("hora", "07:00").split(":")
        self.hora_var.set(hora)
        self.minuto_var.set(minuto)
        for dia, var in self.dias_semana_vars.items():
            var.set(self.despertador.get("dias_semana", {}).get(dia, False))
        self.audio_file = self.despertador.get("audio_file", None)
        self.som_ambiente_var.set(self.despertador.get("som_ambiente", False))
        self.vibracao_var.set(self.despertador.get("vibracao", False))
        self.ondas_var.set(self.despertador.get("ondas", False))

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

    def show_alarm_settings(self):
        """Exibe as configurações do despertador inteligente."""
        # Título
        tk.Label(self.root, text="Despertador Inteligente", font=("Arial", 20), bg='lightgray', fg='black').place(
            relx=0.5, rely=0.2, anchor="center")

        # Campo para o nome do despertador
        tk.Label(self.root, text="Nome do Despertador:", font=("Arial", 14), bg='lightgray', fg='black').place(
            relx=0.3, rely=0.3, anchor="center")
        self.nome_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.nome_var, font=("Arial", 14), width=20).place(relx=0.5, rely=0.3, anchor="center")

        # Seleção de hora
        tk.Label(self.root, text="Hora:", font=("Arial", 14), bg='lightgray', fg='black').place(
            relx=0.3, rely=0.35, anchor="center")
        self.hora_var = tk.StringVar(value="07")
        tk.Spinbox(self.root, from_=0, to=23, textvariable=self.hora_var, font=("Arial", 14), width=5).place(relx=0.4, rely=0.35, anchor="center")
        tk.Label(self.root, text=":", font=("Arial", 14), bg='lightgray', fg='black').place(relx=0.45, rely=0.35, anchor="center")
        self.minuto_var = tk.StringVar(value="00")
        tk.Spinbox(self.root, from_=0, to=59, textvariable=self.minuto_var, font=("Arial", 14), width=5).place(relx=0.5, rely=0.35, anchor="center")

        # Seleção de dias da semana
        tk.Label(self.root, text="Dias da Semana:", font=("Arial", 14), bg='lightgray', fg='black').place(
            relx=0.1, rely=0.4, anchor="center")
        self.dias_semana_vars = {
            "Segunda": tk.BooleanVar(value=False),
            "Terça": tk.BooleanVar(value=False),
            "Quarta": tk.BooleanVar(value=False),
            "Quinta": tk.BooleanVar(value=False),
            "Sexta": tk.BooleanVar(value=False),
            "Sábado": tk.BooleanVar(value=False),
            "Domingo": tk.BooleanVar(value=False)
        }
        x_offset = 0.25
        for dia, var in self.dias_semana_vars.items():
            tk.Checkbutton(self.root, text=dia, variable=var, font=("Arial", 12), bg='lightgray', fg='black').place(
                relx=x_offset, rely=0.4, anchor="center")
            x_offset += 0.1

        # Botão para selecionar arquivo de áudio
        tk.Button(self.root, text="Selecionar Áudio", command=self.select_audio_file, width=20, font=("Arial", 14),
                  bg='white', fg="black", padx=20, pady=10, bd=2, relief="raised").place(relx=0.5, rely=0.5, anchor="center")

        # Botão ON/OFF para som ambiente
        self.som_ambiente_var = tk.BooleanVar(value=False)
        tk.Checkbutton(self.root, text="Som Ambiente", variable=self.som_ambiente_var, font=("Arial", 14),
                       bg='lightgray', fg='black').place(relx=0.15, rely=0.6, anchor="center")

        # Botão ON/OFF para vibração
        self.vibracao_var = tk.BooleanVar(value=False)
        tk.Checkbutton(self.root, text="Vibração", variable=self.vibracao_var, font=("Arial", 14),
                       bg='lightgray', fg='black').place(relx=0.35, rely=0.6, anchor="center")

        # Botão ON/OFF para movimento de ondas
        self.ondas_var = tk.BooleanVar(value=False)
        tk.Checkbutton(self.root, text="Movimento de Ondas", variable=self.ondas_var, font=("Arial", 14),
                       bg='lightgray', fg='black').place(relx=0.55, rely=0.6, anchor="center")

        # Botão para iniciar/parar o despertador
        tk.Button(self.root, text="Iniciar Despertador", command=self.start_alarm, width=20, font=("Arial", 14),
                  bg='white', fg="black", padx=20, pady=10, bd=2, relief="raised").place(relx=0.5, rely=0.75, anchor="center")

    def select_audio_file(self):
        """Abre uma janela para selecionar um arquivo de áudio."""
        self.audio_file = filedialog.askopenfilename(
            title="Selecione um arquivo de áudio",
            filetypes=(("Arquivos de Áudio", "*.mp3 *.wav"), ("Todos os arquivos", "*.*")))
        if self.audio_file:
            messagebox.showinfo("Áudio Selecionado", f"Arquivo selecionado: {os.path.basename(self.audio_file)}")

    def start_alarm(self):
        """Inicia o despertador inteligente."""
        if not self.audio_file:
            messagebox.showerror("Erro", "Selecione um arquivo de áudio antes de iniciar.")
            return

        if self.is_running:
            messagebox.showinfo("Info", "O despertador já está em execução.")
            return

        self.is_running = True
        self.volume = 0
        self.vibration_intensity = 0
        self.pillow_height = 0

        # Iniciar threads para controle de volume, vibração e movimento
        threading.Thread(target=self.control_volume).start()
        threading.Thread(target=self.control_vibration).start()
        threading.Thread(target=self.control_pillow).start()

        # Reproduzir o áudio
        mixer.music.load(self.audio_file)
        mixer.music.play()

    def control_volume(self):
        """Aumenta o volume gradualmente."""
        while self.is_running and self.volume < 100:
            self.volume += 1
            mixer.music.set_volume(self.volume / 100)
            time.sleep(5)  # Aumenta 1% a cada 5 segundos

    def control_vibration(self):
        """Aumenta a intensidade da vibração gradualmente."""
        while self.is_running and self.vibration_intensity < 100:
            self.vibration_intensity += 0.5
            # Simular controle de vibração (substitua por código real para controlar motores)
            print(f"Intensidade da vibração: {self.vibration_intensity}%")
            time.sleep(10)  # Aumenta 0.5% a cada 10 segundos

    def control_pillow(self):
        """Simula o movimento de ondas na almofada."""
        direction = 1  # 1 para subir, -1 para descer
        while self.is_running:
            self.pillow_height += 0.2 * direction
            if self.pillow_height >= 100 or self.pillow_height <= 0:
                direction *= -1  # Inverte a direção
            # Simular controle de servos (substitua por código real para controlar servos)
            print(f"Altura da almofada: {self.pillow_height}%")
            time.sleep(10)  # Ajusta a altura a cada 10 segundos

    def stop_alarm(self):
        """Para o despertador inteligente."""
        self.is_running = False
        mixer.music.stop()
        messagebox.showinfo("Despertador Parado", "O despertador foi parado.")

    def guardar_despertador(self):
        """Guarda as configurações do despertador no ficheiro JSON."""
        # Carregar a lista existente de despertadores inteligentes
        inteligente_path = os.path.join("config", "despertador_inteligente.json")
        if os.path.exists(inteligente_path):
            with open(inteligente_path, "r") as f:
                data = json.load(f)
                despertadores_inteligentes = data.get("despertadores_inteligentes", [])
        else:
            despertadores_inteligentes = []

        # Verifica se estamos editando um despertador existente ou criando um novo
        if self.despertador is None:
            # Se for um novo despertador, cria um novo ID
            novo_id = max([d["id"] for d in despertadores_inteligentes], default=0) + 1
            despertador = {
                "id": novo_id,
                "nome": self.nome_var.get(),
                "hora": f"{self.hora_var.get()}:{self.minuto_var.get()}",
                "dias_semana": {dia: var.get() for dia, var in self.dias_semana_vars.items()},
                "audio_file": self.audio_file,
                "som_ambiente": self.som_ambiente_var.get(),
                "vibracao": self.vibracao_var.get(),
                "ondas": self.ondas_var.get(),
                "ativo": True  # Por padrão, o despertador é ativado ao ser guardado
            }
            # Adiciona o novo despertador à lista
            despertadores_inteligentes.append(despertador)
        else:
            # Se estiver editando um despertador existente, atualiza as configurações
            despertador = {
                "id": self.despertador["id"],  # Mantém o ID existente
                "nome": self.nome_var.get(),
                "hora": f"{self.hora_var.get()}:{self.minuto_var.get()}",
                "dias_semana": {dia: var.get() for dia, var in self.dias_semana_vars.items()},
                "audio_file": self.audio_file,
                "som_ambiente": self.som_ambiente_var.get(),
                "vibracao": self.vibracao_var.get(),
                "ondas": self.ondas_var.get(),
                "ativo": True  # Por padrão, o despertador é ativado ao ser guardado
            }
            # Atualiza o despertador na lista
            for i, desp in enumerate(despertadores_inteligentes):
                if desp["id"] == self.despertador["id"]:
                    despertadores_inteligentes[i] = despertador
                    break

        # Salva as configurações no ficheiro JSON
        self.save_inteligente_config(despertadores_inteligentes)

        # Mostra mensagem de sucesso
        messagebox.showinfo("Sucesso", "Despertador guardado com sucesso!")

        # Volta para a lista de despertadores
        self.go_back()

    def save_inteligente_config(self, despertadores_inteligentes):
        """Salva a lista de despertadores inteligentes no ficheiro despertador_inteligente.json."""
        inteligente_path = os.path.join("config", "despertador_inteligente.json")
        try:
            with open(inteligente_path, "w") as f:
                json.dump({"despertadores_inteligentes": despertadores_inteligentes}, f, indent=4)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar despertadores inteligentes: {e}")

    def go_back(self):
        """Fecha a tela atual e volta para a lista de despertadores."""
        self.root.destroy()
        from GUI.despertador_lista_screen import DespertadorListaScreen
        lista_root = tk.Tk()
        DespertadorListaScreen(lista_root)
        lista_root.mainloop()


# Exemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    app = Despertador_Inteligente(root)
    root.mainloop()