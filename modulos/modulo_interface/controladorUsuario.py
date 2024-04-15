import sqlite3
from modulo_interface.interface_usuario import InferfaceUsuario
from modulo_interface.interface_admin import InferfaceAdmin

class ControladorUsuario:
    def __init__(self):
        self.conexao = sqlite3.connect('usuarios.db')  # Conexão com o banco de dados
        self.cursor = self.conexao.cursor()
        
    def validar_usuario(self, username, senha):
        # Verifica se o usuário existe no banco de dados e se a senha está correta
        self.cursor.execute("SELECT * FROM USUARIOS WHERE username=? AND senha=?", (username, senha))
        usuario = self.cursor.fetchone()
        if usuario:
            print("Login bem-sucedido!")
            return usuario[2]  # Retorna o tipo de usuário (admin ou comum)
        else:
            print("Nome de usuário ou senha incorretos.")
            return None
    
    def abrir_tela(self, tipo_usuario):
        tipo_usuario = int(tipo_usuario)
        if(tipo_usuario==1):
            InferfaceUsuario.mostrar_opcoes()
        elif(tipo_usuario==2):
            InferfaceAdmin.mostrar_opcoes()
        