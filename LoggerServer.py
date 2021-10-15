import json
import socket
import threading
import socketserver
import jwt
import time
from config import secret, logfile
import logging

logging.basicConfig(filename=logfile, level=logging.INFO)

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        try:
            jsondata = json.loads(data)
            text = jsondata['text']
            key = jsondata['token']
        except:
            return self.request.send(bytes(f'Wrong input format, expected dict', 'ascii'))

        try:
            jwtdecoded = jwt.decode(key, secret, algorithms=["HS256"])
        except:
            return self.request.send(bytes(f'Wrong token', 'ascii'))
        logging.info(f'{jwtdecoded["code"]}: {text}')
        response = bytes(f'Succes', 'ascii')
        self.request.send(response)



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
    server = TokenServer("localhost", 8001)
    server.start_server()
    server.loop()
    server.stop_server()
