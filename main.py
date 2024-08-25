import sqlite3
import os

def connectar_ao_banco(nome_banco):
    conexao = sqlite3.connect(nome_banco)
    return conexao

def executar_sql_script(conexao, caminho_sql):
    with open(caminho_sql, 'r') as file:
        sql_script = file.read()
            
    cursor = conexao.cursor()
    cursor.executescript(sql_script)
    conexao.commit()

def insert_tabelas (conexao):
    cursor = conexao.cursor()
    #insert produtos
    cursor.execute('INSERT INTO Produto (id_produto, nome, qtnd_disponivel, preco, id_categoria, id_fornecedor) VALUES (1,"Teclado Gamer", 20, 120.10, 1, 1)')
    cursor.execute('INSERT INTO Transacao (id_transacao, qtnd_produto, valor_total, data_transacao, id_cliente, id_produto) VALUES ()')
    cursor.execute('INSERT INTO Cliente')
    cursor.execute('INSERT INTO Fornecedor')


    conexao.commit()

def main():
    # Nome do banco de dados SQLite 
    nome_banco = 'mercado.db'
    
    # Conectando ao banco de dados
    conn = connectar_ao_banco(nome_banco)

    # Diretórios onde estão os scripts SQL  
    produto_sql = 'produto/produto.sql'
    transacao_sql = 'transacao/transacao.sql'
    
    # Executando scripts SQL
    executar_sql_script(conn, produto_sql)
    executar_sql_script(conn, transacao_sql)
    insert_tabelas(conn)


    # Fechando a conexão
    conn.close()

if __name__ == "__main__":
    main()
