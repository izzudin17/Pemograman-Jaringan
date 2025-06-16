import socket

def koneksi_ke_server():
    server_ip = input("Masukkan IP Server: ")
    server_port = int(input("Masukkan port server: "))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Koneksi berhasil\n")

    while True:
        pesan = input("Client: ")
        client_socket.sendto(pesan.encode(), (server_ip, server_port))

        if pesan.lower() == "quit":
            data, _ = client_socket.recvfrom(1024)
            print(f"Server: {data.decode()}")
            break

        data, _ = client_socket.recvfrom(1024)
        print(f"Msg dari server: {data.decode()}")

def lihat_history():
    nama_file = input("Masukkan nama file: ")
    try:
        with open(nama_file, "r") as f:
            print("\nPesan:")
            print(f.read())
    except FileNotFoundError:
        print("File tidak ditemukan.")

def main():
    while True:
        print("\nMenu Pilihan:")
        print("1. Koneksi ke server")
        print("2. Melihat history")
        pilihan = input("Pilih (1/2): ")

        if pilihan == "1":
            koneksi_ke_server()
        elif pilihan == "2":
            lihat_history()
        else:
            print("Pilihan tidak valid")

        ulang = input("Ingin kembali ke menu? (Y/T): ").upper()
        if ulang != "Y":
            break

if __name__ == "__main__":
    main()
