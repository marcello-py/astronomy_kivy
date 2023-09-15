import sqlite3


class Database:
    def __init__(self, db_astronomy):
        self.conn = sqlite3.connect(db_astronomy)
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS data(
                            id INTERGER PRIMARY KEY,
                            username TEXT NOT NULL, 
                            password TEXT NOT NULL
                            )
                            ''')
        self.conn.commit()

    def insert_user(self, username, password):
        self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        self.conn.commit()

    def check_credentials(self, username, password):
        self.cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = self.cursor.fetchone()
        if user:
            return True
        else:
            return False