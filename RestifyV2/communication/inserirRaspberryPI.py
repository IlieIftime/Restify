import socket

SERVER_IP = "ENDEREÇO_IP_DO_PC"  # Substituir pelo IP real do PC
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((SERVER_IP, PORT))
    client.sendall(b"Hello, PC!")
    data = client.recv(1024)

print("Recebido:", data.decode())
"""server do rasp :
import socket
import json
import os
import threading
from datetime import datetime
import random

class SensorServer:
    def __init__(self, host='0.0.0.0', port=65432):
        self.host = host
        self.port = port
        self.socket = None
        self.running = False
        self.data_file = "/home/grupob23/Desktop/data_sent.txt"
        self.config_file = "/home/grupob23/Desktop/config_received.txt"
        
        # Ensure directories exist
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        
        # Initial sensor data
        self.sensor_data = {
            "pressure": 0.0,
            "proximity": 0,
            "servo": 0,
            "timestamp": ""
        }

    def start(self):
        #Start the server.
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        self.running = True
        
        print(f"Server started on {self.host}:{self.port}")
        
        # Thread to simulate sensor data
        threading.Thread(target=self.simulate_sensors, daemon=True).start()
        
        while self.running:
            try:
                conn, addr = self.socket.accept()
                threading.Thread(target=self.handle_client, args=(conn, addr)).start()
            except Exception as e:
                if self.running:
                    print(f"Error accepting connection: {e}")

    def simulate_sensors(self):
        #Simulate random sensor data and save to file.
        while self.running:
            try:
                self.sensor_data = {
                    "pressure": round(random.uniform(0.5, 10.0), 2),  # kPa
                    "proximity": random.randint(0, 100),  # cm
                    "servo": random.randint(0, 180),  # degrees
                    "timestamp": datetime.now().isoformat()
                }
                
                # Save to formatted text file
                with open(self.data_file, 'w') as f:
                    f.write(f"Sensor Data - {datetime.now()}\n")
                    f.write("="*40 + "\n")
                    f.write(f"Pressure: {self.sensor_data['pressure']} kPa\n")
                    f.write(f"Proximity: {self.sensor_data['proximity']} cm\n")
                    f.write(f"Servo Position: {self.sensor_data['servo']} deg\n")
                    f.write(f"Updated at: {self.sensor_data['timestamp']}\n")
                
                time.sleep(2)  # Update every 2 seconds
            except Exception as e:
                print(f"Sensor simulation error: {e}")

    def handle_client(self, conn, addr):
        #Handle client connection.
        print(f"Connection established with {addr}")
        
        try:
            while self.running:
                data = conn.recv(1024)
                if not data:
                    break
                    
                message = data.decode('utf-8').strip()
                
                if message == "GET_SENSOR_DATA":
                    # Send latest sensor data
                    conn.sendall(json.dumps(self.sensor_data).encode('utf-8'))
                elif message.startswith("CONFIG_START:"):
                    self.receive_configs(conn, message)
                elif message == "GET_BATTERY":
                    conn.sendall(b"85%")  # Simulated value
                elif message == "PING":
                    conn.sendall(b"PONG")
                elif message == "TEST_CONNECTION":
                    conn.sendall(b"CONNECTION_OK")
                else:
                    conn.sendall(b"UNKNOWN_COMMAND")
                    
        except Exception as e:
            print(f"Connection error with {addr}: {e}")
        finally:
            conn.close()
            print(f"Connection with {addr} closed")

    def receive_configs(self, conn, message):
        #Receive and process client configurations.
        try:
            # Confirm ready to receive
            conn.sendall(b"READY_FOR_CONFIG")
            
            # Receive data size
            size = int(message.split(":")[1])
            received = 0
            chunks = []
            
            while received < size:
                chunk = conn.recv(min(size - received, 4096))
                if not chunk:
                    raise Exception("Connection interrupted")
                chunks.append(chunk)
                received += len(chunk)
            
            # Process received data
            data = b''.join(chunks).decode('utf-8')
            config_data = json.loads(data)
            
            # Save to text file
            with open(self.config_file, 'w') as f:
                f.write("Received Configurations:\n")
                f.write("="*40 + "\n")
                for file_name, content in config_data['data'].items():
                    f.write(f"\nFile: {file_name}\n")
                    f.write("-"*20 + "\n")
                    f.write(json.dumps(content, indent=2) + "\n")
            
            # Confirm receipt
            conn.sendall(b"CONFIG_RECEIVED")
            print(f"Configurations saved to {self.config_file}")
            
        except Exception as e:
            print(f"Error receiving configurations: {e}")
            conn.sendall(b"CONFIG_ERROR")

    def stop(self):
        #Stop the server.
        self.running = False
        if self.socket:
            self.socket.close()
        print("Server stopped")

if __name__ == "__main__":
    server = SensorServer()
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()
"""