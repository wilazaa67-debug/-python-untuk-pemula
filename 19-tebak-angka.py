# Bab 19: Game Tebak Angka

import random

skor = 0
level = int(input("Pilih level (1/2/3): "))

if level == 1:
    batas = 10
elif level == 2:
    batas = 20
else:
    batas = 50

while True:
    angka_rahasia = random.randint(1, batas)
    percobaan = 0
    riwayat = []

    while percobaan < 5:
        tebakan = int(input("Tebak angka 1-" + str(batas) + ": "))
        percobaan += 1
        riwayat.append(tebakan)

        if tebakan < angka_rahasia:
            print("Kekecilan, coba lagi")
        elif tebakan > angka_rahasia:
            print("Kebesaran, coba lagi")
        else:
            print("Benar! Kamu menang")
            print("Percobaan:", percobaan)
            skor += 1
            break
    else:
        print("Kesempatan habis, angkanya:", angka_rahasia)

    print("Riwayat tebakan:", riwayat)

    lagi = input("Main lagi? (y/n): ")
    if lagi != "y":
        break

print("Skor:", skor)