import sqlite3
import io

# criando a conexão
conexao = sqlite3.connect('usuarios.db')
cursor = conexao.cursor()

def cadastrar_usuario():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS USUARIOS(
            matricula INTEGER NOT NULL PRIMARY KEY,
            username varchar(40) NOT NULL,
            tipo INTEGER NOT NULL,
            senha varchar(8) NOT NULL
        );
     """)

    print("Cadastro de novo usuario:\n")
    matricula = input("Digite a matricula do usuario:\n")
    username = input("Digite o username do usuario:\n")
    tipo = input("1-Usuario convencional, 2-Usuario Administrador\n")
    senha = input("Digite a senha de acesso do usuario\n")

    cursor.execute("""
        INSERT INTO usuarios(matricula,username,tipo,senha)
        VALUES(?,?,?,?)""",
                       (matricula, username, tipo, senha)
                       )

    conexao.commit()
    print("Usuario cadastrado com sucesso\n")

    return 0

def listar_usuario():
    cursor.execute("""
        SELECT * FROM USUARIOS;
     """)

    print("Usuarios cadastrados\n")
    for linha in cursor.fetchall():
        print(linha)
    return 0

def atualizar_cadastro():
    print("Atualizando cadastro de usuário\n")
    matricula_atualizar = input("Digite a matrícula do usuário que deseja atualizar:\n")

    # Verificar se a matrícula existe
    cursor.execute("SELECT COUNT(*) FROM usuarios WHERE matricula = ?", (matricula_atualizar,))
    if cursor.fetchone()[0] == 0:
        print("Matrícula não encontrada. Nenhuma atualização realizada.")
        return 0

    username = input("Digite o novo username do usuário:\n")
    tipo = input("1-Usuário convencional, 2-Usuário Administrador\n")
    senha = input("Digite a nova senha de acesso do usuário (tamanho máximo 8):\n")

    cursor.execute("""
        UPDATE usuarios
        SET username=?, tipo=?, senha=?
        WHERE matricula =? """, (username, tipo, senha, matricula_atualizar))

    conexao.commit()
    print("Usuário atualizado com sucesso!")

def deletar_usuario():
    print("Deletando cadastro de usuário\n")
    listar_usuario()  # Se desejar listar os usuários antes de deletar
    matricula_del = input("Digite a matrícula do usuário que deseja deletar:\n")

    # Verificar se a matrícula existe
    cursor.execute("SELECT COUNT(*) FROM usuarios WHERE matricula = ?", (matricula_del,))
    if cursor.fetchone()[0] == 0:
        print("Matrícula não encontrada. Nenhum usuário deletado.")
        return 0

    cursor.execute("DELETE FROM usuarios WHERE matricula = ?", (matricula_del,))
    conexao.commit()
    print("Usuário deletado com sucesso!")


def mostrar_opcoes():
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
    elif(op == "0"):
        print("xau xau")
    else:
        print("Opção invalida")

    conexao.close()

if __name__ == "__main__":
    mostrar_opcoes()