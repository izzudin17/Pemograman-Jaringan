import socket
import select

# Inisialisasi server
HOST = 'localhost'
PORT = 12345

# Membuat socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
server_socket.setblocking(False)

# List socket yang akan dipantau
sockets_list = [server_socket]

# Menyimpan client address
clients = {}

print(f"Server berjalan di {HOST}:{PORT}")

while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        # Jika yang readable adalah server_socket -> berarti ada koneksi masuk
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            client_socket.setblocking(False)
            sockets_list.append(client_socket)
            clients[client_socket] = client_address

            print(f"Accepted new connection from {client_address}")
        else:
            try:
                message = notified_socket.recv(1024)

                if not message:
                    # Client disconnect
                    print(f"Closed connection from {clients[notified_socket]}")
                    sockets_list.remove(notified_socket)
                    del clients[notified_socket]
                    continue

                print(f"Received message from {clients[notified_socket]}: {message.decode('utf-8')}")
                # Broadcast ke semua client lain
                for client_socket in clients:
                    if client_socket != notified_socket:
                        client_socket.send(f"From {clients[notified_socket]}: {message.decode('utf-8')}".encode('utf-8'))

            except:
                print(f"Error dengan client {clients[notified_socket]}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
