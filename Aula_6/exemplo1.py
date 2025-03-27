# o def e a palava separada para as funcoes
def boasVindas(nome):
    print( f"olá {nome} seja bem vindo!")

def olaMundo():
    print("olá mundo!")

# vc pode usar ele com um vetor tbm, sendo declarado da seginte forma
def boasVindas2(alunos):
    for aluno in alunos:
        print(f"olá {aluno} seja bem vindo!")

print("aula 06")
boasVindas("yuki")
boasVindas(27)
olaMundo()
boasVindas2(["Felipe","Julia","Ligia","Jose","Matheis"])