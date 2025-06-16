import socket
import os

def menu_service_protokol():
    try:
        port = int(input("Masukkan port protokol: "))
        service = socket.getservbyport(port)
        print(f"Port: {port} => service name: {service}")
    except OSError:
        print(f"Tidak ditemukan service untuk port {port}")
    except ValueError:
        print("Masukkan angka yang valid untuk port.")

def menu_ip_website():
    website = input("Masukkan alamat web: ")
    try:
        ip_web = socket.gethostbyname(website)
        hostname = socket.gethostname()
        ip_local = socket.gethostbyname(hostname)
        print(f"Anda mengakses {website}")
        print(f"dengan alamat IP {ip_web}")
        print(f"dari komputer {hostname} dengan alamat IP {ip_local}")
    except socket.gaierror:
        print("Alamat website tidak valid atau tidak bisa diakses.")

def main():
    while True:
        print("\nMENU PILIHAN:")
        print("1. MENGETAHUI SERVICE DAN PROTOKOL PADA JARINGAN")
        print("2. MENGETAHUI ALAMAT IP DARI SEBUAH WEBSITE")
        pilihan = input("Masukkan pilihan (1/2): ").strip()  # Gunakan strip() untuk hapus spasi/karakter tersembunyi

        if pilihan == "1":
            menu_service_protokol()
        elif pilihan == "2":
            menu_ip_website()
        else:
            print("Pilihan tidak valid!")

        ulang = input("ANDA INGIN MENGULANG (Y/T)? ").upper()
        if ulang != "Y":
            print("Program selesai.")
            break

if __name__ == "__main__":
    main()