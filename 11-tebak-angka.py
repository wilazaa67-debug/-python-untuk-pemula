# Bab 11: Game Tebak Angka

import random

angka_rahasia = random.randint(1, 10)

while True:
    tebakan = int(input("Tebak angka 1-10: "))

    if tebakan < angka_rahasia:
        print("Kekecilan, coba lagi")
    elif tebakan > angka_rahasia:
        print("Kebesaran, coba lagi")
    else:
        print("Benar! Kamu menang")
        break