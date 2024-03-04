import code
import json
from json.tool import main
from pathlib import Path
import sqlite3
import io, os

# criando a conexão
conexao = sqlite3.connect('BD.db')
cursor = conexao.cursor()

def cadastrar_bd():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bd(
            id INTERGER NOT NULL PRIMARY KEY,
            tipo INTEGER NOT NULL,
            path varchar(60) NOT NULL
        );
     """)

    print("Cadastro de novo Banco de Dados:\n")
    id = input("Digite o id do BD:\n") # Atualizar para auto incremento
    tipo = input("Digite o tipo de BD (1- SQL e 2- NoSQL):\n")
    path = input("Digite a string de acesso:\n")

    cursor.execute("""
        INSERT INTO bd(id,tipo,path)
        VALUES(?,?,?)""",
                       (id, tipo, path)
                       )

    conexao.commit()
    print("Banco cadastrado com sucesso\n")

    return 0

def listar_bd():
    cursor.execute("""
        SELECT * FROM bd;
     """)

    print("Bancos de dados cadastrados\n")
    for linha in cursor.fetchall():
        print(linha)
    return 0

def gerar_json():
    cursor.execute("""
        SELECT * FROM bd;
     """)
    with open('backup_bd.json', 'w+') as f:
        for linha in cursor.fetchall():
            json.dumps(linha)
            #f.write(';\n')
    return 0

def atualizar_cadastro():
    print("Atualizando cadastro dos bancos de dados\n")
    listar_bd()
    id__atualizar = input("Digite o id do banco que deseja atualizar:\n")
    tipo = input("Tipo: 1-SQL, 2-NoSQL\n")
    path = input("Digite o link de acesso ao banco:\n")

    cursor.execute("""
        UPDATE bd
        SET tipo=?, path=?
        WHERE id =? """, (tipo, path, id__atualizar)
    )

    conexao.commit()
    print("Banco de Dados Atualizado!")
    return 0

def deletar_bd():
    print("Deletando cadastro de banco de dados\n")
    listar_bd()
    id_del = input("Digite o id do banco de dados que deseja deletar\n")
    
    cursor.execute("""
        DELETE FROM bd
        WHERE id=?""",(id_del)
    )

    conexao.commit()
    print("Bd deletado!")
    return 0

def backup_bd():
    with io.open('bd_dump.sql', 'w') as f:
        for linha in conexao.iterdump():
            f.write('%s\n' % linha)
    print("Backup realizado!")
    return 0

def menu_bd():
    print("Digite uma opção:\n")
    op = input("1-Cadastrar um banco de dado, 2-Listar os banco de dados, 3-Atualizar um bancos de bados, 4- deletar um bancos de dados, 5- Fazer backup, 6- gerar json, 0 -sair\n")

    if(op == "1"):
        cadastrar_bd()
    elif(op == "2"):
        listar_bd()
    elif(op == "3"):
        atualizar_cadastro()
    elif(op == "4"):
        deletar_bd()
    elif(op == "5"):
        backup_bd()
    elif(op == "6"):
        gerar_json()
    elif(op == "0"):
        print("xau xau")
        conexao.close()
    else:
        print("Opção invalida")