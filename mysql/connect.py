import pymysql
print("teste")

aServidor = "localhost"
aUsuario  = "root"
aSenha    = "root"
aBanco    = "universidade"
db = pymysql.connect(aServidor, aUsuario, aSenha, aBanco)
cursor = db.cursor(pymysql.cursors.DictCursor) # RETORNA OS RESULTADOS EM FORMA DE DICIONÁRIO
# EXECUTA CONSULTAS MYSQL
def Executa_SQL(pSQL):
  try:
    cursor.execute(pSQL)
    db.commit()
  except:
    print("Erro: Não foi possível executar o SQL")
    db.rollback()

def Busca_SQL(pSQL):
  try:
    cursor.execute(pSQL)
    results = cursor.fetchall()
    return results
  except:
    print("Erro: Não foi possível buscar os dados")
    return 0

vSQL = "CREATE TABLE IF NOT EXISTS usuario (NOME VARCHAR(50) NOT NULL, LOGIN VARCHAR(20), SENHA VARCHAR(20) )"
Executa_SQL(vSQL)

Executa_SQL("INSERT INTO USUARIO(NOME, LOGIN, SENHA) VALUES ('Maria da Silva', 'Maria', 'maria')")

resultado = Busca_SQL("SELECT * FROM usuario Where 1")

for row in resultado:
    print(row)
