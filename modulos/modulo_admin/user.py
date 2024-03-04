from json.tool import main
import sqlite3
import io

# criando a conexão
conexao = sqlite3.connect('usuarios.db')
cursor = conexao.cursor()

def cadastrar_usuario():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            matricula INTERGER NOT NULL PRIMARY KEY,
            nome varchar(40),
            tipo INTEGER NOT NULL,
            email TEXT NOT NULL,
            senha varchar(8)
        );
     """)

    print("Cadastro de novo usuario:\n")
    matricula = input("Digite a matricula do usuario:\n")
    nome = input("Digite o nome do usuario:\n")
    tipo = input("1-Usuario convencional, 2-Usuario Administrador\n")
    email = input("Digite o email do usuario:\n")
    senha = input("Digite a senha de acesso do usuario\n")

    cursor.execute("""
        INSERT INTO usuarios(matricula,nome,tipo,email,senha)
        VALUES(?,?,?,?,?)""",
                       (matricula, nome, tipo, email, senha)
                       )

    conexao.commit()
    print("Usuario cadastrado com sucesso\n")

    return 0

def listar_usuario():
    cursor.execute("""
        SELECT * FROM usuarios;
     """)

    print("Usuarios cadastrados\n")
    for linha in cursor.fetchall():
        print(linha)
    return 0

def atualizar_cadastro():
    print("Atualizando cadastro de usuario\n")
    matricula__atualizar = input("Digite a matricula do usuario que deseja atualizar:\n")
    nome = input("Digite o nome do usuario:\n")
    tipo = input("1-Usuario convencional, 2-Usuario Administrador\n")
    email = input("Digite o email do usuario:\n")
    senha = input("Digite a senha de acesso do usuario\n")

    cursor.execute("""
        UPDATE usuarios
        SET nome=?, tipo=?, email=?,senha=?
        WHERE matricula =? """, (nome, tipo, email, senha, matricula__atualizar)
    )

    conexao.commit()
    return 0

def deletar_usuario():
    print("Deletando cadastro de usuario\n")
    listar_usuario()
    matricula_del = input("Digite a matricula do usuario que deseja deletar\n")
    
    cursor.execute("""
        DELETE FROM usuarios
        WHERE matricula=?""",(matricula_del)
    )

    conexao.commit()
    print("Usuario deletado!")
    return 0

def backup_usuario():
    with io.open('usuarios_dump.sql', 'w') as f:
        for linha in conexao.iterdump():
            f.write('%s\n' % linha)
    print(" Backup realizado!")
    return 0

def menu_user():
    print("Digite uma opção:\n")
    op = input("1-Cadastrar, 2-Listar usuarios, 3-Atualizar usuarios, 4- Deletar usuarios, 5- Fazer backup, 0 -sair\n")

    if(op == "1"):
        cadastrar_usuario()
    elif(op == "2"):
        listar_usuario()
    elif(op == "3"):
        atualizar_cadastro()
    elif(op == "4"):
        deletar_usuario()
    elif(op == "5"):
        backup_usuario()
    elif(op == "0"):
        print("xau xau")
    else:
        print("Opção invalida")

    conexao.close()