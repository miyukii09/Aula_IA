notas_aula = []

def Medias(n1, n2):
    medias = (int(n1) + int(n2)) / 2
    return medias

def clasificacao(media):
    if media <= 5:
        estado = "Reprovado"
    elif media >= 6 and media <=7:
        estado = "Na media"
    else:
        estado = "Aprovado"
    return estado

def Alunos(vetor):
    nome = []
    n1   = []
    n2   = []
    
    for i in range(0, len(vetor), 3):
        nome.append(vetor[i])
        n1.append(vetor[i+1])
        n2.append(vetor[i+2])

    for i in range(len(nome)):
        medias = Medias(n1[i], n2[i])
        estado =clasificacao(medias)
        print(f"Nome: {nome[i]} Nota 1: {n1[i]} Nota 2: {n2[i]} Média: {medias:.2f} {estado}")

for i in range(2):  
    nome = input(f"Digite o nome do aluno {i+1}: ")
    notas_aula.append(nome)
    n1 = input(f"Digite a primeira nota do aluno {i+1}: ")
    notas_aula.append(n1)
    n2 = input(f"Digite a segunda nota do aluno {i+1}: ")
    notas_aula.append(n2)
    
print(notas_aula)
Alunos(notas_aula)
