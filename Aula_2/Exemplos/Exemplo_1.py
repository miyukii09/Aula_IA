nota1 = float(input("Digite a preira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2
print("A média é", media)

if media >= 6:
    print("Aluno aprovado")
elif media >= 2:
    print("Aluno esta de exame")
else:
    print("Aulo reptovado")