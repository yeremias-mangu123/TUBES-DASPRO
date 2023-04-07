import Load

def CheckCredential(uname, pw):
    
    user_data = Load.CSV_Parser('user')
    print(user_data)
    
    #username
    Found = False
    role = ''
    for i in user_data:
        if uname == i[0]:
            Found = True
            role = i[2]
            break
    
    if not Found:
        return [2, 0]
    
    
    #password
    Found = False
    for i in user_data:
        if pw == i[1]:
            Found = True
            role = i[2]
            break
    
    if not Found:
        return [3, 0]
    
    # true
    if role == 'bandung_bondowoso':
        return [1, 1]
    elif role == 'roro_jonggrang':
        return [1, 4]
    elif role == 'pembangun':
        return [1, 2]
    elif role == 'pengumpul':
        return [1,3]

def login(access):
    # input apa yang diterima, yaitu access
    # return ???



    
# login()
# print(CheckCredential('lmao','sad'))
