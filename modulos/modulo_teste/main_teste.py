from ast import Try
import time
from modulo_interface import Mensagem
from modulo_traducao import Traduz
from modulo_comunicacao import Conexao
import modulo_comunicacao as c
import numpy as np

time_exec_carga = []
time_trad_carga = []
time_exec_mysql = []
time_exec_mongo = []

# Gera tempos aleatórios para testes com mais de uma consulta
def gerador_poisson():
    s = np.random.poisson(75,9)
    #print("Vetor de poisson:", s)
    return s

def realizar_consulta():
    c = Conexao()
    t = Traduz()
    total_trad_mysql=0
    total_trad_mongodb=0
    
    #bloco Mysql
    with open('Entradas.txt', 'r') as consultasNL:
        consultas = consultasNL.readlines()

    vetor_time = gerador_poisson() 
    p=0
    
    for consulta in consultas:
        mensagem = Mensagem(consulta[0:-2])
        
        try:
            #inicio_exec_mysql = time.time()
            #inicio_trad_mysql = time.time()  
            mensagem.set_csql(t.ln2Sql(mensagem.get_consulta_nl()))
            #fim_trad_mysql = time.time()
            #print("Consultas em SQL:", mensagem.get_csql())
            print(c.realiza_conexao(1, mensagem.get_csql()), "\n")
            #fim_exec_mysql = time.time()
            
            time.sleep(vetor_time[p])
            p=p+1
        except:
            print("Fim carga mysql")
            
        #total_trad_mysql=total_trad_mysql+(fim_trad_mysql-inicio_trad_mysql)
        #time_exec_mysql.append(fim_exec_mysql - inicio_exec_mysql)
        
        
    #bloco MongoDB
    with open('Entradas.txt', 'r') as consultasNL:
        consultas = consultasNL.readlines()
    
    vetor_time = gerador_poisson()
    p=0

    for consulta in consultas:
        mensagem = Mensagem(consulta[0:-2])    
        
        try:
            #inicio_exec_mongodb = time.time()
            #inicio_trad_mongodb = time.time()
            mensagem.set_csql(t.ln2Sql(mensagem.get_consulta_nl()))
            mensagem.set_cnosql(t.sqlToMongo(mensagem.get_csql()))
            #fim_trad_mongodb = time.time()
            #print("Consultas em Linguagem MongoDB:", mensagem.get_cnosql)
            print(c.realiza_conexao(2, mensagem.get_cnosql()), "\n")
            #fim_exec_mongodb = time.time()
            time.sleep(vetor_time[p])
            p=p+1
        
        except:
            print("Fim carga mongoDB")
            
        #total_trad_mongodb=total_trad_mongodb+(fim_trad_mongodb-inicio_trad_mongodb)
        #time_exec_mongo.append(fim_exec_mongodb - inicio_exec_mongodb)
        
    #print("tempo de tradução mysql da carga: ", total_trad_mysql)
    #print("tempo de tradução mongodb da carga: ", total_trad_mongodb)    
    #time_trad_carga.append(total_trad_mysql+total_trad_mongodb) # Vetor com os tempos totais de traducao de carga

def main():
    print("#################### Executando ####################")
    inicio_exec = time.time()  # Inicio do tempo de execução completo da carga
    realizar_consulta()
    fim_exec = time.time()  # Fim do tempo de execução completo da carga
    time_exec_carga.append(fim_exec-inicio_exec) # Vetor com os tempos totais de execucao de carga
    
    
    # Ativar caso deseje ver os tempo de execução das consultas
    '''
    print("Tempo de execução da carga:")
    print(time_exec_carga)

    print("Tempo de tradução da carga:")
    print(time_trad_carga)
        
    print("Tempo de execução do banco mysql:")
    print(sum(time_exec_mysql))

    print("Tempo de execução do banco mongodb:")
    print(sum(time_exec_mongo))
    '''
    
    time_exec_carga.clear()
    time_exec_mysql.clear()
    time_exec_mongo.clear()
    time_trad_carga.clear()
        
if __name__ == "__main__":
    main()
