import threading
import time

def cetak_ganjil():
    for i in range(1, 11):
        if i % 2 == 1:
            print(f"Ganjil: {i}")
            time.sleep(1)

def cetak_genap():
    for i in range(1, 11):
        if i % 2 == 0:
            print(f"Genap: {i}")
            time.sleep(1)

if __name__ == "__main__":
    t1 = threading.Thread(target=cetak_ganjil)
    t2 = threading.Thread(target=cetak_genap)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Cetak ganjil-genap selesai.")
