DNA  = input("Digite o DNA que vc quer fazer a converter: ")
SDNA = []

for LDNA in DNA:
    if LDNA.lower()== 'f' or LDNA.lower()== 'g':
        if LDNA.lower() == 'f':
            SDNA.append('g')
        else:
            SDNA.append('f')
    else:
        print (f"Por favor digite o DNA correto!")
        exit()

print(SDNA)