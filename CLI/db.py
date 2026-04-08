import os

import psycopg2
from psycopg2 import sql


def _garantir_banco_existe(host, database, user, password, port):
    conn = psycopg2.connect(
        host=host,
        database="postgres",
        user=user,
        password=password,
        port=port,
    )
    conn.autocommit = True

    try:
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (database,))

        if cur.fetchone() is None:
            cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(database)))
    finally:
        conn.close()

def conectar():
    host = os.getenv("PGHOST", "localhost")
    database = os.getenv("PGDATABASE", "biblioteca")
    user = os.getenv("PGUSER", "postgres")
    password = os.getenv("PGPASSWORD", "postgres")
    port = os.getenv("PGPORT", "5432")

    _garantir_banco_existe(host, database, user, password, port)

    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port,
    )
    return conn