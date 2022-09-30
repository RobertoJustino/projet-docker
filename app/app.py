from typing import List, Dict
from flask import Flask, render_template, request, flash, redirect
import mysql.connector
import json
import sys

app=Flask(__name__,template_folder='templates')

app.secret_key = 'secret key'

config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'goodreads'
}

@app.route('/')
def index():
    return render_template('index.html')

def mangas():
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


@app.route('/manga/<int:id>', methods=["GET"])
def manga_view(id):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mangas WHERE id=%s", (id,))
    row = cursor.fetchone()
    conn.commit()
    print(row, file=sys.stderr)
    if row:
        cursor.close()
        conn.close()
        return render_template('manga.html', row=row)
    else:
        cursor.close()
        conn.close()
        return 'Error loading #{id}'.format(id=id)

@app.route('/update_manga')
def add_manga_form_update():
	return render_template('manga_form_update.html')


@app.route('/manga/update', methods=['POST'])
def update_manga():
    _title = request.form['inputTitle']
    _image = request.form['inputImage']
    _auteur = request.form['inputAuteur']
    _description = request.form['inputDescription']
    _year = request.form['inputYear']
    _id = request.form['id']
	# validate the received values
    if _title and _image and _auteur and _description and _year and request.method == 'POST':
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        sql = "UPDATE mangas SET title=%s, img_src=%s, author=%s, description=%s, year=%s WHERE id=%s"
        data = (_title, _image, _auteur, _description, _year, _id)
        cursor.execute(sql, data)
        conn.commit()
        flash('User updated successfully!')
        cursor.close()
        conn.close()
        return redirect('/manga/' + _id)
    else:
        cursor.close()
        conn.close()
        return 'Error while updating user'
		


@app.route('/manga/delete/<int:id>')
def delete_user(id):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM mangas WHERE id=%s", (id,))
    conn.commit()
    flash('User deleted successfully!')
    cursor.close() 
    conn.close()
    return redirect('/mangas')
    


if __name__ == '__main__':
    app.run(host='0.0.0.0')