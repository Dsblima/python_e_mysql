# ADICIONAR ELEMENTO À LISTA lista.append()
# REMOVER ELEMENTOS DA LISTA del lista[comeco:fim]
# ORDENAR LISTA lista.sort() ORDENA A PRÓPRIA LISTA, SEM RETORNAR QUALQUER VALOR
# ORDENAR LISTA sorted(lista) ORDENA A LISTA, E RETORNA, NÃO ALTERANDO A LISTA QUE CHAMOU O MÉTODO
# ORDENAR EM ORDEM DECRESCENTE lista.sort(reverse=True)
# INVERTE A ORDEM DOS ELEMENTOS lista.reverse()
lista1 = ["abacaxi","acerola","maçã","açai", "laranja", "jaca"]
print(lista1)
lista1.append("manga")
print(lista1)
del lista1[0:2]
print(lista1)
lista2 = sorted(lista1)

print(lista1)
print(lista2)