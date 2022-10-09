from typing import List, Dict
from flask import Flask, render_template, request, flash, redirect, jsonify
from flask_cors import CORS, cross_origin
import mysql.connector
import sys

app=Flask(__name__,template_folder='templates')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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

# ---------------------------------- MANGA ------------------------------------------

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
    cursor.execute("SELECT name FROM mangas a join manga_genre b on a.id = b.manga_id join genres c on b.genre_id = c.id  where a.id=%s", (id,))
    genres = cursor.fetchall()
    cursor.execute("SELECT * FROM reviews a join reviews_manga b on a.id = b.reviews_id join mangas c on b.manga_id = c.id  where c.id=%s", (id,))
    reviews = cursor.fetchall()
    conn.commit()
    if row:
        cursor.close()
        conn.close()
        return render_template('manga.html', row=row, genres=genres, reviews=reviews)
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

# ---------------------------------- USERS ------------------------------------------

# READ ALL USERS
def users():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    results = cursor.fetchall()
    cursor.close()
    connection.close()

    return results

@app.route('/users')
def list_users():
    return render_template('users.html', users=users())


    
# ---------------------------------- API MANGA ------------------------------------------

# LIST MANGA API
@app.route('/api/mangas')
def listMangasAPI():

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM mangas')
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    rv = cursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    cursor.close()
    connection.close()

    return jsonify(json_data)

# AFFICHER UN MANGA API
@app.route('/api/mangas/<int:id>', methods=["GET"])
def manga_view_api(id):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mangas WHERE id=%s", (id,))
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    row = cursor.fetchone()
    conn.commit()
    json_data=[]
    if row:
        json_data.append(dict(zip(row_headers,row)))
        cursor.close()
        conn.close()
        return jsonify(json_data)
    else:
        cursor.close()
        conn.close()
        return 'Error loading #{id}'.format(id=id)

# AFFICHER LES GENRES D'UN MANGA API
@app.route('/api/mangas/<int:id>/genres', methods=["GET"])
def manga_view_genres_api(id):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM mangas a join manga_genre b on a.id = b.manga_id join genres c on b.genre_id = c.id  where a.id=%s", (id,))
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    genres = cursor.fetchall()
    conn.commit()
    json_data=[]
    if genres:
        for result in genres:
            json_data.append(dict(zip(row_headers,result)))
        cursor.close()
        conn.close()
        return jsonify(json_data)
    else:
        cursor.close()
        conn.close()
        return 'Error loading #{id}'.format(id=id)

# AFFICHER LES REVIEWS D'UN MANGA API
@app.route('/api/mangas/<int:id>/reviews', methods=["GET"])
def manga_view_reviews_api(id):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT review FROM reviews a join reviews_manga b on a.id = b.reviews_id join mangas c on b.manga_id = c.id  where c.id=%s", (id,))
    reviews = cursor.fetchall()
    conn.commit()
    if reviews:
        cursor.close()
        conn.close()
        return jsonify(reviews)
    else:
        cursor.close()
        conn.close()
        return 'Error loading #{id}'.format(id=id)

if __name__ == '__main__':
    app.run(host='0.0.0.0')