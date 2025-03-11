import socket

SERVER_IP = "10.192.7.241"  # Coloca aqui o IP do Servidor
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((SERVER_IP, PORT))
    client.sendall(b"Hello, servidor!")
    data = client.recv(1024)

print("Recebido:", data.decode())
