import sqlite3 as sql

def conectar():
    return sql.connect("pessoas.db")

def tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            cpf TEXT,
            telefone TEXT
        
        )
    
    """)

    conn.commit()
    conn.close()

def registrar(nome, idade, cpf, telefone):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO dados (nome, idade, cpf, telefone)
        VALUES (?, ?, ?, ?)
    
    """,(nome, idade, cpf, telefone))

    conn.commit()
    conn.close()

def listar():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM dados")
    pessoas = cursor.fetchall()

    conn.close()
    return pessoas

def atualizar(id, nome, idade, cpf, telefone):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE dados SET nome=?, idade=?, cpf=?, telefone=? WHERE id=?
    
    """, (nome, idade, cpf, telefone, id))

    conn.commit()
    conn.close()

def excluir(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM dados WHERE id=?", (id,))

    conn.commit()
    conn.close()