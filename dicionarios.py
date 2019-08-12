# meu_dicionario.items() RETORNA OS ITENS DE UM DICIONARIO EM FORMA DE TUPLA
# meu_dicionario.values() RETORNA APENAS OS VALORES
# meu_dicionario.keys() RETORNA AS CHAVES

meu_dicionario = {"a":"abacate","b":"banana","c":"caju","e":"espinafre"}

for chave in meu_dicionario:
    print(meu_dicionario[chave])

for i in meu_dicionario.items():
    print(i)

for valor in meu_dicionario.values():
    print(valor)

for chave in meu_dicionario.keys():
    print(chave)