from database import criar_banco
from tabelas import criar_tabelas
from crud import registrar, listar, atualizar, excluir

def main():
    criar_banco()
    criar_tabelas()

    while True:
        try:
            opcao = int(input("\n___ Menu ___\n"
                            "1 - Registrar\n"
                            "2 - Listar\n"
                            "3 - Atualizar\n"
                            "4 - Excluir\n"
                            "5 - Sair\n\n"
                              ">> "))
        except ValueError:
            print("Digite um número do menu\n")
            continue

        match opcao:
            case 1:
                registrar()
            case 2:
                listar()
            case 3:
                atualizar()
            case 4:
                excluir()
            case 5:
                print("\nFinalizando...")
                break
            case _:
                print("Comando inválido\n")

if __name__ == '__main__':
    main()