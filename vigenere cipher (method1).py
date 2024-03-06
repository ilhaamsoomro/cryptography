def encrypt(M, K):
    E=[]
    for i in range (len(M)):
        E.append(alphabet[int(M[i])][int(K[i%len(key)])])
    print (E)

def decrypt(M, K):
    D = []
    for i in range(len(M)):
        col_index = alphabet[0].index(alphabet[int(K[i % len(K)])][0])
        row_index = alphabet[col_index].index(alphabet[0][M[i]])
        D.append(alphabet[0][row_index])
    print(D)

def create_table():
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    table = [alphabet]
    n = 25

    for i in range(n-1):
        new_row = table[-1][1:]  # Remove the first element of the last row
        new_row.append(table[-1][0])  # Add the removed element to the end
        table.append(new_row)

    for row in table:
        print(row)

    return table

alphabet = create_table()

message = str(input("Input message in uppercase : "))
key = str(input("Input Key in uppercase : "))
temp = []
M=[]
K=[]

for i in range(len(message)):
        if message[i].isalpha():
            temp.append(ord(message[i]))
            M.append(temp[-1] - ord('A'))

for i in range(len(key)):
        if key[i].isalpha():
            temp.append(ord(key[i]))
            K.append(temp[-1] - ord('A'))

choice = str(input("E. Encrypt\nD. Decrypt\n"))

if (choice == 'E'):
    encrypt(M, K)
if (choice == 'D'):
    decrypt(M, K)