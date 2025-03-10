import socket

class RaspberryCommunication:
    def __init__(self, host="192.168.1.10", port=5000):
        self.server_address = (host, port)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client.connect(self.server_address)
            print("Conectado ao Raspberry Pi")
        except Exception as e:
            print(f"Erro ao conectar ao Raspberry: {e}")

    def send_data(self, data):
        try:
            self.client.sendall(data.encode())
        except Exception as e:
            print(f"Erro ao enviar dados: {e}")

    def receive_data(self):
        try:
            return self.client.recv(1024).decode()
        except Exception as e:
            print(f"Erro ao receber dados: {e}")
            return None
