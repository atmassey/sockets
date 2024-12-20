import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
print("Client started")
x = 0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while x < 10:
        s.sendall(b"ping")
        data = s.recv(1024)
        print(f"Received {data!r}")
        x += 1
