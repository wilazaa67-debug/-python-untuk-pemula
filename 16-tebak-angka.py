# Bab 16: Game Tebak Angka

import random

skor = 0

while True:
    angka_rahasia = random.randint(1, 20)
    percobaan = 0

    while percobaan < 5:
        tebakan = int(input("Tebak angka 1-20: "))
        percobaan += 1

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

    lagi = input("Main lagi? (y/n): ")
    if lagi != "y":
        break

print("Skor:", skor)