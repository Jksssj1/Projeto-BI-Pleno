
Sobre a criação do código, segue algumas considerações:

Foi um desafio bem interessante onde eu pude relembrar algumas coisas praticas do Python e também aprender algumas novas.

O meu maior desafio foi no quesito de bibliotecas não estou acostumado a utilizar a biblioteca do mysql , algumas que eu utilizei em antigos projetos não estavam funcionando por que eu atualizei o Python.

Para a conexão e inserção de dados para o SQL foi a primeira vez que fiz, porém tive exito após pesquisar um pouco sobre as melhores praticas pra aplicar. 

Qualquer dúvida estou a disposição.

Lembrete (Para rodar a parte do SQL ele precisa do arquivo env na raiz do projeto ) 

--




1. **Criação do Ambiente Virtual**: Execute o comando para criar o ambiente virtual: `python -m venv venv`.

2. **Ativação do Ambiente Virtual**: Para **Windows**, use: `venv\Scripts\activate`. Para **Linux/macOS**, use: `source venv/bin/activate`.

3. **Instalação das Dependências**: Instale as dependências a partir do arquivo `requirements.txt` com o comando: `pip install -r requirements.txt`.

4. **Configuração do Arquivo `.env`**: coloque o arquivo `.env` na raiz do projeto, contendo as variáveis de ambiente necessárias. (não estou incluindo junto ao github por conta da sensibilidade dos dados, irei enviar por e-mail.)

5. **Criação das Tabelas no Banco de Dados** (Opcional): Execute o script de criação das tabelas no banco de dados com o comando: `python create_tables.py`.

6. **Execução do Script de Análise de Dados** (Opcional): Caso queira gerar o perfil dos dados, execute o script `profiling.py` com o comando: `python profiling.py`.

7. **Execução do Script Principal**: Execute o script principal que realiza o processamento dos dados com o comando: `python main.py`.

8. **Teste da Inserção de Dados**(Opcional): Execute o script de teste para verificar se os dados foram corretamente inseridos no banco de dados com o comando: `python test.py`.

--- abaixo como funciona.

---

O código começa com a importação das bibliotecas necessárias para o processamento de dados e a conexão com o banco de dados. As bibliotecas utilizadas são `pandas`, `os`, `dotenv`, `mysql.connector`, `hashlib` e `sqlalchemy`. O `pandas` é usado para manipulação de dados, enquanto o `mysql.connector` e `sqlalchemy` são utilizados para a conexão com o banco de dados MySQL. O `hashlib` é utilizado para gerar hashes MD5, e o `dotenv` carrega variáveis de ambiente a partir de um arquivo `.env`.

Em seguida, o arquivo `.env` é carregado usando o método `load_dotenv()`, que permite acessar as variáveis de ambiente para configurar a conexão com o banco de dados. As variáveis como `HOST`, `USER`, `PASSWORD`, `DATABASE` e `PORT` são lidas a partir do arquivo `.env` usando o método `getenv()`, que busca esses valores.

A conexão com o banco de dados é estabelecida através do `create_engine` da `sqlalchemy`, utilizando as credenciais carregadas das variáveis de ambiente para formar a URL de conexão com o MySQL.

Depois, o código carrega os dados de dois arquivos: `registro_oportunidades.json` e `sellout.parquet`. O arquivo JSON é carregado usando o `pandas.read_json()` e o arquivo Parquet é carregado com `pandas.read_parquet()`.

Em seguida, o código faz algumas transformações nos dados. Para o DataFrame `df_oportunidades`, ele gera identificadores únicos para cada parceiro e produto utilizando a função `hashlib.md5()`, que gera um hash MD5 dos valores das colunas `CNPJ Parceiro` e `Nome_Produto`. Esses valores são atribuídos às novas colunas `id_parceiro` e `id_produto`. Também converte a coluna `Data de Registro` para o formato de data com a função `pd.to_datetime()` e cria novas colunas como `quantidade` e `valor_total`, que são calculadas com base nas colunas existentes. A coluna `status` também é extraída diretamente do DataFrame. Em seguida, o DataFrame é filtrado para manter apenas as colunas essenciais e o resultado final é armazenado em `df_oportunidades_final`.

O mesmo processo de transformação é aplicado ao DataFrame `df_sellout`. Identificadores únicos são gerados para o parceiro e o produto, e a coluna `Data_Fatura` é convertida para o formato de data. Além disso, as colunas `quantidade` e `valor_total` são calculadas da mesma maneira. O DataFrame resultante é armazenado em `df_sellout_final`.

Após o processamento dos dados, os DataFrames `df_sellout_final` e `df_oportunidades_final` são salvos como arquivos Excel (`fato_sellout_final.xlsx` e `fato_oportunidades_final.xlsx`) usando o método `to_excel()`.

Por fim, o código tem a opção de enviar os dados para o banco de dados MySQL. Este trecho de código está comentado pois para rodar ele precisa do arquivo env na raiz do projeto, ele utiliza o método `to_sql()` para inserir os dados nas tabelas `fato_sellout` e `fato_registro_oportunidade` no banco de dados, caso o usuário deseje fazer isso.






