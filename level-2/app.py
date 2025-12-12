from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import hashlib
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

DATABASE = 'database.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS infos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    # Check if users already exist
    cursor.execute('SELECT COUNT(*) FROM users')
    if cursor.fetchone()[0] == 0:
        # Add sample users
        users = [
            ('alice', 'password123', 'alice@example.com'),
            ('bob', 'securepass456', 'bob@example.com')
        ]
        
        for username, password, email in users:
            hashed_pw = hashlib.sha256(password.encode()).hexdigest()
            cursor.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)',
                         (username, hashed_pw, email))
        
        # Add sample infos for Alice (user_id=1)
        alice_infos = [
            ('Project Proposal', 'Confidential project proposal for Q1 2024. Budget: $50,000'),
            ('Meeting Notes', 'Discussion with stakeholders about new feature requirements'),
            ('Personal Document', 'Alice\'s personal notes - PRIVATE')
        ]
        
        for title, content in alice_infos:
            cursor.execute('INSERT INTO infos (user_id, title, content) VALUES (?, ?, ?)',
                         (1, title, content))
        
        # Add sample infos for Bob (user_id=2)
        bob_infos = [
            ('Salary Information', 'Bob\'s salary details: $85,000/year - CONFIDENTIAL'),
            ('Performance Review', 'Annual performance review - Exceeds expectations'),
            ('Vacation Plans', 'Planning trip to Hawaii in March')
        ]
        
        for title, content in bob_infos:
            cursor.execute('INSERT INTO infos (user_id, title, content) VALUES (?, ?, ?)',
                         (2, title, content))
    
    conn.commit()
    conn.close()

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not username or not password:
            flash('Please provide both username and password', 'danger')
            return render_template('login.html')
        
        hashed_pw = hashlib.sha256(password.encode()).hexdigest()
        
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?',
                      (username, hashed_pw))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to access this page', 'warning')
        return redirect(url_for('login'))
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM infos WHERE user_id = ?', (session['user_id'],))
    infos = cursor.fetchall()
    conn.close()
    
    return render_template('dashboard.html', infos=infos, username=session['username'])

@app.route('/info/<int:info_id>')
def view_info(info_id):
    if 'user_id' not in session:
        flash('Please log in to access this page', 'warning')
        return redirect(url_for('login'))
    
    conn = get_db()
    cursor = conn.cursor()
    # IDOR Vulnerability: No ownership check here
    cursor.execute('SELECT * FROM infos WHERE id = ?', (info_id,))
    info = cursor.fetchone()
    conn.close()
    
    if not info:
        flash('Information not found', 'danger')
        return redirect(url_for('dashboard'))
    
    return render_template('info.html', info=info)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=False)
