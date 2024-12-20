import socket
import logging

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65436  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    logging.info(f"Listening on {HOST} port {PORT}")
    s.listen()
    conn, addr = s.accept()
    logging.info(f"Connected by {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            logging.info(f"Received {data}")
            if data == b"ping":
                conn.sendall(b"pong")
            if isinstance(data, int):
                logging.info(f"Received integer {data}")    
            if data == b"quit":
                logging.info("Request to quit received")
                conn.close()
                break