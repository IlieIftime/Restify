import socket
import threading
import time
import os
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import platform
import json
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='conexao_hardware.log'
)


class Conexao_Hardware:
    def __init__(self, root):
        self.root = root
        self.root.title("Conexao Hardware - Restify")
        self.root.geometry("1200x1200")
        self.root.resizable(False, False)

        # Configurações de conexão
        self.HOST = '192.168.137.138'  # IP do Raspberry Pi
        self.PORT = 65433
        self.socket = None
        self.conexao_status = "Desconectado"
        self.bateria_status = "N/A"
        self.keep_alive = False
        self.connection_timeout = 10
        self.file_transfer_timeout = 30
        self.max_retries = 3

        # Caminhos dos arquivos
        self.data_recebida_path = r"C:\Users\iliei\OneDrive - ISCTE-IUL\Ambiente de Trabalho\Universidade 2º ano\2º Semestre\Empreendedorimos e Inovaçao II\RestifyV2\data_recebida\data.json"
        self.config_files = [
            r"C:\Users\iliei\OneDrive - ISCTE-IUL\Ambiente de Trabalho\Universidade 2º ano\2º Semestre\Empreendedorimos e Inovaçao II\RestifyV2\config\dados_almofada.json",
            r"C:\Users\iliei\OneDrive - ISCTE-IUL\Ambiente de Trabalho\Universidade 2º ano\2º Semestre\Empreendedorimos e Inovaçao II\RestifyV2\config\despertador_inteligente.json",
            r"C:\Users\iliei\OneDrive - ISCTE-IUL\Ambiente de Trabalho\Universidade 2º ano\2º Semestre\Empreendedorimos e Inovaçao II\RestifyV2\config\dados.json",
            r"C:\Users\iliei\OneDrive - ISCTE-IUL\Ambiente de Trabalho\Universidade 2º ano\2º Semestre\Empreendedorimos e Inovaçao II\RestifyV2\config\config.json"
        ]

        # Iniciar interface
        self.set_background()
        self.show_logo()
        self.create_buttons()
        self.create_status_area()

        # Thread para receber dados dos sensores
        self.sensor_data = {}
        self.start_sensor_thread()

    def set_background(self):
        try:
            img = Image.open("img/img.png").resize((1200, 1200), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(img)
            label_fundo = tk.Label(self.root, image=self.bg_photo)
            label_fundo.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            logging.error(f"Erro ao carregar imagem de fundo: {e}")

    def show_logo(self):
        try:
            logo = Image.open("img/logo.png").resize((200, 200), Image.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo)
            label_logo = tk.Label(self.root, image=self.logo_photo, bg='white')
            label_logo.place(x=500, y=20)
        except Exception as e:
            logging.error(f"Erro ao carregar logo: {e}")

    def create_buttons(self):
        btn_wifi = tk.Button(self.root, text="Conectar via Wi-Fi", font=("Arial", 14),
                             bg='white', fg='black', command=self.conectar_wifi)
        btn_wifi.place(relx=0.5, rely=0.3, anchor="center", width=200, height=50)

        btn_enviar = tk.Button(self.root, text="Enviar Configurações", font=("Arial", 14),
                               bg='white', fg='black', command=self.enviar_configuracoes)
        btn_enviar.place(relx=0.5, rely=0.4, anchor="center", width=200, height=50)

        btn_sensores = tk.Button(self.root, text="Obter Dados Sensores", font=("Arial", 14),
                                 bg='white', fg='black', command=self.obter_dados_sensores)
        btn_sensores.place(relx=0.5, rely=0.5, anchor="center", width=200, height=50)

        btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 14),
                               bg='white', fg='black', command=self.voltar)
        btn_voltar.place(relx=0.5, rely=0.6, anchor="center", width=200, height=50)

    def create_status_area(self):
        self.status_frame = tk.Frame(self.root, bg='lightgray', bd=2, relief="groove")
        self.status_frame.place(relx=0.5, rely=0.7, anchor="center", width=400, height=150)

        self.status_label = tk.Label(self.status_frame, text="Status: Desconectado",
                                     font=("Arial", 12), bg='lightgray')
        self.status_label.pack(pady=5)

        self.bateria_label = tk.Label(self.status_frame, text="Bateria: N/A",
                                      font=("Arial", 12), bg='lightgray')
        self.bateria_label.pack(pady=5)

        self.sensores_label = tk.Label(self.status_frame, text="Sensores: Nenhum dado",
                                       font=("Arial", 10), bg='lightgray', wraplength=380)
        self.sensores_label.pack(pady=5)

    def start_sensor_thread(self):
        """Inicia thread para receber dados dos sensores."""

        def sensor_thread():
            while True:
                if self.socket and self.keep_alive:
                    try:
                        self.socket.sendall(b"GET_SENSOR_DATA")
                        data = self.socket.recv(4096)
                        if data:
                            self.sensor_data = json.loads(data.decode('utf-8'))
                            self.salvar_dados_recebidos()
                            self.atualizar_ui_sensores()
                    except Exception as e:
                        logging.error(f"Erro ao receber dados: {e}")
                time.sleep(2)

        threading.Thread(target=sensor_thread, daemon=True).start()

    def salvar_dados_recebidos(self):
        """Salva os dados recebidos no arquivo especificado."""
        try:
            os.makedirs(os.path.dirname(self.data_recebida_path), exist_ok=True)
            with open(self.data_recebida_path, 'w') as f:
                json.dump(self.sensor_data, f, indent=2)
            logging.info(f"Dados salvos em {self.data_recebida_path}")
        except Exception as e:
            logging.error(f"Erro ao salvar dados: {e}")

    def atualizar_ui_sensores(self):
        """Atualiza a UI com os dados dos sensores."""
        if self.sensor_data:
            texto = (f"Pressão: {self.sensor_data.get('pressao', 'N/A')} kPa\n"
                     f"Proximidade: {self.sensor_data.get('proximidade', 'N/A')} cm\n"
                     f"Servo: {self.sensor_data.get('servo', 'N/A')}°")
            self.sensores_label.config(text=texto)

    def conectar_wifi(self):
        """Conecta ao Raspberry Pi via Wi-Fi."""
        for tentativa in range(self.max_retries):
            try:
                if not self.verificar_conexao():
                    messagebox.showerror("Erro", "Raspberry Pi não está acessível")
                    return False

                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.settimeout(self.connection_timeout)
                self.socket.connect((self.HOST, self.PORT))

                self.conexao_status = "Conectado"
                self.bateria_status = self.obter_status_bateria()
                self.keep_alive = True
                self.atualizar_status()

                messagebox.showinfo("Sucesso", "Conexão estabelecida!")
                return True

            except Exception as e:
                logging.error(f"Tentativa {tentativa + 1} falhou: {e}")
                time.sleep(2)

        messagebox.showerror("Erro", "Falha ao conectar após várias tentativas")
        return False

    def enviar_configuracoes(self):
        """Envia todos os arquivos de configuração para o Raspberry Pi."""
        if not self.socket or not self.keep_alive:
            messagebox.showerror("Erro", "Não há conexão ativa")
            return

        try:
            combined_data = {}
            for config_file in self.config_files:
                try:
                    with open(config_file, 'r') as f:
                        config_name = os.path.basename(config_file)
                        combined_data[config_name] = json.load(f)
                except Exception as e:
                    logging.error(f"Erro ao ler {config_file}: {e}")
                    continue

            # Envia todos os dados combinados
            message = {
                'type': 'combined_config',
                'data': combined_data
            }
            message_str = json.dumps(message)

            self.socket.settimeout(self.file_transfer_timeout)
            self.socket.sendall(f"CONFIG_START:{len(message_str)}".encode('utf-8'))

            if self._verificar_resposta("READY_FOR_CONFIG"):
                self.socket.sendall(message_str.encode('utf-8'))

                if self._verificar_resposta("CONFIG_RECEIVED"):
                    messagebox.showinfo("Sucesso", "Configurações enviadas com sucesso!")
                else:
                    raise Exception("Falha na confirmação de recebimento")
            else:
                raise Exception("Servidor não está pronto para receber configurações")

        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao enviar configurações: {e}")
            self.handle_connection_loss()

    def _verificar_resposta(self, resposta_esperada):
        """Verifica se a resposta do servidor é a esperada."""
        try:
            resposta = self.socket.recv(1024).decode('utf-8')
            return resposta == resposta_esperada
        except Exception as e:
            logging.error(f"Erro ao verificar resposta: {e}")
            return False

    def obter_dados_sensores(self):
        """Solicita os dados mais recentes dos sensores."""
        if not self.socket or not self.keep_alive:
            messagebox.showerror("Erro", "Não há conexão ativa")
            return

        try:
            self.socket.sendall(b"GET_SENSOR_DATA")
            data = self.socket.recv(4096)
            if data:
                self.sensor_data = json.loads(data.decode('utf-8'))
                self.salvar_dados_recebidos()
                self.atualizar_ui_sensores()
                messagebox.showinfo("Sucesso", "Dados dos sensores atualizados!")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao obter dados: {e}")

    def verificar_conexao(self):
        """Verifica se o host está acessível."""
        try:
            param = '-n' if platform.system() == 'Windows' else '-c'
            return os.system(f"ping {param} 1 {self.HOST}") == 0
        except:
            return False

    def obter_status_bateria(self):
        """Obtém o status da bateria."""
        try:
            if self.socket:
                self.socket.sendall(b"GET_BATTERY")
                return self.socket.recv(1024).decode('utf-8')
            return "N/A"
        except:
            return "N/A"

    def atualizar_status(self):
        self.status_label.config(text=f"Status: {self.conexao_status}")
        self.bateria_label.config(text=f"Bateria: {self.bateria_status}")

    def handle_connection_loss(self):
        """Lida com a perda de conexão."""
        self.keep_alive = False
        if self.socket:
            try:
                self.socket.close()
            except:
                pass
            finally:
                self.socket = None

        self.conexao_status = "Desconectado"
        self.bateria_status = "N/A"
        self.atualizar_status()

    def voltar(self):
        self.keep_alive = False
        if self.socket:
            try:
                self.socket.close()
            except:
                pass

        from GUI.definicoes_screen import DefinicoesScreen
        for widget in self.root.winfo_children():
            widget.destroy()
        DefinicoesScreen(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    app = Conexao_Hardware(root)
    root.mainloop()