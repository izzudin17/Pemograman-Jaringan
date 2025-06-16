import socket

IP_SERVER = "0.0.0.0"
PORT = 9900

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((IP_SERVER, PORT))

print(f"[SERVER] Menunggu koneksi di port {PORT}...")

chat_logs = {}

while True:
    data, addr = server_socket.recvfrom(1024)
    pesan = data.decode()
    ip_client = addr[0]
    print(f"Msg dari client: {pesan}")

    if ip_client not in chat_logs:
        chat_logs[ip_client] = []

    chat_logs[ip_client].append(f"Client: {pesan}")

    if pesan.lower() == "quit":
        server_socket.sendto("Koneksi ditutup.".encode(), addr)
        filename = f"{ip_client}.txt"
        with open(filename, "w") as f:
            for msg in chat_logs[ip_client]:
                f.write(msg + "\n")
        print(f"[SERVER] Chat disimpan ke {filename}")
        continue

    balasan = input("Server: ")
    server_socket.sendto(balasan.encode(), addr)
    chat_logs[ip_client].append(f"Server: {balasan}")
