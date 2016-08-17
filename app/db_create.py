import sqlite3
from config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as conn:
	c = conn.cursor()
	c.execute("""  CREATE TABLE tasks (task_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL, status INTEGER NOT NULL) """)
	c.execute('INSERT INTO tasks (name, due_date, priority, status) VALUES ("finish tutorial", "08/25/2016", 10,1)')
	c.execute('INSERT INTO tasks (name, due_date, priority, status) VALUES ("finish next tutorial", "09/25/2016", 10,1)')