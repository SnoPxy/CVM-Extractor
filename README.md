📊 CVM EXTRATOR

O CVM EXTRATOR é um projeto pessoal desenvolvido com o objetivo de praticar programação, automação de dados e integração com banco de dados.
O sistema realiza automaticamente a coleta dos extratos de fundos de investimento disponibilizados pela CVM, faz o tratamento necessário e organiza as informações em um banco relacional (MySQL).

🚀 Funcionalidades

🔎 Web Scraping: identifica os arquivos de extratos diretamente no site da CVM.

⬇️ Download Automático: baixa o extrato desejado de acordo com o ano informado pelo usuário.

🛠 Tratamento de Dados: leitura com Pandas e padronização da estrutura, mesmo em casos de CSVs inconsistentes (ex.: ausência da coluna TP_FUNDO_CLASSE).

🗄 Banco de Dados Relacional: insere os dados tratados em uma tabela MySQL.

♻️ Atualização Automática: sempre que a CVM lançar um novo extrato, ele pode ser baixado e integrado.

🧹 Limpeza: remove o arquivo local após a inserção no banco, evitando acúmulo desnecessário.

⚙️ Tecnologias Utilizadas

Python 3

Pandas

BeautifulSoup (bs4)

Requests

Regex

MySQL (via conector)

OS / Sys

🏗 Estrutura do Projeto
CVM_EXTRATOR/
│
├── app.py                 # Script principal
├── conection.py           # Função para conectar ao banco de dados
├── README.md              # Documentação do projeto

📥 Como Utilizar

Clone o repositório:

git clone https://github.com/seu-usuario/CVM_EXTRATOR.git


Instale as dependências:

pip install pandas requests beautifulsoup4 mysql-connector-python


Configure o arquivo conection.py com suas credenciais do banco MySQL:

import mysql.connector

def conection_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="seu_usuario",
        password="sua_senha",
        database="extratos_cvm"
    )
    cursor = mydb.cursor()
    return cursor, mydb


Execute o script:

python app.py


Informe o ano do extrato que deseja baixar e o processo será iniciado automaticamente.

📊 Exemplo de Fluxo

Usuário escolhe o ano →

Script baixa o CSV da CVM →

Dados são tratados e padronizados →

Registros inseridos no banco de dados MySQL →

Arquivo CSV é removido da máquina.

📌 Observações

Em alguns arquivos da CVM, a coluna TP_FUNDO_CLASSE não está presente.

O projeto foi adaptado para padronizar automaticamente a estrutura e manter a consistência dos dados.

🎯 Objetivo

Esse projeto foi desenvolvido como prática para consolidar conhecimentos em Python, SQL, ETL e automação de processos, simulando desafios reais encontrados em projetos de Data Engineering e Business Intelligence.
