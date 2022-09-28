from typing import List, Dict
from flask import Flask, render_template, jsonify
import mysql.connector
import json

app=Flask(__name__,template_folder='templates')

@app.route('/mangas')
def mangas():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'goodreads'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM mangas')
    results = cursor.fetchall()
    cursor.close()
    connection.close()

    return results


""" @app.route('/')
def index():
   return json.dumps({'favorite_colors': favorite_colors()}) """

@app.route('/')
def index():
    return render_template('index.html', data=mangas())
    #    return render_template('index.html', data=json.dumps({'mangas': mangas()}))



if __name__ == '__main__':
    app.run(host='0.0.0.0')