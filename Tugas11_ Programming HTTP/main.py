import urllib.request

def download_data():
    url = input("Masukkan URL untuk didownload: ")
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        print("Data berhasil di-download:")
        print(data.decode('utf-8')[:500])
    except Exception as e:
        print("Gagal:", e)

if __name__ == "__main__":
    download_data()
