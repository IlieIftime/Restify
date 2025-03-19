import socket
import RPi.GPIO as GPIO
import time

# Configurações do servidor
HOST = '0.0.0.0'  # Escuta em todas as interfaces
PORT = 65432

# Configuração GPIO para o servo
SERVO_PIN = 18  # Substitua pelo pino GPIO conectado ao servo
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Configuração do PWM para o servo
pwm = GPIO.PWM(SERVO_PIN, 50)  # 50 Hz (frequência do servo)
pwm.start(0)  # Inicializa o PWM com duty cycle 0

def set_servo_angle(angle):
    """Define o ângulo do servo."""
    duty = angle / 18 + 2  # Fórmula para calcular o duty cycle
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)  # Tempo para o servo alcançar a posição
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)

def handle_command(command):
    """Executa o comando recebido."""
    try:
        if command == "SERVO:UP":
            set_servo_angle(90)  # Mover para cima (ângulo 90°)
            print("Servo movido para cima!")
        elif command == "SERVO:DOWN":
            set_servo_angle(0)  # Mover para baixo (ângulo 0°)
            print("Servo movido para baixo!")
    except Exception as e:
        print(f"Erro ao executar comando: {e}")

def start_server():
    """Inicia o servidor para receber comandos."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Servidor aguardando conexões em {HOST}:{PORT}...")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Conexão estabelecida com {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    command = data.decode('utf-8').strip()
                    print(f"Comando recebido: {command}")
                    handle_command(command)
                    conn.sendall(b"Comando executado")

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("Servidor encerrado.")
    finally:
        pwm.stop()
        GPIO.cleanup()


"""import socket
import subprocess

# Configurações do servidor
HOST = '0.0.0.0'  # Escuta em todas as interfaces
PORT = 65432

def gravar_audio():
    #Grava áudio de 10 segundos.
    subprocess.run(["arecord", "-d", "10", "-f", "cd", "gravacao.wav"])

def reproduzir_audio():
    #Reproduz o áudio gravado.
    subprocess.run(["aplay", "gravacao.wav"])

def start_server():
    #Inicia o servidor para receber comandos.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Servidor aguardando conexões em {HOST}:{PORT}...")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Conexão estabelecida com {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    command = data.decode('utf-8').strip()
                    print(f"Comando recebido: {command}")
                    if command == "GRAVAR_AUDIO":
                        gravar_audio()
                    elif command == "REPRODUZIR_AUDIO":
                        reproduzir_audio()
                    conn.sendall(b"Comando executado")

if __name__ == "__main__":
    start_server()"""