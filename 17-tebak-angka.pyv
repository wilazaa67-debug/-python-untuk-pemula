# Bab 17: Game Tebak Angka

import random

level = int(input("Pilih level (1/2/3): "))

if level == 1:
    batas = 10
elif level == 2:
    batas = 20
else:
    batas = 50

angka_rahasia = random.randint(1, batas)
percobaan = 0

while percobaan < 5:
    tebakan = int(input("Tebak angka 1-" + str(batas) + ": "))
    percobaan += 1

    if tebakan < angka_rahasia:
        print("Kekecilan, coba lagi")
    elif tebakan > angka_rahasia:
        print("Kebesaran, coba lagi")
    else:
        print("Benar! Kamu menang")
        print("Percobaan:", percobaan)
        break
else:
    print("Kesempatan habis, angkanya:", angka_rahasia)