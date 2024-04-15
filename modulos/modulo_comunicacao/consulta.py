from modulo_interface import Mensagem
from modulo_interface import Mensagem
from modulo_traducao import Traduz
from modulo_comunicacao import Conexao
from modulo_admin import bd


class Consulta():

    def realizar_consulta():
        c = Conexao()
        t = Traduz()

        # print("Banco de dados cadastrados")
        bd.listar_bd()
        id_bd = int(input("Digite o id do banco de dados:\n"))
        
        consulta = input("Digite sua consulta em linguagem natural:\n")

        mensagem = Mensagem(consulta[0:-1])
            
        if(id_bd==1):
            try:
                mensagem.set_csql(t.ln2Sql(mensagem.get_consulta_nl()))
                resposta=(c.realiza_conexao(1, mensagem.get_csql()), "\n")
                return resposta
            
            except:
                print("Erro!")
            
        if(id_bd==2):
            try:
                mensagem.set_csql(t.ln2Sql(mensagem.get_consulta_nl()))
                mensagem.set_cnosql(t.sqlToMongo(mensagem.get_csql()))
                resposta=(c.realiza_conexao(2, mensagem.get_cnosql()), "\n")
                return resposta
                        
            except:
                print("Erro!")
