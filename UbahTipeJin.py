def ubahjin(access):
    if access == 1:
        jin_uname = input("Masukkan username jin : ")

        data_jin = FindJin(jin_uname)
        
        if CheckJinUname(jin_uname):
            ans = input(f"Jin ini bertipe \"{data_jin[1]}\". Yakin ingin mengubah ke tipe \"{data_jin[3]}\" (Y/N)? ")
            print("\nJin telah berhasil diubah.")
        else:
            print("\nTidak ada jin dengan username tersebut.")
