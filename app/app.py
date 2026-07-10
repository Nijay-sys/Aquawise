from flask import Flask, render_template, request, redirect
from utils import get_db_connection, DB_PATH
import sqlite3

app = Flask(__name__, template_folder='templates')

def initialize_sqlite_database():
    """Automatically builds the database file and table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS water_telemetry (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            ph REAL NOT NULL,
            turbidity REAL NOT NULL,
            hardness REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-data', methods=['POST'])
def submit_data():
    ph = request.form['ph']
    turbidity = request.form['turbidity']
    hardness = request.form['hardness']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO water_telemetry (ph, turbidity, hardness) VALUES (?, ?, ?)",
        (ph, turbidity, hardness)
    )
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect('/')

if __name__ == '__main__':
    initialize_sqlite_database() 
    app.run(port=5000, debug=True)