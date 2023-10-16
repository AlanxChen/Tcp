import socket
import threading


class TCPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

    def handle_client(self, client_socket):
        request = client_socket.recv(1024).decode('utf-8')
        print(f"Received data from client: {request}")
        response = f"Server received: {request}"
        client_socket.send(response.encode('utf-8'))
        client_socket.close()

    def start(self):
        while True:
            client, addr = self.server_socket.accept()
            print(f"Accepted connection from {addr[0]}:{addr[1]}")
            client_handler = threading.Thread(target=self.handle_client, args=(client,))
            client_handler.start()


    
if __name__=='__main__':
    serve_host='127.0.0.1'
    serve_port=1234
    server=TCPServer(serve_host,serve_port)
    server.start()