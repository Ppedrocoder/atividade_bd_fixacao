from pathlib import Path

from db import conectar


BASE_DIR = Path(__file__).resolve().parents[2]

def executar_arquivo_sql(caminho):
    conn = conectar()
    cur = conn.cursor()

    try:
        with open(caminho, "r", encoding="utf-8", errors="ignore") as f:
            sql = f.read()

        comandos = sql.split(";")

        for comando in comandos:
            comando = comando.strip()
            if comando:
                cur.execute(comando)

        conn.commit()
        print("SQL executado!")

    except Exception as e:
        conn.rollback()
        print("Erro:", e)

    finally:
        conn.close()

def create():
    executar_arquivo_sql(BASE_DIR / "fisico" / "ddl.sql")
    print("Tabelas criadas!")

def seed():
    executar_arquivo_sql(BASE_DIR / "fisico" / "dml.sql")
    print("Dados inseridos!")

def reset():
    confirmar = input("Tem certeza que deseja resetar o banco? (s/n): ")

    if confirmar.lower() != "s":
        print("Cancelado.")
        return

    executar_arquivo_sql(BASE_DIR / "fisico" / "reset.sql")
    executar_arquivo_sql(BASE_DIR / "fisico" / "ddl.sql")
    executar_arquivo_sql(BASE_DIR / "fisico" / "dml.sql")

    print("Banco resetado!")