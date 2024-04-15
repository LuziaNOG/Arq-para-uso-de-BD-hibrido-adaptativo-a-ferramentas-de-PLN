from modulo_interface.controladorUsuario import ControladorUsuario


class InterfaceLogin():
    def login_usuario(self):
        c = ControladorUsuario()
        username=input("Digite o username:\n")
        senha=input("Digite sua senha:\n")

        tipo_usuario=c.validar_usuario(username,senha)
        if(tipo_usuario!=None):
            c.abrir_tela(tipo_usuario)
        else:
            print("Usuário não encontrado, enrtre em contato com o administrador para realizar o cadastro!")