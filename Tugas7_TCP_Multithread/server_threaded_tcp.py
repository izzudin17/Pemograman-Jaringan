import socket
import threading

IP_SERVER = "0.0.0.0"
PORT = 9900

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP_SERVER, PORT))
server_socket.listen(5)

print(f"[SERVER] Menunggu koneksi di {IP_SERVER}:{PORT}...")

def handle_client(conn, addr):
    print(f"[SERVER] Terhubung dengan {addr}")
    try:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"Msg dari client {addr}: {data}")
            balasan = input(f"Server ke {addr}: ")
            conn.send(balasan.encode())
    except ConnectionResetError:
        print(f"[SERVER] Client {addr} memutus koneksi")
    finally:
        conn.close()
        print(f"[SERVER] Koneksi dengan {addr} ditutup")

while True:
    conn, addr = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f"[SERVER] Thread aktif: {threading.active_count() - 1}")
