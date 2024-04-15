import socketserver
import mysql.connector
from pymongo import MongoClient
import re, json

class Conexao:
    #tipo 1 SQL e 2 NoSQL
    def realiza_conexao(self, tipo_bd, consulta):
        if(tipo_bd==1):
            print("Acessando banco relacional, resposta:")
            resp=self.realizar_conexao_mysqlBD(consulta)
        else:
            print("Acessando banco não relacional, resposta:")
            resp=self.realizar_conexao_mongoBD(consulta)

        return resp


    def realizar_conexao_mysqlBD(self, consulta):
        conexao = mysql.connector.connect(
        host='localhost', port='3306', database='school', user='root', password='Password@123')

        cursor = conexao.cursor()
        cursor.execute(consulta)
        resultado = cursor.fetchall()

        cursor.close()
        conexao.close()
        return resultado
        

    def realizar_conexao_mongoBD(self,consulta):
        arrayData = consulta.split(".")
        col = arrayData[1] #pega a collection
        s1 = consulta.replace("\n", "").replace(" ", "") #retira execesso de espaços
        tipo = arrayData[2].split("(")[0] #pega o tipo da consulta
        data = re.findall("\[.*\]", s1)[0] #pega os arqgumentos
        data2 = data.replace(str(col)+".","")
        myclient = MongoClient("mongodb://localhost:27017/", socketTimeoutMS=1800000, waitQueueTimeoutMS= 1800000, connectTimeoutMS=1800000, serverSelectionTimeoutMS=1800000) 
        
        db = myclient["school"] 
        collection = db[col]
        consulta = getattr(collection, tipo)
        cursor = consulta(json.loads(data2))
        return list(cursor)
    
if __name__ == "__main__":
    con = Conexao()
    #con.realizar_conexao_mysqlBD('''SELECT AVG(SchoolRecords.present) FROM SchoolRecords;''')
    resp = con.realizar_conexao_mongoBD('''db.SchoolRecords.aggregate([{"$group":{"_id":{},"sum_SchoolRecords_absented":{"$sum":"$absented"}}},{"$project":{"sum_SchoolRecords_absented":1,"_id":0}}])''')
    print(resp)
    #con.realizar_conexao_mongoBD('''db.school.aggregate([{"$group":{"_id":{},"max_school_absented":{"$max":"$absented"}}},{"$project":{"max_school_absented":1,"_id":0}}])''')
