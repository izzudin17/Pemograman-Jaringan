import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                print("Connection closed by the server.")
                break
            print(message.decode('utf-8'))
        except:
            print("Error receiving message.")
            break

def main():
    HOST = 'localhost'
    PORT = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    print("Connected to server.")

    # Thread untuk menerima pesan
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    # Kirim pesan ke server
    while True:
        message = input()
        if message.lower() == 'exit':
            break
        client_socket.send(message.encode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    main()
