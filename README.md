# Modelo de arquitetura para uso de banco de dados hibridos adaptavel a ferramentas PLN
Esse projeto esta relacionado a uma dissertação de mestrado do PCOMP - UFC - Campus Quixadá.

O objetivo é propor um modelo de arquitetura capaz de possibilitar a usuários não especialistas extrair a partir de linguagem natural informações de base de dados homogêneas
ou heterogêneas, armazenadas em banco de dados híbridos, locais ou distribuídos. 
O modelo de arquitetura proposta gera transparência para o usuário através de um módulo de interface único para acesso a múltiplos bancos de dados por meio de consultas formuladas
em linguagem natural e suporta diferentes ferramentas de Processamento de Linguagem Natural (PLN) com poucas adaptações, pois foi projetado com módulos independentes com funcionalidades distintas.

A arquitetura segue o modelo cliente- servidor. O lado do servidor possui quatro módulos: i) Módulo de Interface de Usuário, ii) Módulo de Tradução, iii) Módulo de Comunicação e o iv) Módulo de Administração. O modelo pode ser observado na imagem a seguir.

<img src="/modelo_proposto.png">

**(i) Módulo de Interface com Usuário** é responsável pelos processos de autenticação do usuário, verificando quais são as ações de manipulação de dados permitidas e quais
conjuntos de dados podem ser manipulados. A interface desse módulo ainda não foi em implementação, as entradas são fornecidas por meio do arquivo entrada.txt, onde as consultas devem ser escritas no idioma inglês.

**ii) Módulo de tradução** é responsável pela tradução de consulta em linguagem natural para as linguagens formais utilizadas pelos bancos de dados implantados no ambiente. O Módulo de Tradução foi implementado servindo-se da ferramenta LN2SQL publicada em: https://github.com/FerreroJeremy/ln2sql para tradução das consultas em LN para linguagem SQL e a ferramenta SQL To MongoDB Query Converter, publica em : https://github.com/vincentrussell/sql-to-mongo-db-query-converter. 

**(iii) Módulo de comunicação** é responsável pela interação com os SGBDs implantados em ambientes virtualizados, como os clusters de computadores ou nuvens computacionais. O Módulo de Comunicação recebe a consulta traduzida pelo Módulo de Tradução e realiza o processo de execução da consulta. Após a execução da consulta, o Módulo de Comunicação recebe e encaminha os resultados do processamento da consulta para o Módulo de Interface com Usuário.

**(iv) Módulo de administração** é responsável pelo gerenciamento de todos os usuários e seus respectivos perfis. (Módulo em implementação)

## Diagrama de classes

Abaixo podemos observar o diagrama de classe do modelo proposto.
<img src="/diagrama_classes.png">


## Observações

**Configuração para conexão com os bancos de dados**
- Para adicionar ou configurar novos bancos de dados, altere o arquivo conexao.py ( path: modulo_comunicacao->conexao.py)
- Para bancos de dados relacionais altere ou informe os dados na linha: host='localhost', port='3306', database='school', user='root', password='Password@123')
- Ou duplique a função realizar_conexao_mysqlBD() renomeando com um novo nome, e adicione o novo banco.  

**Adição de novas ferramentas de PLN**
- Teste primeiramente a nova ferramenta na pasta teste_traducao.
- Crie uma nova pasta com o nome da ferramente no teste_traducao->modulo_traducao e no arquivo traduz.py defina uma função que consiga executar a ferramanta e retornar a consulta traduzida
  
**Adição de novos bancos de dados**
- Para a ferramenta LN2SQL realizar a tradução é necessário adicionar o esquema do banco, na pasta database_store ( path: modulo_traducao->ln2sql-> databases_store ).
- Para gerar o esquema, pode-se utilizar o phpmyadmin, no caso do banco de dados MySQL, através de http://localhost/phpmyadmin/ e exportar o banco (exporte somente a estrutura sem os dados, porque senão o arquivo vai ficar muito grande).
- Por enquanto, não há suporte para outros bancos de dados não relacionais, além do mongoDB.

**Execução**
- Utilize o python3 para executar a main: python3 modulos/main.py
