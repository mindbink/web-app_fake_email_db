from flask import Flask
from flask import request, jsonify, redirect, render_template
import mysql.connector
from selenium import webdriver

config = {'user'	:'root',
		  'host'	:'localhost',
		  'password':'687510bnm',
		  'database':'simple'}

# connect to database
def mysql_connect():
	conn = mysql.connector.connect(**config)
	cursor = conn.cursor()
	count = cursor.execute('SELECT COUNT(*) FROM users')
	count = cursor.fetchall()
	cursor.close()
	return count[0][0]

app = Flask(__name__)
app.config['DEBUG'] = True

# home page
@app.route('/', methods=['GET'])
def home():
	app.static_folder = 'static'
	emails_in_db = mysql_connect()
	return render_template('home_page.html', count=emails_in_db)

# error handler
@app.errorhandler(404)
def page_not_found(e):
	return '<h1>404</h1><p>The page could not be found.</p>', 404

# insert new email into database
@app.route('/register/', methods=['POST'])
def register():
	email = request.form['email']
	conn = mysql.connector.connect(**config)
	cursor = conn.cursor()
	query = 'INSERT INTO users (email) VALUES (%s)'
	cursor.execute(query, (email,))
	conn.commit()
	return redirect('/')

if __name__ == "__main__":
	app.run()
