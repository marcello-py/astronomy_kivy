# Exemplo de queries.py
from database import Database
def select_users_by_name(name):
    return f"SELECT * FROM users WHERE name = '{name}';"

def insert_user(name, age):
    return f"INSERT INTO users (name, age) VALUES ('{name}', {age});"
