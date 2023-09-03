import sqlite3 as lite

""" Criando Conexão """
try:
    conn = lite.connect('cadastro_quimica.db') #nome do banco de dados
    print("Conexão realizada com sucesso! ")
except lite.Error as e:
    print("Erro ao conectar com banco de dados: ", e)

"""Tabela de VIDRARIAS--------------------------------------------"""
#Inserir VIDRARIAS

def inserir_vidrarias(i):
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO vidrarias (nome, quantidade, capacidade, uni_medida, descricao, cuidados) VALUES (?,?,?,?,?,?)" 

        cur.execute(query, i)

#inserir_vidrarias(['Becker', '2', '100','ml','teste descricao', 'oia o bicho quente rapaz'])

def ver_vidrarias():
    lista = []
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM vidrarias')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista
#print(ver_vidrarias())

def atualizar_vidrarias(i):
    with conn:
        cur = conn.cursor()
        query = "UPDATE vidrarias SET nome=?, quantidade=?, capacidade=?, uni_medida=?, descricao=?, cuidados=? WHERE id=?"

        cur.execute(query, i)
l = ['Funil', '2', '100','ml','teste descricao', 'oia o bicho quente rapaz',1]
#atualizar_vidrarias(l)
#print(ver_vidrarias())

def deletar_vidrarias(i):
    with conn:
        cur = conn.cursor()
        query = "DELETE FROM vidrarias WHERE id=?"

        cur.execute(query, i)

#deletar_vidrarias([1])
#print(ver_vidrarias())


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////

"""Tabela de reagentes--------------------------------------------"""
#Inserir Reagentes


def inserir_reagentes(i):
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO reagentes (nome, quantidade, composicao, massa, descricao, cuidados) VALUES (?,?,?,?,?,?)" 

        cur.execute(query, i)

#inserir_reagentes(['Cloro', '3', 'Cl','100 g','teste descricao', 'oia o vai na piscina'])

def ver_reagentes():
    lista = []
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM reagentes')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista
#print(ver_reagentes())



def atualizar_reagentes(i):
    with conn:
        cur = conn.cursor()
        query = "UPDATE reagentes SET nome=?, quantidade=?, composicao=?, massa=?, descricao=?, cuidados=? WHERE id=?"

        cur.execute(query, i)
#d = ['Cloro', '2', 'Cl','100g','teste descricao', 'oia o bicho vai na piscina',1]
#atualizar_reagentes(d)
#print(ver_reagentes())

def deletar_reagentes(i):
    with conn:
        cur = conn.cursor()
        query = "DELETE FROM reagentes WHERE id=?"

        cur.execute(query, i)
#print(ver_reagentes())

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////

"""Tabela de reagentes--------------------------------------------"""
#Inserir Reagentes


def inserir_maquinas(i):
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO maquinas (nome, quantidade, descricao, instrucoes, restricoes, situacao, cuidados) VALUES (?,?,?,?,?,?,?)" 

        cur.execute(query, i)

#inserir_maquinas(['Capela', '1', 'teste descricao','teste instrucoes','teste restricoes', 'manutencao', 'Fechar corretamente'])

def ver_maquinas():
    lista = []
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM maquinas')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista
#print(ver_maquinas())


def atualizar_maquinas(i):
    with conn:
        cur = conn.cursor()
        query = "UPDATE maquinas SET nome=?, quantidade=?, descricao=?, instrucoes=?, restricoes=?, situacao=?, cuidados=? WHERE id=?"

        cur.execute(query, i)
d = ['Capela de Exaustao', '1', 'teste descricao','teste instrucoes','teste restricoes', 'manutencao', 'Fechar corretamente',1]
#atualizar_maquinas(d)
#print(ver_maquinas())

def deletar_maquinas(i):
    with conn:
        cur = conn.cursor()
        query = "DELETE FROM maquinas WHERE id=?"

        cur.execute(query, i)
#deletar_maquinas([1])
#print(ver_maquinas())

