lista1 = [1,2,3,4,5,6]
lista2 = ["a","b","c","d"]

x = 0

#ESTRUTURA WHILE
while x < len(lista1):
    print(lista1[x])
    x += 2

#O COMANDO ABAIXO SIGNIFICA PARA CADA ELEMENTO I NA LISTA2 PRINT I
for i in lista2:
    print(i)

"""FUNÇÃO RANGE RETORNA UMA LISTA
range(b) retorna uma lista com b elementos, sendo zero o primeiro valor

range(a,b) retorna uma lista que inicia em a e termina em b-1

range(a,b,c) retorna uma lista que começa em a, termina em b-1 e possui c como diferença entre um elemento e o subsequente 

"""

for i in range(10,20,2):
    print(i)