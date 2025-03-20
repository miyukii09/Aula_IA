DNA = input("Digite o DNA que vc quer fazer a converter: ").upper()
SDNA = []
texto = ""

for LDNA in DNA:
    if LDNA == 'A' or LDNA == 'T' or LDNA == 'C' or LDNA == 'G':
        texto += LDNA
        if LDNA == 'A':
            SDNA.append('T')            
        elif LDNA == 'T':
            SDNA.append('A')
        elif LDNA == 'C':
            SDNA.append('G')
        else:
            SDNA.append('C')
    else:
        print("Por favor digite o DNA correto!")
        exit()

print(texto)
