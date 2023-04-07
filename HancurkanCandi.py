def hancurkancandi(access):
    if access == 4:
        id_candi = int(input("Masukkan ID candi: "))
        ans = input(f"Apakah anda yakin ingin mengahncurkan candi ID: {id_candi} (Y/N)? ")

        if CheckCandi(id_candi):
            # delete from array

            print("Candi telah berhasil dihancurkan.")
        else:
            print("Tidak ada candi dengan ID tersebut.")