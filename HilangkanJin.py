def hapusjin(access):
    if access == 1:
        jin_uname = input("Masukkan username jin : ")
        
        if CheckJinUname(jin_uname):
            ans = input(f"Apakah anda yakin ingin menghapus jin dengan username {jin_uname} (Y/N)? ")

            # some array process hmm...
            print("\nJin telah berasil dihapus dari alam gaib.")
        else:
            print("\nTidak ada jin dengan username tersebut.")
