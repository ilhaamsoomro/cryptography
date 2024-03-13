pt = input("Enter your text:   ")
key= int(input("Enter Key size:     "))
choice = int(input("Type 1 for encryption and 2 for decryption"))

def remove_spaces(string):
    return string.replace(" ", "")

pt = remove_spaces(pt)

def encryption(pt, key):
    ct = ''
    pos = 0
    row = 0
    flag = 0
    tg = [['' for _ in range(len(pt))] for _ in range(key)]

    for i in range(len(pt)):
        if flag == 0:
            tg [row][i] = pt[pos]
            row += 1
        if flag == 1:
            tg [row][i] = pt[pos]
            row -= 1
        if row == key:
            flag = 1
            row = row -2
        if row == -1:
            flag = 0
            row = row +2
        pos += 1
    
    for i in tg:
        for j in i:
            if j =='':
                pass
            else:
                ct += j
    print("Transposition grid:  ", tg)
    print("Cipher Text:    ", ct)

    
def decryption(pt, key):
    ct = ''
    pos = 0
    row = 0
    flag = 0
    tg = [['' for _ in range(len(pt))] for _ in range(key)]

    for i in range(len(pt)):
        if flag == 0:
            tg[row][i] = '*'
            row += 1
        if flag == 1:
            tg[row][i] = '*'
            row -= 1
        if row == key:
            flag = 1
            row = row - 2
        if row == -1:
            flag = 0
            row = row + 2

    for i in range(len(tg)):
        for j in range(len(tg[i])):
            if tg[i][j] == '*':
                tg[i][j] = pt[pos]
                pos += 1

    pos = 0
    row = 0
    flag = 0

    for i in range(len(pt)):
        ct += tg[row][pos]
        if flag == 0:
            row += 1
        if flag == 1:
            row -= 1
        if row == key:
            flag = 1
            row = row - 2
        if row == -1:
            flag = 0
            row = row + 2
        pos += 1

    print("Transposition grid:  ", tg)
    print("Plain Text:    ", ct)


if choice == 1:
    encryption(pt, key)
elif choice == 2:
    decryption(pt, key)
