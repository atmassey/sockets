import socket

def main():
    # Create a socket object
    s = socket.socket()

    # Define the port on which you want to connect
    HOST, PORT = 'localhost',65000

    # connect to the server on local computer
    s.connect((HOST, PORT))

    # receive data from the server
    print(s.recv(1024))
    s.close()


if __name__ == '__main__':
    main()