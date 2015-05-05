import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

create_table_query = """
CREATE TABLE company(id INTEGER PRIMARY KEY, name TEXT,
                   monthly_salary INTEGER, yearly_bonus INTEGER,
                   position TEXT)
"""

cursor.execute(create_table_query)

users = [
        ("Ivan Ivanov", 5000, 10000, "Software Developer"),
        ("Rado Rado", 500, 0, "Technical Support internn"),
        ("Ivo Ivo", 10000, 100000, "CEO"),
        ("Petar Petrov", 3000, 1000, "Marketing Manager"),
        ("Maria Georgieva", 8000, 10000, "COO")]

cursor.executemany(""" INSERT INTO company(
name, monthly_salary, yearly_bonus, position) VALUES(?,?,?,?)""", users)
conn.commit()
