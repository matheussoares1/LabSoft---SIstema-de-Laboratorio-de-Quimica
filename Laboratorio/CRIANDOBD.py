""" Crindo Banco de Dados """
import sqlite3

""" Criando Conexão """
try:
    conn = sqlite3.connect('cadastro_quimica.db') #nome do banco de dados
    print("Conexão realizada com sucesso! ")
except sqlite3.Error as e:
    print("Erro ao conectar com banco de dados: ", e)



#Criando tabela de Vidrarias

try:
    with conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS vidrarias(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    quantidade INT,
                    capacidade REAL,
                    uni_medida TEXT,
                    descricao TEXT,
                    cuidados TEXT

                    
        ) """)

        print("TABELA VIDRARIAS CRIADA COM SUCESSO")

except sqlite3.Error as e:
    print("ERRO AO CRIAR TABELA VIDRARIAS ", e)

    #Criando tabela de Vidrarias

try:
    with conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS reagentes(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    quantidade INT,
                    composicao TEXT,
                    massa TEXT,
                    descricao TEXT,
                    cuidados TEXT

                    
        ) """)

        print("TABELA REAGENTES CRIADA COM SUCESSO")

except sqlite3.Error as e:
    print("ERRO AO CRIAR TABELA REAGENTES ", e)


try:
    with conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS maquinas(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    quantidade INT,
                    descricao TEXT,
                    instrucoes TEXT,
                    restricoes TEXT,
                    situacao TEXT,
                    cuidados TEXT

                    
        ) """)

        print("TABELA MAQUINAS CRIADA COM SUCESSO")

except sqlite3.Error as e:
    print("ERRO AO CRIAR TABELA MAQUINAS ", e)


try:
    with conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS epis(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    quantidade INT,
                    descricao TEXT,
                    instrucoes TEXT,
                    cuidados TEXT

                    
        ) """)

        print("TABELA EPIS CRIADA COM SUCESSO")

except sqlite3.Error as e:
    print("ERRO AO CRIAR TABELA EPIS ", e)