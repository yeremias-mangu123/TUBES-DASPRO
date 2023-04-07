def print_help(arr1, arr2):
    # print(name)
    for i in (arr2):
        print(i[0])
        print('\t' + i[1])
    for i in (arr1):
        print(i[0])
        print('\t' + i[1])

def help(access):
    # struktur matriks [nama, deskripsi]
    print("account level", access)
    all = [['load', 'sebuah deskripsi'], ['save', '...'], ['help', '...'], ['exit', '...']]
    if access == 0: # not login
        accessible = [['login', '...']]
        print_help(all, accessible)

    elif access == 1: # Akun Bandung Bondowoso
        accessible = [['logout', '...'], ['summonjin', '...'], ['hapusjin', '...'], ['ubahjin', '...'], ['batchkumpul', '...'], ['batchbangun', '...'], ['laporanjin', '...'], ['laporancandi', '...']]
        print_help(all, accessible)

    elif access == 2: # Akun Pembangun
        accessible = [['logout', '...'], ['bangun', '...']]
        print_help(all, accessible)

    elif access == 3:
        accessible = [['logout', '...'], ['kumpul', '...']]
        print_help(all, accessible)

    elif access == 4:
        accessible = [['logout', '...'], ['hancurkancandi', '...'], ['ayamberkokok', '...']]
        print_help(all, accessible)

