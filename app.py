from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(_name_)

def init_db():
    conn = sqlite3.connect('expense.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS expenses
                 (id INTEGER PRIMARY KEY,
                  title TEXT,
                  amount REAL,
                  category TEXT,
                  date TEXT)''')
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('expense.db')
    data = conn.execute('SELECT * FROM expenses').fetchall()
    total = conn.execute('SELECT SUM(amount) FROM expenses').fetchone()[0]
    category = conn.execute('SELECT category, SUM(amount) FROM expenses GROUP BY category').fetchall()
    conn.close()
    return render_template('index.html', data=data, total=total, category=category)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    amount = request.form['amount']
    category = request.form['category']
    date = request.form['date']

    conn = sqlite3.connect('expense.db')
    conn.execute('INSERT INTO expenses (title, amount, category, date) VALUES (?,?,?,?)',
                 (title, amount, category, date))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('expense.db')
    conn.execute('DELETE FROM expenses WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if _name_ == '_main_':
    init_db()
    app.run(debug=True)