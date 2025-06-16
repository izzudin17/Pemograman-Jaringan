import multiprocessing
import time

def proses(nomor, delay):
    print(f"Proses {nomor} dimulai, delay {delay} detik")
    time.sleep(delay)
    print(f"Proses {nomor} selesai")

if __name__ == "__main__":
    delays = [2, 3, 4, 5, 6]
    proses_list = []

    for i, delay in enumerate(delays):
        p = multiprocessing.Process(target=proses, args=(i + 1, delay))
        proses_list.append(p)
        p.start()

    for p in proses_list:
        p.join()

    print("Semua proses selesai.")
