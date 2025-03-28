import sqlite3

def init_db():
    """Инициализирует базу данных SQLite."""
    conn = sqlite3.connect("skating.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tournaments (
        id INTEGER PRIMARY KEY,
        name TEXT,
        dances TEXT  # JSON-список танцев
    )
    """)
    conn.commit()
    conn.close()

def save_preset(name: str, dances: list):
    """Сохраняет набор танцев в БД."""
    conn = sqlite3.connect("skating.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tournaments (name, dances) VALUES (?, ?)",
        (name, str(dances))
    )
    conn.commit()
    conn.close()

def load_presets() -> list:
    """Загружает список сохранённых турниров."""
    conn = sqlite3.connect("skating.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM tournaments")
    presets = cursor.fetchall()
    conn.close()
    return presets
