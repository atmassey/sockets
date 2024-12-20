import socket
import logging
from logging.handlers import TimedRotatingFileHandler

log_handler = TimedRotatingFileHandler("server.log", when="midnight", interval=1)
log_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
log_handler.setFormatter(log_formatter)
logger = logging.getLogger()
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65437  # Port to listen on (non-privileged ports are > 1023)
try:
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
except KeyboardInterrupt:
    logging.info("Server shutting down")
    conn.close()
    s.close()
except Exception as e:
    logging.error(e)
    conn.close()
    s.close()