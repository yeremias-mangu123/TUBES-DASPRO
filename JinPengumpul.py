import random

def kumpul(access):
    if access == 3:
        pasir = random.randint(0,5)
        batu = random.randint(0,5)
        air = random.randint(0,5)

        print(f"Jin menemukan {pasir} pasir, {batu} batu, {air} air")
        # masukkan data ke bahan_bangunan.csv