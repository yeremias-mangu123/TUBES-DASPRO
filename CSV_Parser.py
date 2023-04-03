
# load user.csv data

def CSV_Parser(fname):
    f = open(fname + '.csv', 'r')
    arr = []
    size = 0

    for line in f:
        temp = ""
        for c in line:
            if c != ';':
                temp += c
            if c == ';':
                arr.append(temp)
                size = size + 1
                temp = ''
            
        arr.append(temp)
    return [arr, size]

# CSV_Parser('user')
        
