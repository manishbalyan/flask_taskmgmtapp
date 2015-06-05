import sqlite3
from _config import DATABASE_PATH
with sqlite3.connect(DATABASE_PATH) as connection:
	# get a cursor object used to execute a sql command
	c = connection.cursor()

	# create the table

	c.execute(""" CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL, status INTEGER NOT NULL)""")
	
	# insert dummy data into the table
	# don't include task_id into insert command bc it is autoincrement value ie it is auto generated with each new row of data 
	c.execute('INSERT INTO tasks (name, due_date, priority, status)' 'VALUES ("Finish this tutorial", "03/25/2015", 10, 1)')
	c.execute('INSERT INTO tasks (name, due_date, priority, status)' 'VALUES ("Finish Real Python Course 2", "03/25/2015", 10, 1)')