import socket

# Define os IPs permitidos
ALLOWED_IPS = ["10.192.7.241", "10.192.23.170"]#meu id e do Marin  # Substitui pelo IP do teu PC e do colega

HOST = "0.0.0.0"  # Aceita conexões de qualquer IP, mas serão filtradas
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"Servidor rodando em {HOST}:{PORT}, aguardando conexão...")

    while True:
        conn, addr = server.accept()
        client_ip = addr[0]

        if client_ip in ALLOWED_IPS:
            print(f"Conexão aceita de {client_ip}")
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print("Recebido:", data.decode())
                    conn.sendall(b"Dados recebidos")
        else:
            print(f"Conexão recusada de {client_ip}")
            conn.close()
