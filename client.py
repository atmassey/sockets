import socket
import logging
from logging.handlers import TimedRotatingFileHandler

log_handler = TimedRotatingFileHandler("client.log", when="midnight", interval=1)
log_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
log_handler.setFormatter(log_formatter)
logger = logging.getLogger()
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65437  # The port used by the server
logging.info(f"Starting up on {HOST} port {PORT}")
x = 0
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while x < 10:
            message = b"ping"
            logging.info(f"Sending {message}")
            s.sendall(message)
            data = s.recv(1024)
            logging.info(f"Received {data}")
            x += 1
except KeyboardInterrupt:
    logging.info("Client shutting down")
    s.close()
except Exception as e:
    logging.error(e)
    s.close()