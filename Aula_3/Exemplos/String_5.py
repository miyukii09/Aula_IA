nome = "yuki gonzales nishta"

# usando o split vc coloca coloca os dados dentro de um vetor
nomes = nome.split()

print("quantidade de caracteeres é:",len(nome))
print("quantidade de palavras é:",len(nomes))

# obiserve que nesse expmplo ele nao quebrou letra por eltra, mas sim testo por testo
for i in nomes:
    print (i)