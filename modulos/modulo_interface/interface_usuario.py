import sys
sys.path.append('../modulos')
from modulo_comunicacao import Consulta


class InferfaceUsuario():
    
    def mostrar_opcoes():    
        print("Seja bem-vindo Usuário")
        op=0

        while(op<3):
            op=int(input("Digite sua opção: 1-Realizar consulta, 2-Sair :\n"))
            if(op==1):
                Consulta.realizar_consulta()
            elif(op==2):
                print("Inté!\n")
                exit(0)
