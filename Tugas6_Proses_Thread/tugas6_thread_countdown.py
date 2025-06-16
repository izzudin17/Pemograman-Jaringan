import threading
import time

def countdown(nomor, count):
    print(f"Thread {nomor} mulai countdown dari {count}")
    while count > 0:
        print(f"Thread {nomor}: {count}")
        time.sleep(1)
        count -= 1
    print(f"Thread {nomor} selesai")

if __name__ == "__main__":
    hitung_list = [3, 6, 9, 12, 15]
    thread_list = []

    for i, count in enumerate(hitung_list):
        t = threading.Thread(target=countdown, args=(i + 1, count))
        thread_list.append(t)
        t.start()

    for t in thread_list:
        t.join()

    print("Semua thread countdown selesai.")
