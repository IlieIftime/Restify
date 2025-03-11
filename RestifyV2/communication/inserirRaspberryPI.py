import socket

SERVER_IP = "ENDEREÇO_IP_DO_PC"  # Substituir pelo IP real do PC
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((SERVER_IP, PORT))
    client.sendall(b"Hello, PC!")
    data = client.recv(1024)

print("Recebido:", data.decode())
