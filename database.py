import sqlite3

class Database:
    def __init__(self, db_astronomy):
        self.conn = sqlite3.connect(db_astronomy)
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL, 
                password TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def insert_user(self, username, password):
        # Use marcadores de posição ? e passe os valores como parâmetros
        self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        self.conn.commit()

    def insert_user(self, username, password):
        # Use marcadores de posição ? e passe os valores como parâmetros
        self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        self.conn.commit()


    def drop_table(self):
        self.cursor.execute('DELETE FROM users WHERE id = 2')
        self.conn.commit()


    def check_credentials(self, username, password):
        # Use marcadores de posição ? e passe os valores como parâmetros
        self.cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = self.cursor.fetchone()
        if user:
            return True
        else:
            return False

    def view_all_users(self):
        # Execute uma consulta para selecionar todos os registros da tabela "users"
        self.cursor.execute('SELECT * FROM users')
        users = self.cursor.fetchall()

        # Imprima os resultados
        for user in users:
            print(user)

# Criar uma instância da classe Database
db = Database('astronomy.db')

# Inserir um usuário com valores fictícios
#db.insert_user('marcelonunesmeira@gmail.com', '123')

# Verificar as credenciais corretas
if db.check_credentials('marcelonunesmeira@gmail.com', '123'):
    print("Credenciais corretas.")
else:
    print("Credenciais incorretas.")


db.view_all_users()

# Deletar dados especificos
db.drop_table()


# Fechar a conexão com o banco de dados
db.conn.close()
