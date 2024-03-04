import sys

class Mensagem:
    csql = ""
    cnosql = ""

    def __init__(self, consultaNL):
        self.consulta_nl = consultaNL
        self.resposta = ""
        
    def get_id(self):
        return self.id

    def get_consulta_nl(self):
        return self.consulta_nl
    
    def get_resposta(self):
        return self.resposta

    def set_resposta(self, resposta):
        self.resposta = resposta

    def set_csql(self, csql):
        self.csql = csql

    def get_csql(self):
        return self.csql

    def set_cnosql(self, cnosql):
        self.cnosql = cnosql

    def get_cnosql(self):
        return self.cnosql
    
    def __str__(self):
        txt = 'Consulta em linguagem Natural: ' + self.get_consulta_nl()
        txt += '\nConsulta em SQL: ' + self.get_csql()
        txt += '\nConsulta em NoSQL: ' + self.get_cnosql()
        return txt