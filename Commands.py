# daftar semua command yang ada
# import all files

import Help, Login, Logout, SummonJin
import Misc

access = 0
# 0 artinya masih belum login
# 1 itu bondowoso
# 2 pembangun
# 3 pengepul
# 4 roro jongrang

daftar_jin = [['username','password','role']]

def run(command):
    global access, daftar_jin

    if command == 'help':
        Help.help(access)
    elif command == 'login':
        access = Login.login(access)
    elif command == 'logout':
        access = Logout.logout(access)
    elif command == 'summonjin':
        data = SummonJin.summonjin(access)
        print(data)
        if data[0][2] != '':
            daftar_jin = Misc.append_ku(daftar_jin, data)
            print(daftar_jin)


# by All
# login()
# logout()
# load ()
# save()
# help()
# exit()

# by Bandung Bondowoso
# summoonjin()
# hapusjin()
# ubahjin()

# batchkumpul()
# batchbangun()
# laporanjin()
# laporancandi()

# by Roro Jonggrang
# hancurkancandi()
# ayamberkokok()


# by Jin Pembangun
# bangun()

# by Jin Pengepul
# kumpul()