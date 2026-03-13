import sqlite3

DB_NAME = "data/progress.db"

def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

def init_db():

    conn = get_connection()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT,
        completed INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()

def get_tasks():

    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT id, task, completed FROM tasks")

    tasks = c.fetchall()

    conn.close()

    return tasks


def add_task(task):

    conn = get_connection()
    c = conn.cursor()

    c.execute("INSERT INTO tasks(task) VALUES(?)", (task,))

    conn.commit()
    conn.close()


def update_task(task_id, status):

    conn = get_connection()
    c = conn.cursor()

    c.execute(
        "UPDATE tasks SET completed=? WHERE id=?",
        (status, task_id)
    )

    conn.commit()
    conn.close()
