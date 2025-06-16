def seleksi_nilai(nilai):
    if nilai >= 88:
        return "A"
    elif 77 <= nilai < 88:
        return "B"
    elif 60 <= nilai < 77:
        return "C"
    elif 45 <= nilai < 60:
        return "D"
    else:
        return "E"

# Contoh penggunaan
nilai = int(input("Masukkan nilai: "))
kriteria = seleksi_nilai(nilai)
print(f"Kriteria nilai {nilai} adalah {kriteria}")