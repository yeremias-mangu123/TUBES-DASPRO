import CSV_Parser

def CheckCredential(uname, pw):
    user_data = CSV_Parser.CSV_Parser('user')
    print(user_data)
    
    #username
    Found = False
    for i in range(0+3,user_data[1]+1, 3):
        if uname == user_data[0][i]:
            Found = True
            break
    
    if not Found:
        return 2
    
    
    #password
    Found = False
    for i in range(1+3,user_data[1]+2, 3):
        if pw == user_data[0][i]:
            Found = True
    
    if not Found:
        return 3
    
    # true
    return 1

def Login():
    uname = input('Username: ')
    pw = input('Password: ')

    resp = CheckCredential(uname, pw)

    if resp == 1:
        print(f'Selamat datang, {uname}')
    elif resp == 2:
        print('Username tidak terdaftar!')
    elif resp == 3:
        print('Password salah!')
    
Login()
# print(CheckCredential('lmao','sad'))
