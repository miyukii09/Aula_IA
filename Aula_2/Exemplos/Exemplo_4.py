soma = 0 

# nesse exemplo estamos fazendo o for perguntar a nota do aluno 5 vezes, e fazer a conta a soma das notas
for i in range(5):
    nota = float(input("Digite a nota " + str(i+1) + " " ))
    soma = soma + nota
# e agora ele pega a soma da nota e divide por 5 fazendo a media
media = soma /5
print("A nota do aluno é", media)