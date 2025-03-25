import socket

# Configurações do servidor
HOST = '192.168.137.138'  # Endereço IP específico do Raspberry Pi
PORT = 65433  # Porta para escutar

# Cria um socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Permite reutilizar o endereço
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Associa o socket ao endereço e porta
    server_socket.bind((HOST, PORT))
    # Escuta por conexões (máximo de 5 clientes na fila)
    server_socket.listen(5)
    print(f"Servidor escutando em {HOST}:{PORT}...")

    while True:
        # Aceita uma nova conexão
        client_socket, client_address = server_socket.accept()
        with client_socket:
            print(f"Conexão estabelecida com {client_address}")
            while True:
                # Recebe dados do cliente
                data = client_socket.recv(1024).decode('utf-8').strip()
                if not data:
                    break
                print(f"Recebido: {data}")

                # Responde com base na mensagem recebida
                if data == "x1":
                    resposta = "a"
                elif data == "x2":
                    resposta = "b"
                else:
                    resposta = "Mensagem desconhecida"

                # Envia a resposta ao cliente
                client_socket.sendall(resposta.encode('utf-8'))
                print(f"Enviado: {resposta}")