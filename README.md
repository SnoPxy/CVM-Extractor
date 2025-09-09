# 📊 CVM EXTRATOR  

## Descrição do Projeto  
O **CVM EXTRATOR** é uma aplicação em Python desenvolvida para automatizar a coleta, tratamento e armazenamento dos **extratos de fundos de investimento disponibilizados pela CVM**.  
O sistema realiza o download dos arquivos CSV diretamente do site da CVM, trata eventuais inconsistências (como ausência da coluna `TP_FUNDO_CLASSE`) e organiza os dados em um banco de dados relacional (MySQL), criando uma base confiável para análises e consultas futuras.  

---

## Funcionalidades Principais  
- **Coleta Automática**: Identifica e baixa os arquivos de extrato diretamente do site da CVM.  
- **Tratamento de Dados**: Realiza a leitura e padronização dos arquivos CSV utilizando **Pandas**, garantindo consistência mesmo em estruturas diferentes.  
- **Integração com Banco de Dados**: Insere os registros processados em uma tabela MySQL.  
- **Atualização Contínua**: Permite baixar e inserir novos extratos sempre que a CVM disponibilizar atualizações.  
- **Limpeza Automática**: Remove o arquivo local após a inserção no banco, evitando acúmulo desnecessário.  

---

## Tecnologias Utilizadas  
- **Python 3**  
- **Pandas** (tratamento de dados)  
- **BeautifulSoup** (web scraping)  
- **Requests** (requisições HTTP)  
- **Regex** (extração de nomes de arquivos)  
- **MySQL** (armazenamento dos dados)  

---

## Como Usar  

### Configuração do Ambiente  
1. Certifique-se de ter o **Python 3** instalado.  
2. Clone este repositório:  
   ```bash
   git clone https://github.com/seu-usuario/CVM_EXTRATOR.git

## Configure o arquivo conection.py com suas credenciais do banco de dados MySQL:

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


## Execute o script principal:
    python app.py
- **Informe o ano desejado para baixar o extrato.
- **O sistema fará a leitura, tratamento, inserção no banco e exclusão do arquivo local.

  
