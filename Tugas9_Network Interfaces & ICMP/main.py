from ping3 import ping
import psutil

def check_delay():
    host = input("Masukkan alamat web: ")
    delay = ping(host, unit='ms')
    if delay is None:
        print("Gagal menghubungi host.")
    else:
        print(f"Get pong in {int(delay)}ms")

def list_interfaces():
    interfaces = psutil.net_if_addrs()
    print("List Interface:")
    for iface in interfaces:
        print(iface)

def get_ip_address():
    iface = input("Masukkan interface: ")
    interfaces = psutil.net_if_addrs()
    if iface in interfaces:
        for snic in interfaces[iface]:
            if snic.family.name == 'AF_INET':
                print(f"{iface}: {snic.address}")
                return
        print(f"{iface} tidak memiliki alamat IPv4")
    else:
        print("Interface tidak ditemukan")

def main():
    while True:
        print("\\nMENU PILIHAN")
        print("1. Mengetahui delay ke suatu alamat")
        print("2. Mengetahui list interface")
        print("3. Mengetahui alamat IP")
        pilihan = input("Masukkan pilihan anda: ")

        if pilihan == '1':
            check_delay()
        elif pilihan == '2':
            list_interfaces()
        elif pilihan == '3':
            get_ip_address()
        else:
            print("Pilihan tidak valid atau keluar.")
            break

if __name__ == "__main__":
    main()
