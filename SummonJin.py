def FindJinUsername(uname):
    # under development
    return True

def CheckJinPassword(pw):
    count = 0
    for i in (pw):
        count = count + 1
    
    if count >= 5 and count <= 25:
        return True
    else:
        return False

def summonjin(access):
    if access == 1:
        print("Jenis jin yang dapat dipanggil:")
        print("  (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("  (2) Pembangun - Bertugas membangun candi")
        
        jin_no = int(input("Masukan nomor jenis jin yang ingin dipanggil: ")) 
        while not (jin_no == 1 or jin_no == 2):
            print(f"Tidak ada jenis jin bernomor \"{jin_no}\"!")
            jin_no = int(input("Masukan nomor jenis jin yang ingin dipanggil: "))
        
        role = ''
        if jin_no == 1:
            print("Memilih jin \"Pengumpul\"")
            role = 'Pengumpul'
        else:   # sudah pasti 2
            print("Memilih jin \"Pengumpul\"")
            role = 'Pembangun'
        
        jin_uname = input("Masukkan username jin: ")
        while not (FindJinUsername(jin_uname)):
            print(f"Username \"{jin_uname}\" sudah diambil!")
            jin_uname = input("Masukkan username jin: ")
        
        jin_pw = input("Masukkan password jin: ")
        while not (CheckJinPassword(jin_pw)):
            print("Password panjangnya harus 5-25 karakter!")
            jin_pw = input("Masukkan password jin: ")
        
        print("Mengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...")

        print(f"Jin {jin_uname} berhasil dipanggil!")

        return [[jin_uname, jin_pw, role]]
    else:
        print("Maaf hanya akun bondowoso yang punya akses!")
        return [['','','']]