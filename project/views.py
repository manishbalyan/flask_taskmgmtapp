# imports
from flask import Flask , render_template, request, session, flash, redirect, url_for, g

import sqlite3
from functools import wraps

# config
app = Flask(__name__)


app.config.from_object('_config')

# helper function
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash('You need to login first')
			return redirect(url_for('login'))
	return wrap	

# route handlers
@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('Goodbye!')
	return redirect(url_for('login'))

@app.route('/', methods = ['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid Credentials. Please try again.'
		else:
			session['logged_in'] = True
			return redirect(url_for('main'))
		return render_template('login.html', error = error)	
			
	return render_template('login.html')

