from flask import Flask, render_template, request, jsonify
import pymysql
from urllib.parse import quote as url_quote

app = Flask(__name__)

# MySQL configurations
db_host = "db"
db_user = "root"
db_password = "password"
db_name = "mydatabase"

# Connect to MySQL
db = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_name, cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()

# Create table if not exists
create_table_query = """
    CREATE TABLE IF NOT EXISTS user_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL
    );
"""
cursor.execute(create_table_query)
db.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']

    # Insert user data into the database
    insert_query = f"INSERT INTO user_data (name, email) VALUES ('{name}', '{email}')"
    cursor.execute(insert_query)
    db.commit()

    return render_template('index.html', message='User added successfully')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
