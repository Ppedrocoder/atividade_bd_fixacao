from db import conectar

def listar():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT id, nome, email, data_registro FROM usuario ORDER BY id;")
    print(cur.fetchall())
    conn.close()
def adicionar():
    nome = input("Nome: ")
    email = input("Email: ")

    conn = conectar()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO usuario (nome, email) VALUES (%s, %s)",
        (nome, email)
    )

    conn.commit()
    conn.close()
def top_emprestimos():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    SELECT u.id, u.nome, COUNT(*) AS total
    FROM emprestimo e
    JOIN usuario u ON u.id = e.id_usuario
    GROUP BY u.id, u.nome
    ORDER BY total DESC;
    """)

    print(cur.fetchall())
    conn.close()
def top_reservas():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    SELECT u.id, u.nome, COUNT(*) AS total
    FROM reserva r
    JOIN usuario u ON u.id = r.id_usuario
    GROUP BY u.id, u.nome
    ORDER BY total DESC;
    """)

    print(cur.fetchall())
    conn.close()
def reservas(args):
    if not args:
        print("Informe o ID")
        return

    conn = conectar()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT r.id, r.data_reserva, r.status_reserva, r.id_livro
        FROM reserva r
        WHERE r.id_usuario = %s
        ORDER BY r.id
        """,
        (args[0],)
    )

    print(cur.fetchall())
    conn.close()