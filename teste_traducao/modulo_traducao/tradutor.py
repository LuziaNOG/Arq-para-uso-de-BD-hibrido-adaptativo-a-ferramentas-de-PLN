import subprocess

class Traduz:
    def ln2Sql(self, frase) -> str:
        c = "python -m ln2sql.main -d database_store/school.sql -l lang_store/english.csv -j output.json -i"
        l = c.split(" ")
        l.append(frase)
        resposta = subprocess.run(l, capture_output=True, text=True, cwd="modulo_traducao")
        return resposta.stdout.replace("\n", " ")[1:]

    def sqlToMongo(self, frase) -> str:
        c = "java -jar sqlToMongo/target/sql-to-mongo-db-query-converter-1.21-SNAPSHOT-standalone.jar -sql"
        l = c.split(" ")
        l.append(frase)
        resposta = subprocess.run(l, capture_output=True, text=True, cwd="modulo_traducao")
        return resposta.stdout.replace("\n", "")[27:].replace(" ", "")

