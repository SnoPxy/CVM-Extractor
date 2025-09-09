import mysql.connector

def conection_database():
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'extratos_cvm',
    )   
    cursor = mydb.cursor()

    if not mydb.is_connected():
        print('Banco de dados n conectado')


    return cursor, mydb



