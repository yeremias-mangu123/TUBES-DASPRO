# jumlah bahan bangunan 1-5
import random

def CheckMaterials(pasir, batu, air):
    # baca data bahan_bangunan.csv

def bangun(access):
    if access == 2:
        pasir = random.randint(1,5)
        batu = random.randint(1,5)
        air = random.randint(1,5)

        candi = 2 # harus get current candi count
        if (candi == 100):
            print("Candi tidak bisa dibangun!")
            print("Sisa candi yang perlu dibangun: 0")
        elif CheckMaterials(pasir, batu, air):
            print("Candi berhasil dibangun")
            # sisa candi pikirin cok gimana hmmm...

            # masukin data ke candi.csv

            print(f"Sisa candi yang perlu dibangun: {100 - candi}")
        else:
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")


bangun(2)