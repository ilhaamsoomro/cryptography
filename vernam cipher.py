# alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# CT = []

# def vernam_cipher(alphabet, CT):
#     plaintext = input("Input text to be encrypted in all caps: ")
#     keyval = input("Key value in all caps: ")
#     choice = input("1 for encryption, 2 for decryption")
#     PTval= []
#     KV= []
#     for char in plaintext:
#         if char in alphabet:
#             PTval.append(alphabet.index(char))

#     for i in range(len(PTval)):
#         KV.append(alphabet.index(keyval[i % len(keyval)]))
#     if (choice == 1):
#         print(encryption(PTval, KV, alphabet, CT))
#     elif (choice == 2):
#         print(decryption(PTval, KV, alphabet, CT))
#     else:
#         print("ERROR, input again")

# def encryption(PTval, KV, alphabet, CT):
#     for i in range(len(PTval)):
#         CT.append(PTval[i] + KV[i])
#         CT[i] += alphabet[CT[i]]
#     for i in range(len(CT)):    
#         if CT[i] >= 26:
#             CT[i] += CT[i] - 26
#             CT[i] += alphabet[CT[i]]
#     print(CT)

# def decryption(PTval, KV, alphabet, CT):
#     for i in range(len(PTval)):
#         CT.append(PTval[i] - KV[i])
#         CT[i] += alphabet[CT[i]]

#     for i in range(len(CT)):    
#         if CT[i] <= 0:
#             CT[i] += CT[i] + 26
#             CT[i] += alphabet[CT[i]]
#     print(CT)

# vernam_cipher(alphabet, CT)


plaintext = input("Input text to be encrypted in all caps: ")
keyval = input("Key value in all caps: ")
choice = input("1 for encryption, 2 for decryption")
alpha=['A', 'I', 'D', 'E', 'H', 'A', 'G', 'K', 'E', 'H']
beta=['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']

print(beta)