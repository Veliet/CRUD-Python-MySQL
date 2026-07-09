from database import tabela, registrar, listar, atualizar, excluir

tabela()

while True:
    print("\n___ Menu ___")
    print("1 - Cadastrar.")
    print("2 - Listar.")
    print("3 - Atualizar.")
    print("4 - Excluir.")
    print("5 - Sair.")

    try:
        opcao = int(input("\n>> "))
    except ValueError:
        print("\nErro >>> Digite um número inteiro.\n")
        continue

    match opcao:

        case 1:
            print("--- Cadastro ---\n")
            nome = input("Nome: ")

            try:
                idade = int(input("Idade: "))
            except ValueError:
                print("\nErro >>> Digite um número inteiro.\n")
                continue

            cpf = input("CPF: ")
            telefone = input("Telefone: ")

            registrar(nome, idade, cpf, telefone)
            print("\nPessoas cadastrada com sucesso.\n")

        case 2:
            pessoas = listar()

            if not pessoas:
                print("\nNenhum cadastro encontrado.\n")

            else:
                print("\n--- Cadastros ---\n")
                for pessoa in pessoas:
                    print(
                        f"ID: {pessoa[0]} | " 
                        f"Nome: {pessoa[1]} | "
                        f"Idade: {pessoa[2]} | "
                        f"CPF: {pessoa[3]} | "
                        f"Telefone: {pessoa[4]}"
                    )

        case 3:
            print("--- Atualizar ---\n")
            id = int(input("ID da pessoa: "))
            nome = input("Novo nome: ")

            try:
                idade = int(input("Nova idade: "))
            except ValueError:
                print("\nErro >>> Digite um número inteiro.\n")
                continue

            cpf = input("Novo CPF: ")
            telefone = input("Novo telefone: ")

            atualizar(id, nome, idade, cpf, telefone)
            print("\nCadastro atualizado.\n")

        case 4:
            print("--- Excluir ---\n")
            id = int(input("ID da pessoa: "))
            excluir(id)
            print("\nCadastro excluído.\n")

        case 5:
            print("\nFinalizando...")
            break

        case _:
            print("\nOpção inválida.\n")
