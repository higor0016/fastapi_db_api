import sqlite3


#Conecta com banco de dados
con = sqlite3.connect("gameTemporario.db")

#Cria um novo cursor para fazer instruções (querys)
cur = con.cursor()


#CRIAÇÃO DE TABELA JOGADOR QUE DEVE CONTER:

# ID
# Nome do Aluno/Jogador
# Curso
# Nível
# XP
# Conquistas
#
#
#
cur.execute('''
             
    CREATE TABLE IF NOT EXISTS jogador(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT,
            Curso TEXT,
            Nivel INTEGER,
            XP INTEGER,
            Conquistas TEXT
    )
''')

con.commit()
con.close()