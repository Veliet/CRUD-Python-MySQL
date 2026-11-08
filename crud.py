import mysql.connector

from database import conectar, aux
from validacoes import chk_entrada

def ins_bandas(nome, formacao):
    return aux("""
        INSERT INTO bandas (nome, formacao)
        VALUES (%s, %s)
    """, (nome, formacao))

def ins_albuns(nome, ano, id_banda):
    return aux("""
            INSERT INTO albuns (nome, ano, id_banda)
            VALUES (%s, %s, %s)
        """, (nome, ano, id_banda))

def ins_musicas(nome, duracao, faixa, id_album):
    return aux("""
            INSERT INTO musicas (nome, duracao, faixa, id_album)
            VALUES (%s, %s, %s, %s)
        """, (nome, duracao, faixa, id_album))

def slc_tabela():
    conn = conectar()

    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT TABLE_NAME
            FROM information_schema.tables
            WHERE TABLE_SCHEMA = DATABASE()
                AND TABLE_TYPE = 'BASE TABLE'
                AND TABLE_NAME IN ('bandas', 'albuns', 'musicas')
            ORDER BY TABLE_NAME
        """)

        tabelas = cursor.fetchall()

        if not tabelas:
            print(">> Nenhuma tabela encontrada\n")
            return None

        print("\nTabelas\n==============")
        for i, tbl in enumerate(tabelas, start=1):
            print(f"{i} - {tbl[0]}")
        print("==============\n")
        try:
            escolha = int(input(">> "))
        except ValueError:
            print("Digite um número válido\n")
            return None

        if not 1 <= escolha <= len(tabelas):
            print(">> Opção inválida\n")
            return None

        return tabelas[escolha - 1][0]

    finally:
        conn.close()

def registrar():
    tabela = slc_tabela()

    if tabela is None:
        return

    match tabela:
        case "bandas":
            nome = input("Nome da banda: ")
            formacao = chk_entrada("Ano de formação: ")
            resultado = ins_bandas(nome, formacao)
            if resultado > 0:
                print("\nBanda cadastrada\n")
            else:
                print("\nNenhuma alteração registrada\n")

        case "albuns":
            nome = input("Nome do álbum: ")
            ano = chk_entrada("Ano do álbum: ")
            id_banda = chk_entrada("ID da banda: ")
            resultado = ins_albuns(nome, ano, id_banda)
            if resultado > 0:
                print("\nÁlbum cadastrado\n")
            else:
                print("\nNenhuma alteração registrada\n")

        case "musicas":
            nome = input("Nome da música: ")
            duracao = chk_entrada("Duração (Seg): ")
            faixa = chk_entrada("Número da faixa: ")
            id_album = chk_entrada("ID do álbum: ")
            resultado = ins_musicas(nome, duracao, faixa, id_album)
            if resultado > 0:
                print("\nMúsica cadastrada\n")
            else:
                print("\nNenhuma alteração registrada\n")
        case _:
            print("Erro\n")

def listar():
    tabela = slc_tabela()

    if tabela is None:
        return

    match tabela:
        case "bandas":
            dados = aux("SELECT * FROM bandas", fetch=True)

        case "albuns":
            dados = aux("SELECT * FROM albuns", fetch=True)

        case "musicas":
            dados = aux("SELECT * FROM musicas", fetch=True)

        case _:
            print("Erro\n")
            return

    if not dados:
        print("Nenhum registro encontrado\n")
        return

    for linha in dados:
        print(linha)

def atualizar():
    tabela = slc_tabela()

    if tabela is None:
        return

    match tabela:
        case "bandas":
            id_registro = chk_entrada("ID da banda: ")
            nome = input("Novo nome da banda: ")
            formacao = chk_entrada("Novo ano de formação:")

            sql = """
                UPDATE bandas
                 SET nome = %s, formacao = %s
                WHERE id = %s
            """
            parametros = (nome, formacao, id_registro)

        case "albuns":
            id_registro = chk_entrada("ID do álbum: ")
            nome = input("Novo Nome: ")
            ano = chk_entrada("Novo ano: ")
            id_banda = chk_entrada("ID da banda: ")

            sql = """
                UPDATE  albuns
                SET nome = %s, ano = %s, id_banda = %s
                WHERE id = %s
            """
            parametros = (nome, ano, id_banda, id_registro)

        case "musicas":
            id_registro = chk_entrada("ID da música: ")
            nome = input("Novo nome: ")
            duracao = chk_entrada("Duração (seg): ")
            faixa = chk_entrada("Número da faixa: ")
            id_album = chk_entrada("ID do álbum: ")

            sql = """
                UPDATE musicas
                SET nome = %s, duracao = %s, faixa = %s, id_album = %s
                WHERE id = %s 
            """
            parametros = (nome, duracao, faixa, id_album, id_registro)

        case _:
            print("Tabela inválida\n")
            return

    resultado = aux(sql, parametros)
    if resultado > 0:
        print("Registro atualizado\n")

    else:
        print("Nenhuma alteração feita\n")

def excluir():
    tabela = slc_tabela()

    if tabela is None:
        return

    match tabela:
        case "bandas":
            id_registro = chk_entrada("ID da banda: ")
            sql = "DELETE FROM bandas WHERE id = %s"

        case "albuns":
            id_registro = chk_entrada("ID do álbum: ")
            sql = "DELETE FROM albuns WHERE id = %s"

        case "musicas":
            id_registro = chk_entrada("ID da música: ")
            sql = "DELETE FROM musicas WHERE id = %s"

        case _:
            print("Tabela inválida\n")
            return

    try:
        resultado = aux(sql,(id_registro,))

        if resultado > 0:
            print("Registro excluído\n")

        else:
            print("ID não encontrado\n")

    except mysql.connector.IntegrityError:
        print("Erro: Não foi possível excluir\nDados vinculados a outra(s) tabela(s)\n")