from typing import List, Dict
from flask import Flask, render_template, request, flash, redirect
import mysql.connector
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

# READ ALL MANGA
def mangas():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM mangas')
    results = cursor.fetchall()
    cursor.close()
    connection.close()

    return results

# LIST MANGA
@app.route('/mangas')
def listMangas():
    return render_template('mangas.html', data=mangas())

# CREATE		
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
    

# FORMULAIRE ADD
@app.route('/add_manga')
def add_manga_form():
	return render_template('manga_form.html')

# AFFICHER UN MANGA
@app.route('/manga/<int:id>', methods=["GET"])
def manga_view(id):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mangas WHERE id=%s", (id,))
    row = cursor.fetchone()
    cursor.execute("SELECT * FROM mangas a join manga_genre b on a.id = b.manga_id join genres c on b.genre_id = c.id  where a.id=%s", (id,))
    genres = cursor.fetchall()
    conn.commit()
    if row:
        cursor.close()
        conn.close()
        return render_template('manga.html', row=row, genres=genres)
    else:
        cursor.close()
        conn.close()
        return 'Error loading #{id}'.format(id=id)

# FORMULAIRE UPDATE
@app.route('/update_manga/<int:id>', methods=["GET"])
def add_manga_form_update(id):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mangas WHERE id=%s", (id,))
    row = cursor.fetchone()
    conn.commit()
    if row:
        cursor.close()
        conn.close()
        return render_template('manga_form_update.html', row=row)
    else:
        cursor.close()
        conn.close()
        return 'Error loading #{id}'.format(id=id)

# UPDATE
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
		

# DELETE
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