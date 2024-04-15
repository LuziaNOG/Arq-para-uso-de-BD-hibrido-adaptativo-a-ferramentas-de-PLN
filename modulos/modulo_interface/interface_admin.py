import sys
sys.path.append('../modulos')
from modulo_comunicacao import Consulta
from modulo_admin import user 
from modulo_admin import bd

class InferfaceAdmin():
    
    def mostrar_opcoes():
        print("Seja bem-vindo ADM")
        op=0

        while(op<3):
            op=int(input("1-Entra no menu dos Usuario, 2- Entra no menu dos bancos de dados 3- Realizar consultas 4- Sair :\n"))
            if(op==1):
                user.mostrar_opcoes()
            elif(op==2):
                bd.mostrar_opcoes()
            elif(op==3):
                print(Consulta.realizar_consulta())
            elif(op==4):
                print("Inté!\n")
                exit(0)
                