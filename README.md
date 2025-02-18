# Arquitetura para uso de banco de dados híbrido adaptativo a ferramentas de suporte a consultas em linguagem natural
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

**O fluxo de execução é o seguinte:**
O primeiro passo é realizar o login no sistemas através da **interface de login**. Inicialmente o sistema conta com dois usuários: um usuário administrador com username "admin" e senha "12345" e um usuário convencional com username "user1" e senha "12345". A **interface de login** envia ao **controlador de usuário** os dados de acesso recebidos para que o controlador valide o login. Após validar o login e verificar o tipo de usuario, o controlador chama a **interface admin** para usuários administradores, e a **interface usuários**, para usuários convencionais. 
Através da **interface admin** o administrador pode cadastrar, listar, atualizar e deletar bancos de dados ou usuários. Os dados cadastrados dos bancos de dados e dos usuários são salvos em um banco de dados relacional SQLite. O administrador também pode realizar consultas. Ao optar por realizar uma consultas, a classe **consulta** é invocada, essa classe cria um objeto **mensagem** para guardar todas as informações, como a consulta em linguagem natural (informada pelo usuário), a tradução para uma consulta em SQL e/ou a tradução para uma consulta em mongoDB, além da resposta da consulta. A classe **consulta** também invoca a classe **tradução**, que realiza as traduções utilizando as ferramentas e retorna a consulta em SQL e mongoDB, que são salvos em **mensagem**. Com as consultas traduzidas, a classe **consulta** invoca a classe **conexão**, que estabelese a comunicação com o banco de dados que foi escolhido pelo usuário, envia a consulta na linguaguem correspondete a linguagem do banco de dados e retorna a resposta que é salva em **mensagem** e que será enviada para o usuário. 
O usuário convencional tem acesso a **interface de usuário**,e pode realizar consulta, porém não pode cadastrar, listar, atualizar e deletar bancos de dados ou usuários.

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
