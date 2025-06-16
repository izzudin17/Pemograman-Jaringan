def hitung_fungsi(x):
    if x == 0:
        return "Tidak terdefinisi (pembagian oleh nol)"
    return 2 * x**3 + 2 * x + 15 / x

# Contoh penggunaan
x = int(input("Masukkan nilai x: "))
hasil = hitung_fungsi(x)
print(f"f({x}) = {hasil}")