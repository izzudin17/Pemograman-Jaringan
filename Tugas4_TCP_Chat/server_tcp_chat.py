import socket

# Konfigurasi server
HOST = '0.0.0.0'  # Bisa diakses dari IP mana pun
PORT = 9900

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"[SERVER] Menunggu koneksi di port {PORT}...")
conn, addr = server_socket.accept()
print(f"[SERVER] Terhubung dengan {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Msg dari client: {data}")
    balas = input("Server: ")
    conn.send(balas.encode())
    if balas.lower() == "exit":
        break

conn.close()
server_socket.close()
print("[SERVER] Koneksi ditutup.")
