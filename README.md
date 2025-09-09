# 📊 CVM EXTRATOR

## 📌 Descrição do Projeto
O **CVM EXTRATOR** é uma aplicação desenvolvida em Python que automatiza o processo de coleta, leitura e organização de dados da CVM (Comissão de Valores Mobiliários).  
O sistema baixa automaticamente os arquivos de extratos disponibilizados no site da CVM, processa os arquivos CSV, padroniza colunas (inclusive em casos de ausência como o `TP_FUNDO_CLASSE`) e organiza as informações em um banco de dados para uso posterior.  

Esse fluxo cria uma base confiável e atualizada, permitindo futuras análises e aplicações em projetos de dados financeiros.

---

## 🚀 Funcionalidades Principais
- **Automação da coleta**: download direto dos extratos no site da CVM.  
- **Leitura e padronização**: tratamento de inconsistências nos CSVs, garantindo uniformidade.  
- **Armazenamento estruturado**: inserção dos dados em um banco de dados relacional.  
- **Atualização automática**: sempre que novos extratos são lançados pela CVM, o sistema é capaz de incorporá-los.  

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**  
- **Pandas** → leitura e manipulação de dados  
- **BeautifulSoup4** → web scraping para identificar arquivos no site da CVM  
- **Requests** → download dos arquivos CSV  
- **MySQL Connector** → integração com banco de dados relacional  

---

## ⚙️ Como Usar

### 1. Configuração do Ambiente
Certifique-se de ter o **Python 3.x** instalado.  
Crie e ative um ambiente virtual:

CVM-EXTRATOR/
│── app.py                # Código principal
│── conection.py          # Conexão com o banco de dados
│── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto

Contribuições são bem-vindas!
Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias ou novas funcionalidades.

👨‍💻 Autor
Arthur Lopes
