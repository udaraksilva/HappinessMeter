

from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import datetime

app = Flask(__name__)
CORS(app)

# Database connection helper
def get_db_connection():
    conn = sqlite3.connect('employees.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    emp_id = data.get('employee_id')
    conn = get_db_connection()
    employee = conn.execute('SELECT * FROM employees WHERE employee_id = ?', (emp_id,)).fetchone()
    conn.close()
    if employee:
        return jsonify({"success": True, "name": employee["first_name"]})
    return jsonify({"success": False, "message": "Employee not found"}), 401

@app.route('/api/vote', methods=['POST'])
def vote():
    data = request.json
    emp_id = data.get('employee_id')
    vote = data.get('vote')
    timestamp = datetime.datetime.now().isoformat()
    conn = get_db_connection()
    conn.execute('INSERT INTO votes (employee_id, vote, timestamp) VALUES (?, ?, ?)', (emp_id, vote, timestamp))
    conn.commit()
    conn.close()
    return jsonify({"success": True, "message": "Vote submitted"})

@app.route('/api/meter', methods=['GET'])
def meter():
    conn = get_db_connection()
    happy = conn.execute("SELECT COUNT(*) FROM votes WHERE vote = 'happy'").fetchone()[0]
    sad = conn.execute("SELECT COUNT(*) FROM votes WHERE vote = 'sad'").fetchone()[0]
    conn.close()
    return jsonify({"happy": happy, "sad": sad})

if __name__ == '__main__':
   if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=10000)

