import socket
import sys
import global_parameter

class TCPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))

    def send_message(self, message):
        self.client_socket.send(message.encode('utf-8'))
        response = self.client_socket.recv(1024).decode('utf-8')
        print(f"Server response: {response}")
    def request(self,method,version=0.5,body="\r\n"):
        url=f"diantp://{self.host}:{self.port}"    
        tp_request=f"{method} {url} Diantp/{version} \r\n CSeq: {global_parameter.global_CSeq} INVITE \r\n {body}\r\n"
        global_parameter.global_CSeq+=1
        self.send_message(tp_request)
    def close(self):
        self.client_socket.close()

if __name__=="__main__":
    server_host='127.0.0.1'
    server_port=1234
    client=TCPClient(server_host,server_port)
    msg=input("请输入协议的方法:")
    client.request(msg)
    client.close()