from database import conectar

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bandas(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            formacao INT
        ) ENGINE = InnoDB
    """)

    cursor.execute("""
                CREATE TABLE IF NOT EXISTS albuns(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    ano INT,
                    id_banda INT NOT NULL,
                    FOREIGN KEY(id_banda) REFERENCES bandas(id)
                ) ENGINE = InnoDB
            """)

    cursor.execute("""
                CREATE TABLE IF NOT EXISTS musicas(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    duracao INT,
                    faixa INT,
                    id_album INT NOT NULL,
                    FOREIGN KEY(id_album) REFERENCES albuns(id)
                ) ENGINE = InnoDB
            """)

    conn.commit()
    cursor.close()
    conn.close()