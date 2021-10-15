import socket
import json


def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.send(bytes(json.dumps(message), 'ascii'))
        recieve = sock.recv(1024)
        response = str(recieve, 'ascii')
        return response


if __name__ == '__main__':
    token = client('localhost', 8000, {"code": "your code"})
    print(token)
    result = client('localhost', 8001, {"token": token, "text": "your text"})
    print(result)