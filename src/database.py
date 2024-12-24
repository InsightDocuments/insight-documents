import sqlite3

def initialize_database(db_path="documents.db"):
    """
    Initializes the SQLite database and creates the 'documents' table if it does not exist.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            page_number INTEGER,
            content TEXT
        )
    ''')
    conn.commit()
    conn.close()