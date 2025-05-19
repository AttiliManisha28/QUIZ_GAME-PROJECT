from flask import Flask, render_template, request, redirect, session
import sqlite3
import random

app = Flask(__name__)
app.secret_key = 'quiz_secret'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quiz')
def quiz():
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions ORDER BY RANDOM()")
    questions = cursor.fetchall()
    conn.close()

    session['questions'] = questions  # Store in session to check later
    return render_template('quiz.html', questions=questions)


@app.route('/submit', methods=['POST'])
def submit():
    questions = session.get('questions')
    score = 0

    for i, question in enumerate(questions):
        correct_option = question[6]  # Assuming this is the correct answer index (0-3)
        user_answer = int(request.form.get(f'q{i}'))
        if user_answer == correct_option:
            score += 1

    return render_template('result.html', score=score, total=len(questions))


@app.route('/check_db')
def check_db():
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM questions")
    count = cursor.fetchone()[0]
    conn.close()
    return f"Total questions in DB: {count}"


if __name__ == '__main__':
    app.run(debug=True)






#TO RUN THE FILE TYPE: python app.py, then click the link 