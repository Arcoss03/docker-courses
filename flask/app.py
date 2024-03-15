from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)
print(os.getenv('DB_USER'),)

def get_posts():
    cnx = mysql.connector.connect(
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)
    cursor = cnx.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Posts")

    posts = cursor.fetchall()

    cursor.close()
    cnx.close()

    return jsonify(posts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)