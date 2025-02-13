import socket

def server_program():
    server_socket = socket.socket()
    server_socket.bind(('localhost', 5000))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        conn.send(data.encode())
    conn.close()

def client_program():
    client_socket = socket.socket()
    client_socket.connect(('localhost', 5000))
    message = input(" -> ")
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print('Received from server: ' + data)
        message = input(" -> ")
    client_socket.close()

# for start server
# server_program()

# for start client
# client_program()
