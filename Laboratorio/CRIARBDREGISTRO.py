import sqlite3 

""" Criando Conexão """
try:
    conn = sqlite3.connect('cadastro_professor.db') #nome do banco de dados
    print("Conexão realizada com sucesso! ")
except sqlite3.Error as e:
    print("Erro ao conectar com banco de dados: ", e)


try:
    with conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS registro(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario TEXT,
                    email TEXT,
                    senha TEXT


                    
        ) """)

        print("TABELA REGISTROS CRIADA COM SUCESSO")

except sqlite3.Error as e:
    print("ERRO AO CRIAR TABELA REGISTROS ", e)


