from typing import List, Dict
from flask import Flask, render_template, request, flash, redirect
import mysql.connector
import json

app=Flask(__name__,template_folder='templates')

app.secret_key = 'secret key'

@app.route('/')
def index():
    return render_template('index.html')

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

@app.route('/mangas')
def listMangas():
    return render_template('mangas.html', data=mangas())

		
@app.route('/manga/create', methods=['POST'])
def add_manga():
    _title = request.form['inputTitle']
    _image = request.form['inputImage']
    _auteur = request.form['inputAuteur']
    _description = request.form['inputDescription']
    _year = request.form['inputYear']
	# validate the received values
    if _title and _image and _auteur and _description and _year and request.method == 'POST':
		# save edits
        config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'goodreads'
        }
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        sql = "INSERT INTO mangas(title, img_src, author, description, year) VALUES(%s, %s, %s, %s, %s)"
        data = (_title, _image, _auteur, _description, _year)
        cursor.execute(sql, data)
        conn.commit()
        flash('User added successfully!')
        cursor.close()
        conn.close()
        return redirect('/mangas')
    else:
        cursor.close()
        conn.close()
        return 'Error while adding user'
    

@app.route('/add_manga')
def add_manga_form():
	return render_template('manga_form.html')


@app.route('/manga/<int:id>')
def manga_view(id):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'goodreads'
    }
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mangas WHERE id= '%s'", id)
    conn.commit
    row = cursor.fetchone()
    if row:
        cursor.close()
        conn.close()
        return render_template('manga.html', row=row)
    else:
        cursor.close()
        conn.close()
        return 'Error loading #{id}'.format(id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0')