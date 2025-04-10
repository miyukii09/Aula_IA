arquivo = open("aula.txt","r")

linhas = arquivo.readlines()
arquivo.close()

for i in range(len(linhas)):
    linhas[i] = linhas[i].strip()

print(linhas)
print("Tamanho do vetor é", len(linhas))

for linha in linhas:
    print(linha)