import sys
import pandas as pd 
from bs4 import BeautifulSoup
import requests
import re
from conection import conection_database
import os

def webscrapping_cvm():
    url = 'https://dados.cvm.gov.br/dados/FI/DOC/EXTRATO/DADOS'
    requisição = requests.get(url)
    soup = BeautifulSoup(requisição.text, 'html.parser')
    re_soup = soup.find('pre').text
    arquivos = re.findall('extrato_fi(?:_\d{4})?\.csv', re_soup)
   
    return arquivos

colunas_importantes = [
"TP_FUNDO_CLASSE","CNPJ_FUNDO_CLASSE","DENOM_SOCIAL","DT_COMPTC","CONDOM","NEGOC_MERC","MERCADO","TP_PRAZO","PRAZO","PUBLICO_ALVO","REG_ANBIMA",
"CLASSE_ANBIMA","DISTRIB","POLIT_INVEST","APLIC_MAX_FUNDO_LIGADO","RESULT_CART_INCORP_PL","FUNDO_COTAS","FUNDO_ESPELHO","APLIC_MIN","ATUALIZ_DIARIA_COTA","PRAZO_ATUALIZ_COTA","COTA_EMISSAO",
"COTA_PL","QT_DIA_CONVERSAO_COTA","QT_DIA_PAGTO_COTA","QT_DIA_RESGATE_COTAS","QT_DIA_PAGTO_RESGATE","TP_DIA_PAGTO_RESGATE","TAXA_SAIDA_PAGTO_RESGATE","TAXA_ADM","TAXA_CUSTODIA_MAX","EXISTE_TAXA_PERFM",
"TAXA_PERFM","PARAM_TAXA_PERFM","PR_INDICE_REFER_TAXA_PERFM","VL_CUPOM","CALC_TAXA_PERFM","INF_TAXA_PERFM","EXISTE_TAXA_INGRESSO","TAXA_INGRESSO_REAL","TAXA_INGRESSO_PR","EXISTE_TAXA_SAIDA",
"TAXA_SAIDA_REAL","TAXA_SAIDA_PR","OPER_DERIV","FINALIDADE_OPER_DERIV","OPER_VL_SUPERIOR_PL","FATOR_OPER_VL_SUPERIOR_PL","CONTRAP_LIGADO","INVEST_EXTERIOR","APLIC_MAX_ATIVO_EXTERIOR","ATIVO_CRED_PRIV",
"APLIC_MAX_ATIVO_CRED_PRIV","PR_INSTITUICAO_FINANC_MIN","PR_INSTITUICAO_FINANC_MAX","PR_CIA_MIN","PR_CIA_MAX","PR_FI_MIN","PR_FI_MAX","PR_UNIAO_MIN","PR_UNIAO_MAX","PR_ADMIN_GESTOR_MIN",
"PR_ADMIN_GESTOR_MAX","PR_EMISSOR_OUTRO_MIN","PR_EMISSOR_OUTRO_MAX","PR_COTA_FI_MIN","PR_COTA_FI_MAX","PR_COTA_FIC_MIN","PR_COTA_FIC_MAX","PR_COTA_FI_QUALIF_MIN","PR_COTA_FI_QUALIF_MAX",
"PR_COTA_FIC_QUALIF_MIN","PR_COTA_FIC_QUALIF_MAX","PR_COTA_FI_PROF_MIN","PR_COTA_FI_PROF_MAX","PR_COTA_FIC_PROF_MIN","PR_COTA_FIC_PROF_MAX","PR_COTA_FII_MIN","PR_COTA_FII_MAX",
"PR_COTA_FIDC_MIN","PR_COTA_FIDC_MAX","PR_COTA_FICFIDC_MIN","PR_COTA_FICFIDC_MAX","PR_COTA_FIDC_NP_MIN","PR_COTA_FIDC_NP_MAX","PR_COTA_FICFIDC_NP_MIN","PR_COTA_FICFIDC_NP_MAX","PR_COTA_ETF_MIN",
"PR_COTA_ETF_MAX","PR_CRI_MIN","PR_CRI_MAX","PR_TITPUB_MIN","PR_TITPUB_MAX","PR_OURO_MIN","PR_OURO_MAX","PR_TIT_INSTITUICAO_FINANC_BACEN_MIN","PR_TIT_INSTITUICAO_FINANC_BACEN_MAX","PR_VLMOB_MIN",
"PR_VLMOB_MAX","PR_ACAO_MIN","PR_ACAO_MAX","PR_DEBENTURE_MIN","PR_DEBENTURE_MAX","PR_NP_MIN","PR_NP_MAX","PR_COMPROM_MIN","PR_COMPROM_MAX","PR_DERIV_MIN","PR_DERIV_MAX","PR_ATIVO_OUTRO_MIN",
"PR_ATIVO_OUTRO_MAX","PR_COTA_FMIEE_MIN","PR_COTA_FMIEE_MAX","PR_COTA_FIP_MIN","PR_COTA_FIP_MAX","PR_COTA_FICFIP_MIN","PR_COTA_FICFIP_MAX"
]

def download_csv():
    arquivos = webscrapping_cvm()
   
    for i in arquivos:
        print(i)

    valorCSV = input('De qual ano vc gostaria de baixar o extrato?:')

    urldownload_csv = requests.get(f'https://dados.cvm.gov.br/dados/FI/DOC/EXTRATO/DADOS/extrato_fi_{valorCSV}.csv')

    if urldownload_csv:
        with open(f'extrato_fi_{valorCSV}.csv', 'wb') as f:
            f.write(urldownload_csv.content)
    else:
        print('Ano invalido')
        sys.exit()
       
    
    return valorCSV

def insert_Database(columns_cvmdata,dado_bruto):

    cursor,mydb = conection_database()

    comando = f"""
    INSERT INTO extratos_cvm.cvm_data({', '.join(columns_cvmdata)})
    VALUES ({', '.join(['%s'] * len(columns_cvmdata))})
    """

    cursor.execute(comando, dado_bruto)
    mydb.commit()
    cursor.close(),

def read_csv(): 

    valor_CSV = download_csv()
    df = pd.read_csv(f'extrato_fi_{valor_CSV}.csv', sep=';', encoding='latin1') 
    lista = [df.columns.to_list()] + df.values.tolist() 
    cabecalho = lista[0]    
    dado_bruto = [] 
    count = 0

    for i in lista[1:]:
        if count == lista[1:]:
            break
        else:
            if cabecalho[0] != colunas_importantes[0]:
                
                modificado = ['TP_FUNDO_CLASSE'] + cabecalho
                i = [None] + i

                modificado[1] = 'CNPJ_FUNDO_CLASSE'

                dicionario = dict(zip(modificado, i))

                dado_bruto = []

                for l in colunas_importantes:
                    dado_bruto.append(dicionario[l])

                insert_Database(modificado, dado_bruto)
   
            else:
                dicionario = dict(zip(cabecalho, i))
                dado_bruto = []

                for l in colunas_importantes:
                    dado_bruto.append(dicionario[l])

                insert_Database(colunas_importantes, dado_bruto)



            count += 1
            
    os.remove(f"extrato_fi_{valor_CSV}.csv")
    print(f'Os valores do extrato_fi_{valor_CSV} foram colocados no banco de dados!')

read_csv()




