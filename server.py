from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/movie', methods=['POST'])
def movie():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    title = request.form['title']
    rating = request.form['rating']
    genre = request.form['genre']

    try:
        cursor.execute('INSERT INTO movies(title, rating, genre) VALUES (?, ?, ?)', (title, rating, genre))
        connection.commit()
        message = "Successfully inserted into movies table"
    except:
        connection.rollback()
        message = 'There was an issue inserting the data'
    finally:
        connection.close()
        return message


# @app.route('movies')
# def movies():
