# Bab 12: Game Tebak Angka

import random

angka_rahasia = random.randint(1, 20)

while True:
    tebakan = int(input("Tebak angka 1-20: "))

    if tebakan < angka_rahasia:
        print("Kekecilan, coba lagi")
    elif tebakan > angka_rahasia:
        print("Kebesaran, coba lagi")
    else:
        print("Benar! Kamu menang")
        break