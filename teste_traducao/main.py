from ast import Try
import time
from modulo_interface import Mensagem
from modulo_traducao import Traduz

time_trad_carga = []

def realizar_traducao():
    total=0
    t = Traduz()
    
    with open('Entradas.txt', 'r') as consultasNL:
        consultas = consultasNL.readlines()

    for consulta in consultas:
        mensagem = Mensagem(consulta[0:-2]) # Retira os últimos dois caracteres

        inicio_trad = time.time()  # Inicio do tempo de traducao da consulta
        mensagem.set_csql(t.ln2Sql(mensagem.get_consulta_nl()))
        mensagem.set_cnosql(t.sqlToMongo(mensagem.get_csql()))
        fim_trad = time.time()  # Fim do tempo de traducao da consulta
        print(mensagem.__str__())    
            
        total=total+(fim_trad-inicio_trad) #Soma total do tempo de todas as traducoes da carga
    time_trad_carga.append(total) # Vetor com os tempos totais de traducao de carga

def main():
    
    realizar_traducao()

    print("Tempos de traduçao:")
    print(time_trad_carga)
    

if __name__ == "__main__":
    main()