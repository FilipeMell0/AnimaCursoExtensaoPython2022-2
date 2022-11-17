#1° passo: importar biblioteca

import sqlite3

#2° passo: estabelecer conexão com banco de dados

conexao = sqlite3.connect("dc_universe.db")

#3° passo: criar objeto do tipo cursor

cursor = conexao.cursor()

#4º passo: comando para inserir herói/vilão


sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (13, 'Lex Luthor', 'Alexander Joseph Luthor', 'Vilã(o)')"


#5º passo: executar o comando sql 

print(cursor.execute(sql))

#6° passo: confirmar o INSERT com commit() e fechar o banco

conexao.commit()
conexao.close()