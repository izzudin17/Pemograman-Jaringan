import socket

server_ip = input("Masukkan IP Server: ")
server_port = int(input("Masukkan port server: "))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))
print("Koneksi berhasil")

try:
    while True:
        msg = input("Client: ")
        client_socket.send(msg.encode())
        data = client_socket.recv(1024).decode()
        print("Msg dari server:", data)
except:
    print("Koneksi ditutup")
finally:
    client_socket.close()
