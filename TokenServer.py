import json
import socket
import threading
import socketserver
import jwt
import time
from config import secret
import signal

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        try:
            data = json.loads(data)
            encoded_jwt = jwt.encode({"code": data["code"]}, secret, algorithm="HS256")
            return self.request.send(bytes(encoded_jwt, 'ascii'))
        except:
            return self.request.send(bytes(f'Wrong input format, expected dict', 'ascii'))



class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class TokenServer:

    def __init__(self, ip, port):
        self.server = ThreadedTCPServer((ip, port), ThreadedTCPRequestHandler)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True

    def start_server(self):
        self.server_thread.start()
        print("Server loop running in thread:", self.server_thread.name)

    def stop_server(self):
        self.server.shutdown()
        self.server.server_close()

    def loop(self):
        while True:
            pass

if __name__ == '__main__':
    getter = TokenServer("localhost", 8000)
    getter.start_server()
    getter.loop()
    getter.stop_server()




