import socket


def client():
    host = socket.gethostname()
    port = 5003

    client_socket = socket.socket()
    client_socket.connect((host, port))


if __name__ == '__main__':
    client()
