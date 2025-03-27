# nesse exemplo vamos carregar uma matriz
def carregaAlunosNotas():
    alunos = []
    notas  = []

    # vamos pegar os dados para o vetor usando um for, ja armazenando dentro dos dois vetores
    for i in range(5):
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))
        print()

        alunos.append(nome)
        notas.append(nota)

    # vamos salvar os resultados    
    resultado = []
    resultado.append(alunos)
    resultado.append(notas)

    # vamos terornar os resultados
    return resultado

def nomeAlunoMaiorNota(matriz):
    alunos = matriz[0]
    notas  = matriz[1]
    
    aluno = alunos [0]
    nota  = notas [0]

    for i in range(5):
        if  notas[i] > nota:
            nota = notas[i]
            aluno = alunos[i]
    return (aluno , nota)


# vamos chamar a funcao para textar
print("Exemplo 2")

matriz = carregaAlunosNotas() 
print ( nomeAlunoMaiorNota(matriz))