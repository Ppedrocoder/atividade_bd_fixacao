from comandos import emprestimos, livros, multas, reservas, usuarios

from comandos import setup

def mostrar_ajuda():
    print("Comandos disponíveis:")
    print("setup:create")
    print("setup:seed")
    print("setup:reset")
    print("==================================")
    print("livros:list")
    print("livros:add")
    print("livros:disponiveis")
    print("livros:sem-emprestimo")
    print("livros:mais-reservados")
    print("livros:por-categoria")
    print("==================================")
    print("usuarios:list")
    print("usuarios:add")
    print("usuarios:top-emprestimos")
    print("usuarios:top-reservas")
    print("usuarios:reservas <id>")
    print("==================================")
    print("emprestimos:novo")
    print("emprestimos:devolver")
    print("==================================")
    print("reservas:nova")
    print("reservas:disponiveis")
    print("==================================")
    print("multas:pendentes")
    print("multas:pagar <id>")
    print("==================================")
    print("relatorios:indisponiveis")
    print("===================================")

def executar_comando(cmd):
    partes = cmd.split()

    comando = partes[0]
    args = partes[1:] if len(partes) > 1 else []

    match comando:

        # SETUP
        case "setup:create":
            setup.create()
        case "setup:seed":
            setup.seed()
        case "setup:reset":
            setup.reset()

        # LIVROS
        case "livros:list":
            livros.listar()
        case "livros:add":
            livros.adicionar()
        case "livros:disponiveis":
            livros.disponiveis()
        case "livros:sem-emprestimo":
            livros.sem_emprestimo()

        # USUÁRIOS
        case "usuarios:list":
            usuarios.listar()
        case "usuarios:add":
            usuarios.adicionar()
        case "usuarios:reservas":
            usuarios.reservas(args)

        # EMPRÉSTIMOS
        case "emprestimos:novo":
            emprestimos.novo()
        case "emprestimos:devolver":
            emprestimos.devolver()

        # RESERVAS
        case "reservas:nova":
            reservas.nova()
        case "reservas:disponiveis":
            reservas.disponiveis()

        # MULTAS
        case "multas:pendentes":
            multas.pendentes()
        case "multas:pagar":
            multas.pagar(args)

        case "help":
            mostrar_ajuda()
        
        case "quit":
            print("Saindo...")
            exit(0) 

        case _:
            print("Comando inválido. Digite 'help'")

def main():
    print("Sistema de Biblioteca CLI")
    print("Digite 'help' para ver os comandos")
    print("Digite 'quit' para sair")


    while True:
        cmd = input(">> ")

        if cmd in ["exit", "sair", "quit"]:
            break

        executar_comando(cmd)


if __name__ == "__main__":
    main()