import mysql.connector as sql

def criar_banco():
    conn = sql.connect(
        host="localhost",
        user="root",
        password="FDFS"
    )
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS sample")

    cursor.close()
    conn.close()

def conectar():
    return sql.connect(host="localhost",
                       user="root",
                       password="FDFS",
                       database="sample"
                       )

def aux(sql, parametros=None, fetch=False):
    conn = conectar()

    try:
        cursor = conn.cursor()
        cursor.execute(sql, parametros or ())

        if fetch:
            return cursor.fetchall()

        conn.commit()
        return cursor.rowcount

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()