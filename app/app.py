from flask import Flask, jsonify, request
import os
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
            host=os.environ.get('MYSQL_HOST', 'mysql'),
            user=os.environ.get('MYSQL_USER', 'root'),
            password=os.environ.get('MYSQL_PASSWORD', 'root'),
            database=os.environ.get('MYSQL_DATABASE', 'test_db')
        )

@app.route('/api/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM data')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@app.route('/api/data', methods=['POST'])
def add_data():
    new_data = request.json.get('data')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO data (data) VALUES (%s)', (new_data,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Data added!'}), 201

#@app.route

if __name__ == '__main__':
    app.run(host='0.0.0.0')