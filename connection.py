import mysql.connector
from mysql.connector import Error

try:
    db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='banco')
    print('Conexão estabelecida')
except Error as e:
    print('Erro ao conectar ao banco de dados:', e)

cursor = db_connection.cursor()
def Insert(nome, login, senha, sexo):
    #insert
    sql = f'INSERT INTO usuario (name, login, password, sexo) VALUES ("{nome}","{login}","{senha}","{sexo}")'
    cursor.execute(sql)
    db_connection.commit()

    cursor.close()
    db_connection.close()

def Verify_login_senha(login, senha):
    try:
        # Estabelece a conexão com o banco de dados
        db_connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='banco'
        )
        print('Conexão estabelecida')

        # Cria um cursor para executar consultas SQL
        cursor = db_connection.cursor()

        # Executa a consulta para verificar o login e a senha
        sql = f'SELECT * FROM usuario WHERE login = "{login}" AND password = "{senha}"'
        cursor.execute(sql)

        # Recupera o resultado da consulta
        resultado = cursor.fetchone()
        print(resultado)
        # Verifica se o login e a senha correspondem a um registro no banco de dados
        if resultado[2] == login and resultado[3] == senha:
            print("Login bem-sucedido")
        else:
            print("Login ou senha incorretos")

    except Error as e:
        print('Erro ao conectar ao banco de dados:', e)

    finally:
        # Fecha o cursor e a conexão com o banco de dados
        cursor.close()
        db_connection.close()