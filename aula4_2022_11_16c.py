#1° passo: importar biblioteca

import sqlite3

#passo 2 e 3 virarão função conectar()

def conectar():
#2° passo: estabelecer conexão com banco de dados
  conexao = sqlite3.connect("dc_universe.db")

#3° passo: criar objeto do tipo cursor
  cursor = conexao.cursor()

  return conexao, cursor
