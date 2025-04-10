arquivo = open("aula.txt","w")

nome = input(f"Digite o nome do aluno: ")
arquivo.write(f"Nome: {nome}\n")

nota1 = input(f"Digite a primeira nota do aluno {nome}: ")
arquivo.write(f"A primera nota e de {nota1}\n")

nota2 = input(f"Digite a segunda nota do aluno {nome}: ")
arquivo.write(f"A segunda nota e de {nota2}\n")

arquivo.write(f"com a media de {(int(nota1)+int(nota2)/2)}")

arquivo.close()
print("arquivo gerado com sucesso!")