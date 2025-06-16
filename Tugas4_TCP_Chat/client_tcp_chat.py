import socket

server_ip = input("Masukkan IP Server: ")
server_port = int(input("Masukkan port server: "))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))
print("Koneksi berhasil")

while True:
    pesan = input("Client: ")
    client_socket.send(pesan.encode())
    if pesan.lower() == "exit":
        break
    data = client_socket.recv(1024).decode()
    print(f"Msg dari server: {data}")

client_socket.close()
print("Koneksi ditutup.")
