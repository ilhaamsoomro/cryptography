import math

pt = input("Enter text: ")
key = input("Enter the key: ")
c = int(input("Type 1 for Encryption and 2 for Decryption: "))
ct = ""

def encryption(pt, key, ct):
    key_list = [charac for charac in key]
    col = len(key_list)
    row = math.ceil(len(pt) / col)
    matrix = [['_']*col for i in range(row)]
    sorted_kl = sorted(key_list)
    index = 0
    for i in range(row):
        for j in range(col):
            if index < len(pt):
                matrix[i][j] = pt[index]
                index += 1
            else:
                break
    for charac in sorted_kl:
        for i in range(row):
            ct += matrix[i][key_list.index(charac)]
    return ct

def decryption(pt, key, ct):
    key_list = [charac for charac in key]
    col = len(key_list)
    row = math.ceil(len(pt) / col)
    matrix = [['_']*col for i in range(row)]
    sorted_kl = sorted(key_list)
    index = 0
    for charac in sorted_kl:
        for i in range(row):
            if index < len(pt):
                matrix[i][key_list.index(charac)] = pt[index]
                index += 1
            else:
                break
    for i in range(row):
        for j in range(col):
            ct += matrix[i][j]
    return ct

def choose(c):
    if c == 1:
        print("Encrypted Text:", encryption(pt, key, ct))
    elif c == 2:
        print("Decrypted Text:", decryption(pt, key, ct))


choose(c)