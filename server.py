import socket
import threading
import tkinter as tk
class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.clients = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

    def handle_client(self, client_socket, client_address):
        print(f"Connection from {client_address}")
        self.clients.append(client_socket)

        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    print(f"Received message: {message}")
                    self.broadcast(message)
                else:
                    client_socket.close()
                    self.clients.remove(client_socket)
                    print("Connection lost")
                    break
            except:
                client_socket.close()
                self.clients.remove(client_socket)
                break

    def broadcast(self, message):
        for client in self.clients:
            try:
                client.send(message.encode())
            except:
                client.close()
                self.clients.remove(client)

    def run(self):

        print("Server running...")
        while True:
            client_socket, client_address = self.server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
            client_thread.daemon = True
            client_thread.start()
            


if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 12345
    server = ChatServer(HOST, PORT)
    server.run()