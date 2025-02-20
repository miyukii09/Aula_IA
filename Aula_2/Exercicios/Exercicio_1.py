Numeros =[30, 4, 90 , 70, 2, 6, 9, 10 , 19]
maior = 0
menor = 0

for numero in Numeros:
    if numero >= 10:
        maior = maior+1
    else:
        menor = menor+1 
print("tem", maior,"numeros que sao maiores que 10")
print("tem", menor,"numeros que sao menores que 10")