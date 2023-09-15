import database

import sqlite3

db_name = 'user_database.db'  # Substitua pelo nome do seu arquivo de banco de dados

try:
    conn = sqlite3.connect(db_name)
    conn.close()
    print(f'O banco de dados {db_name} foi criado com sucesso!')
except sqlite3.Error as e:
    print(f'Erro ao criar o banco de dados {db_name}: {e}')
