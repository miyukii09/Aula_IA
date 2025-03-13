# vc  pode criar um vetor dando um nome para ele e ja setando os valores dentro dele
alunos = ['Felipe','Isabele','Pedro','Ligia','Mateus']

print(alunos)

# tem algumas formas de vc poder exibir os valores que vc quer, como passar a posicao que vc quer que ele exiba
print(f"O primeiro valor do vetor é {alunos[0]}")

print(f"O ultimo valor do vetor é {alunos[4]}")

# ou vc pode passar valores negativos, assim o valor era invertido, tipo no exemplo, o -1 sera a mesma coisa quer o 4, isso por que ele e o ultimo elemento do vetor
print(f"o valor do vetor é {alunos[-1]}")

# tem duas formas de vc printar
# dessa forma vc nao quarda posocao
print()
for nome in alunos:
    print(nome)

# dessa forma vc ja quarda a posicao
print()
for i in range(5):
    print(f"na posaocao {i} o valor {alunos[i]}")

