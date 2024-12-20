import socket
import logging

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65436  # The port used by the server
logging.info(f"Starting up on {HOST} port {PORT}")
x = 0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while x < 10:
        message = b"ping"
        logging.info(f"Sending {message}")
        s.sendall(message)
        data = s.recv(1024)
        logging.info(f"Received {data}")
        x += 1
