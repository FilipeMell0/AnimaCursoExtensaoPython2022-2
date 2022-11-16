#1° passo: importar biblioteca

import sqlite3

#2° passo: estabelecer conexão com banco de dados

conexao = sqlite3.connect("dc_universe.db")

#3° passo: criar objeto do tipo cursor

cursor = conexao.cursor()

#4º passo: comando sql do banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#5º passo: executar o comando sql no comando sqlite (cursor)

cursor.execute(sql)

#6º passo: exibir o nome de todos heróis e vilões do banco de dados

pessoas = cursor.fetchall()

for pessoa in pessoas:
  print(pessoa)

for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} ({pessoa[3]})\n")