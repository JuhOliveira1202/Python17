#Exercício 20:
#Escrva uma função num_divisores que recebe
#um n e devolve o número de divisores de n.
    #O programa deverá correr sempre até o utilizador
    # introduzir o número 9999


def num_divisores(num):
    x = 1
    for i in range(1, num//2+1):
        if num % i == 0:
            x += 1
        return x

x = int(input("Introduza um nº inteiro: "))
while True:
    if x == 9999:
        break
    print("Número de divisões: ", num_divisores(x))
    x = int(input("Introduzir um nº inteiro: "))


    
   




