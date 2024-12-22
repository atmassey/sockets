import socket

def main():
    # Create a socket object
    s = socket.socket()

    # Define the port on which you want to connect
    HOST, PORT = '', 65000

    # connect to the server on local computer
    s.bind((HOST, PORT))

    # listen for incoming connections
    s.listen(5)

    print("Server is listening...")

    # a forever loop until we interrupt it or
    # an error occurs
    while True:
        # Establish connection with client.
        c, addr = s.accept()
        print('Got connection from', addr)
        message = "Thank you for connecting"
        # send a thank you message to the client.
        c.send(message.encode())

        # Close the connection with the client
        c.close()

if __name__ == '__main__':
    main()

