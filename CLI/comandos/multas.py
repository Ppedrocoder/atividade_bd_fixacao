from db import conectar

def pendentes():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("SELECT id, valor, data_aplicacao, data_pagamento, id_usuario FROM multa WHERE data_pagamento IS NULL ORDER BY id;")
    print(cur.fetchall())

    conn.close()

def pagar(args):
    if not args:
        print("Informe o ID da multa")
        return

    conn = conectar()
    cur = conn.cursor()

    cur.execute(
        "UPDATE multa SET data_pagamento = CURRENT_DATE WHERE id = %s",
        (args[0],)
    )

    conn.commit()
    conn.close()