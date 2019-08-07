nome = "danilo lima\n"

print(nome[0:3])

"""
 string = 'string'
 string[a:b] retorna uma substring que inicia em a e tem tamanho b

"""
print(nome.lower())
print(nome.upper())
print(nome.strip()) #retira espaços e caractéres especiais do final da string
print(nome)

print(nome.split("l"))

print(nome.find("l")) # retorna em que posição começa a string pesquisada

print(nome.replace("lima","silva"))