from db import conectar

def listar():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("""
    SELECT l.id, l.titulo, l.ano_publicacao, l.genero,
           a.nome AS autor,
           c.nome AS categoria,
           e.nome AS editora
    FROM livro l
    JOIN autor a ON a.id = l.id_autor
    JOIN categoria c ON c.id = l.id_categoria
    JOIN editora e ON e.id = l.id_editora
    ORDER BY l.id;
    """)

    for row in cur.fetchall():
        print(row)

    conn.close()
def adicionar():
    titulo = input("Título: ")
    ano_publicacao = input("Ano de publicação: ")
    genero = input("Gênero: ")
    id_autor = input("ID do autor: ")
    id_categoria = input("ID da categoria: ")
    id_editora = input("ID da editora: ")

    conn = conectar()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO livro (titulo, ano_publicacao, genero, id_autor, id_categoria, id_editora)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (titulo, ano_publicacao, genero, id_autor, id_categoria, id_editora)
    )

    conn.commit()
    conn.close()
    print("Livro adicionado!")
def disponiveis():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    SELECT l.id, l.titulo, l.ano_publicacao, l.genero
    FROM livro l
    LEFT JOIN emprestimo e ON e.id_livro = l.id AND e.data_devolucao IS NULL
    WHERE e.id IS NULL
    ORDER BY l.id;
    """)

    for r in cur.fetchall():
        print(r)

    conn.close()
def sem_emprestimo():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    SELECT l.id, l.titulo, l.ano_publicacao, l.genero
    FROM livro l
    WHERE NOT EXISTS (
        SELECT 1
        FROM emprestimo e
        WHERE e.id_livro = l.id
    )
    ORDER BY l.id;
    """)

    print(cur.fetchall())
    conn.close()
def mais_reservados():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    SELECT r.id_livro, COUNT(*) AS total
    FROM reserva r
    GROUP BY r.id_livro
    ORDER BY total DESC;
    """)

    print(cur.fetchall())
    conn.close()
def por_categoria():
    cat = input("Categoria: ")

    conn = conectar()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT l.id, l.titulo, l.ano_publicacao, l.genero
        FROM livro l
        JOIN categoria c ON c.id = l.id_categoria
        WHERE c.nome = %s
        ORDER BY l.id
        """,
        (cat,)
    )

    print(cur.fetchall())
    conn.close()