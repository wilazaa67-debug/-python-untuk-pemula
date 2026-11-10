# Bab 10: Kalkulator Sederhana

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

print("Hasil tambah:", tambah(angka1, angka2))
print("Hasil kurang:", kurang(angka1, angka2))