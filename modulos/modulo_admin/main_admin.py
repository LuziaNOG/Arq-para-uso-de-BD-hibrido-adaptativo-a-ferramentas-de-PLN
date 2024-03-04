from user import menu_user
from bd import menu_bd

print("Seja bem-vindo ADM")
op=0

while(op<3):
    op=int(input("1-Entra no menu dos Usuario, 2- Entra no menu dos bancos de dados 3- Sair :\n"))
    if(op==1):
        menu_user()
    elif(op==2):
        menu_bd()
    elif(op==3):
        print("See you later!\n")