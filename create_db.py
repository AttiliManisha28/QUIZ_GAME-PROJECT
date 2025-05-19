import sqlite3

conn = sqlite3.connect('quiz.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        option1 TEXT NOT NULL,
        option2 TEXT NOT NULL,
        option3 TEXT NOT NULL,
        option4 TEXT NOT NULL,
        correct_option INTEGER NOT NULL
    )
''')

c.execute('DELETE FROM questions')

questions = [
    ("What is the capital of France?", "Paris", "Berlin", "London", "Rome", 1),
    ("Which is the largest planet?", "Earth", "Mars", "Jupiter", "Venus", 3),
    ("What is 2 + 2?", "3", "4", "5", "6", 2),
    ("Which language is used for web apps?", "Python", "Java", "HTML", "C++", 3)
]

c.executemany('''
    INSERT INTO questions (question, option1, option2, option3, option4, correct_option)
    VALUES (?, ?, ?, ?, ?, ?)
''', questions)

conn.commit()
conn.close()

print("Database created and questions inserted successfully.")
