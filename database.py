import sqlite3

# Conectar ao banco de dados ou criar um novo se não existir
conn = sqlite3.connect('database.db')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Definir a query SQL para criar a tabela "usuarios"
create_table_query = """
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    birth DATE NOT NULL
);
"""

# Executar a query SQL para criar a tabela
cursor.execute(create_table_query)

# Commit (confirmar) as alterações no banco de dados
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()
