"""
- PARA ABRIR UM ARQUIVO arquivo = open(nomedoarquivo.txt,modo)
- O MODO PODE SER (r,a,w,a+,w+,r+)
- PARA LER O CONTEÚDO DE UM ARQUIVO PODEMOS USAR AS FUNÇÕES:
read() - lê o arquivo inteiro
readline() - lê uma linha do arquivo
readlines() - lê o conteúdo inteiro arquivo e retorna em um array de strings
"""
meuArquivo = open("arquivo.txt","a")
meuArquivo.write("Testando inserção\n")
meuArquivo.close()
meuArquivo=  open("arquivo.txt","r")
linhas = meuArquivo.readlines()
for linha in linhas:
    print(linha)
meuArquivo.close()