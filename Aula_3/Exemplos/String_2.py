print ("Exemplo 2")

nome  = "yukii"
idade = 19

# vc pode exibir uma mensagem de varias formas diferentes
# esse primero exemplo ele e a forma mais comun com vc mesmo formatando o testo
print("ola", nome,"voce tem",idade,"anos")

# esse segundo exemplo vc salva o seu testo em uma variavel e dps printa a variavel
frase = "ola", nome,"voce tem",str(idade),"anos"
print(frase)

# nesse ultimo exemplo vc salva um testo em uma variavel e vc formata as inf com o .format()
frase2 = "ola {} vc tem {} anos"
print(frase2.format(nome,idade))

# vc tbm pode usar o f-string
# dessa maneira, vc so tem que colocar o f antes de colocar seu testo
# fora que vc tem que setar os parametros dentro do proprio testo, e tbm nao tem que fazer a conversao, como no exemplo abaixo
frase3 = f"ola {nome} vc tem {idade} anos"
print(frase3)

# vc pode formatar usando o :.2f assim o numero, sempre sera formatado com 2 casa decinais
salario = 1500.1234
frase4 = f"o salario é {salario:.2f}"
print (frase4)