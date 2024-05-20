import tkinter as tk
import socket
import threading
class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.root = tk.Tk()
        self.root.title("Chat Client")

        self.chat_history = tk.Text(self.root, state=tk.DISABLED)
        self.chat_history.pack(expand=True, fill=tk.BOTH)

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(fill=tk.X)

        self.input_field = tk.Entry(self.input_frame)
        self.input_field.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.input_field.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.daemon = True
        receive_thread.start()

    def send_message(self, event=None):
        message = self.input_field.get()
        if message:
            self.socket.send(message.encode())
            self.input_field.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                message = self.socket.recv(1024).decode()
                if message:
                    self.chat_history.configure(state=tk.NORMAL)
                    self.chat_history.insert(tk.END, message + '\n')
                    self.chat_history.configure(state=tk.DISABLED)
                    self.chat_history.see(tk.END)
            except OSError:
                break
        

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 12345
    client = ChatClient(HOST, PORT)
    client.run()