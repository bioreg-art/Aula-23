import mysql.connector
import pandas as pd
from mysql.connector import Error

try:
    #Estabelece a conexão
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='escola'
    )

    if conexao.is_connected():
        print("Conectado com sucesso!")
        #Cria um cursor(objeto que permite executar comandos)
        cursor = conexao.cursor()


        #Define a query de insert usando placeholders (%s)
        sql = "INSERT INTO alunos (nome, cpf, data_nascimento, email, telefone, data_matricula, id_curso) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        #Valores que serão substituidos nos placeholders, na mesma ordem
        valores = ('joana', '11122253344', '2005-04-21', 'joana@email.com', '21911110002', '2026-02-07', '1')

        #Executa o insert no banco, substituindo os % pelos valores em "valores"
        #O conector trata automaticamente aspas, datas e acentos
        cursor.execute(sql, valores)

        #Confirma (grava) as alteraçoes da transação no banco
        #Sem commit() , o INSERT ficaria só na memória e seria descartado
        conexao.commit()

        #Mostra o ID (AUTO_INCREMENT) gerado na última inserção
        print(f"Linha inserida, ID gerado: {cursor.lastrowid}")

        #Executa uma consulta
        cursor.execute("SELECT * FROM alunos LIMIT 5")


        #Busca os resultados
        resultados = cursor.fetchall()          
        for linha in resultados:
            print(linha)

            

except Error as e:
    print(f"Erro ao conectar ou executar: {e}")

finally:
    #Fecha o cursor (se foi criado)
    if 'cursor' in locals():
        try:
            cursor.close()
        except Exception:
            pass #Se ja estiver fechado ou ocorrer erro, ignore

    #Fecha a conexâo (se foi criada e ainda esta conectada)
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão encerrada")

