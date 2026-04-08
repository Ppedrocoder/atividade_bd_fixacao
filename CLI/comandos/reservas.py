from db import conectar

def nova():
    user = input("Usuário ID: ")
    livro = input("Livro ID: ")

    conn = conectar()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO reserva (status_reserva, id_usuario, id_livro) VALUES (%s, %s, %s)",
        ("Ativa", user, livro)
    )

    conn.commit()
    conn.close()

def disponiveis():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("SELECT id, data_reserva, status_reserva, id_livro, id_usuario FROM reserva WHERE status_reserva = 'Ativa' ORDER BY id;")
    print(cur.fetchall())

    conn.close()