def append_ku(arr, data):
    if isinstance(arr, list):

        baris, kolom = len_ku(arr)
        print(baris,kolom)
        baris2, kolom2 = len_ku(data)
        # print(baris, kolom)

        arr2 = [['' for j in range(kolom2)] for i in range(baris+1)]
        
        # copy array
        for i in range(baris):
            for j in range(kolom):
                arr2[i][j] = arr[i][j]
        
        for j in range(kolom2):
            arr2[baris][j] = data[0][j]

        return arr2
    else:
        len = len_ku(arr)
        print(len)
        arr2 = ['' for i in range(len+1)]

        for i in range(len):
            arr2[i] = arr[i]
        arr2[len] = data

        return arr2

def len_ku(arr):
    if isinstance(arr[0], str) or isinstance(arr[0], int) or isinstance(arr[0], float) or isinstance(arr[0], bool):
        len = 0
        for i in arr:
            len = len + 1
        return len
    elif isinstance(arr[0], list):
        baris = 0
        kolom = 0

        for i in arr:
            baris = baris + 1
            temp = 0
            for j in i:
                temp = temp + 1
            kolom = temp
        
        return baris, kolom
        

# arr_new = append_ku([[1,2],[2,3], [3,4]], [20,3])
# print(arr_new)