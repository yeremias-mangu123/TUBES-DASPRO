import sys, argparse


def CSV_Parser(fname):
    # user ada 4 baris 3 kolom fix
    # bahan_bangunan ada 4 baris 3 kolom fix
    # candi ada 101 baris 3 kolom fix
    
    if fname == 'user':
        path = sys.argv[0]
        folder = ''
        f = open(path + '\\' + fname + '.csv', 'r')
        # open(nama_file, akses) 
        # akses --> r, w, 
        # r = read, w = write
        # 3 kolom, 2 baris. ini sudah fix g berubah

        user_list = [['' for j in range(3)] for i in range(3)]

        kolom = 0
        baris = 0
        for line in f:
            temp = ""
            print(line)
            
            for c in line:
                if not((c != ';' and not c != '\n') or (not c != ';' and c != '\n')): # XOR
                    temp = temp + c

                if c == '\n':
                    user_list[baris][kolom] = temp
                    kolom = (kolom + 1) % 3
                elif c == ';':
                    user_list[baris][kolom] = temp
                    temp = "" # reset isinya
                    kolom = (kolom + 1) % 3

            baris = baris + 1
        
        return(user_list)

def load():
    pass

# CSV_Parser('user')