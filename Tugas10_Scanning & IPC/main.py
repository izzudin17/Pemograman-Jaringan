import socket
import os
import psutil

def check_interface_up(interface):
    stats = psutil.net_if_stats()
    if interface in stats and stats[interface].isup:
        print(f"Interface {interface}: up")
    else:
        print(f"Interface {interface}: down")

def ipc_socketpair():
    parent, child = socket.socketpair()
    pid = os.fork()
    if pid == 0:
        child.send(b"Hello from child")
        msg = child.recv(1024)
        print(f"Child received: {msg.decode()}")
        child.close()
    else:
        msg = parent.recv(1024)
        print(f"Parent received: {msg.decode()}")
        parent.send(b"Hello from parent")
        parent.close()

def main():
    print("MENU PILIHAN")
    print("1. Mengetahui interface up")
    print("2. Mengetahui proses IPC")
    pilihan = input("Masukkan pilihan anda: ")

    if pilihan == '1':
        iface = input("Masukkan interface: ")
        check_interface_up(iface)
    elif pilihan == '2':
        ipc_socketpair()

if __name__ == "__main__":
    main()
