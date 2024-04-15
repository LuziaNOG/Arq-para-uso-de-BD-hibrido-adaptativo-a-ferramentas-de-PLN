import code
import json
from json.tool import main
from pathlib import Path
import sqlite3
#import io, os

# criando a conexão
conexao = sqlite3.connect('BD.db')
cursor = conexao.cursor()

def cadastrar_bd():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bd(
            id INTEGER PRIMARY KEY,
            tipo INTEGER NOT NULL,
            nome_bd VARCHAR(60) NOT NULL
        );
     """)

    print("Cadastro de novo Banco de Dados:\n")
    id = input("Digite o id do BD :\n")
    tipo = input("Digite o tipo de BD (1- SQL e 2- NoSQL):\n")
    while tipo not in ['1', '2']:
        print("Tipo de banco de dados inválido. Por favor, insira 1 para SQL ou 2 para NoSQL.")
        tipo = input("Digite o tipo de BD (1- SQL e 2- NoSQL):\n")
    
    nome_bd = input("Digite o nome do banco:\n")

    cursor.execute("""
        INSERT INTO bd(id, tipo, nome_bd)
        VALUES(?,?,?)""",
                       (id,tipo, nome_bd)
                       )

    conexao.commit()
    print("Banco cadastrado com sucesso\n")
    
def listar_bd():
    cursor.execute("""
        SELECT * FROM bd;
     """)

    print("Bancos de dados cadastrados\n")
    for linha in cursor.fetchall():
        print(linha)
    return 0

def atualizar_cadastro():
    print("Atualizando cadastro dos bancos de dados\n")
    listar_bd()
    id_atualizar = input("Digite o id do banco que deseja atualizar:\n")
    tipo = input("Tipo: 1-SQL, 2-NoSQL\n")
    while tipo not in ['1', '2']:
        print("Tipo de banco de dados inválido. Por favor, insira 1 para SQL ou 2 para NoSQL.")
        tipo = input("Tipo: 1-SQL, 2-NoSQL\n")
    
    nome_bd  = input("Digite o nome do banco:\n")

    cursor.execute("""
        UPDATE bd
        SET tipo=?, nome_bd=?
        WHERE id =? """, (tipo, nome_bd, id_atualizar)
    )

    conexao.commit()
    print("Banco de Dados Atualizado!")

def deletar_bd():
    print("Deletando cadastro de banco de dados\n")
    listar_bd()
    id_del = input("Digite o id do banco de dados que deseja deletar\n")
    
    cursor.execute("""
        DELETE FROM bd
        WHERE id=?""",(id_del,)
    )

    conexao.commit()
    print("Banco de dados deletado!")


def mostrar_opcoes():
    print("Digite uma opção:\n")
    op = input("1-Cadastrar um banco de dado, 2-Listar os banco de dados, 3-Atualizar um bancos de bados, 4- deletar um bancos de dados, 0 -sair\n")

    if(op == "1"):
        cadastrar_bd()
    elif(op == "2"):
        listar_bd()
    elif(op == "3"):
        atualizar_cadastro()
    elif(op == "4"):
        deletar_bd()
    elif(op == "0"):
        print("xau xau")
        conexao.close()
    else:
        print("Opção invalida")


if __name__ == "__main__":
    mostrar_opcoes()