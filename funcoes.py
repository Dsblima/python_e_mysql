import random
"""
- GERAR NÚMERO ALEATÓRIOS 
import random
numero = random.randint(comeco,fim)

- SELECIONAR UM NÚMERO DE UMA LISTA
lista = [4,5,6,7,8]
lista.choice(lista)
"""
lista = [4,5,6,7,8]
def soma(x):
    numero = random.randint(0,100)
    print("Número gerado: ")
    print(numero)
    selecao = random.choice(lista)
    print("Número selecinado: ")
    print(selecao)
    return x+numero+selecao
print(soma(4))

