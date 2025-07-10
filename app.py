from flask import Flask, session, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash
import sqlite3

DATABASE = 'banco.sql'
conn = sqlite3.connect('banco.db')
with open(DATABASE) as f:
    conn.executescript(f.read())
conn.commit()
conn.close()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

