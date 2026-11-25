import sqlite3


def init_db(db_path: str = ":memory:") -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'user'
        )
        """
    )
    cursor.execute(
        "INSERT INTO users (username, password, role) VALUES ('admin', 's3nh@Forte123', 'admin')"
    )
    cursor.execute(
        "INSERT INTO users (username, password, role) VALUES ('alice', 'alice123', 'user')"
    )
    conn.commit()
    return conn


def authenticate(conn: sqlite3.Connection, username: str, password: str):
    # VULNERÁVEL (apenas laboratório): entrada do usuário interpolada diretamente na query SQL
    query = (
        f"SELECT id, username, role FROM users "
        f"WHERE username = '{username}' AND password = '{password}'"
    )
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchone()


if __name__ == "__main__":
    db = init_db()
    user_input = input("Usuário: ")
    pass_input = input("Senha: ")

    user = authenticate(db, user_input, pass_input)
    if user:
        print(f"Login bem-sucedido! Bem-vindo, {user[1]} (perfil: {user[2]})")
    else:
        print("Credenciais inválidas.")