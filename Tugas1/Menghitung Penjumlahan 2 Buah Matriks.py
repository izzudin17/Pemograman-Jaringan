def jumlah_matriks(matriks1, matriks2):
    hasil = [[0 for _ in range(len(matriks1[0]))] for _ in range(len(matriks1))]
    for i in range(len(matriks1)):
        for j in range(len(matriks1[0])):
            hasil[i][j] = matriks1[i][j] + matriks2[i][j]
    return hasil

# Contoh penggunaan
matriks1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriks2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
hasil = jumlah_matriks(matriks1, matriks2)
print("Hasil penjumlahan matriks:")
for baris in hasil:
    print(baris)