from db import conectar

def novo():
    user = input("Usuário ID: ")
    livro = input("Livro ID: ")

    conn = conectar()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO emprestimo (id_usuario, id_livro) VALUES (%s, %s)",
        (user, livro)
    )

    conn.commit()
    conn.close()

def devolver():
    emp_id = input("ID empréstimo: ")

    conn = conectar()
    cur = conn.cursor()

    cur.execute(
        "UPDATE emprestimo SET data_devolucao = CURRENT_DATE WHERE id = %s",
        (emp_id,)
    )

    conn.commit()
    conn.close()