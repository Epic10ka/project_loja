import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "database" / "loja.db"


def connect():
    """
    garantindo que a pasta 'data' existe e que retorna a conexão com o SQLite.
    """

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    return sqlite3.connect(DB_PATH)



def create():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            preco INTEGER NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()


def insert(nome, preco):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO produtos (nome, preco) VALUES (?, ?)""", (nome, preco))

    conn.commit()
    conn.close()


def select(choose_id = False, id = 0):

    conn = connect()
    cursor = conn.cursor()

    if not choose_id:
        cursor.execute("""
        SELECT * FROM produtos""")

        produtos = cursor.fetchall()
        return produtos

    else:
        cursor.execute("""
            SELECT * FROM produtos WHERE id = ?""", (id,))

        produtos = cursor.fetchall()
        return produtos


def update(nome, preco, id_n):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE produtos SET nome = ?, preco = ? WHERE id = ?""", (nome, preco, id_n) )

    conn.commit()
    conn.close()

