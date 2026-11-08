def chk_entrada(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Entrada inválida\n")