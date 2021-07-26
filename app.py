from faker import Faker
import mysql.connector

config = {'user':'root',
		  'password':'687510bnm',
		  'host':'localhost'}


def create_db(db_name):
	try:
		cursor.execute('CREATE DATABASE {}'.format(db_name))
	except Exception as e:
		print(e)
	cursor.execute('USE {}'.format(db_name))


def create_table():
	try:
		query = '''CREATE TABLE users (
			email VARCHAR(255) PRIMARY KEY,
			created_at TIMESTAMP DEFAULT NOW()
			)'''
		cursor.execute(query)
	except Exception as e:
		print(e)
	

def fake_names_dates(conn):
	fake = Faker()
	fake_name = fake.email()
	fake_date = fake.date_time_between(start_date='-5y')
	query_names = '''INSERT INTO users (email, created_at)
			VALUES (%s, %s)'''

	cursor.execute(query_names, (fake_name, fake_date))
	conn.commit()


def connect_db(db_name):
	conn = mysql.connector.connect(**config)
	global cursor
	cursor = conn.cursor()
	create_db(db_name)
	create_table()
	try:
		for _ in range(500):
			fake_names_dates(conn)
	except Exception as e:
		pass

connect_db('simple')



