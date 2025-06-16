from statistics import mean, median, mode

def hitung_statistik(data):
    rata_rata = mean(data)
    nilai_median = median(data)
    try:
        nilai_modus = mode(data)
    except:
        nilai_modus = "Tidak ada modus"
    return rata_rata, nilai_median, nilai_modus

# Contoh penggunaan
data = []
for i in range(10):
    data.append(int(input(f"Masukkan data ke-{i+1}: ")))

rata_rata, median, modus = hitung_statistik(data)
print(f"Rata-rata: {rata_rata}")
print(f"Median: {median}")
print(f"Modus: {modus}")