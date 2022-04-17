import socket as socket_util

from lab3.config import *


def client_request(request: str) -> str:
    socket = socket_util.socket(socket_util.AF_INET, socket_util.SOCK_STREAM)
    socket.connect((HOST, PORT))
    socket.send(request.encode(ENCODING))
    result = socket.recv(BUFFER_SIZE).decode(ENCODING)
    socket.close()
    return result
