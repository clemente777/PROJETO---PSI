from flask import Flask, session, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

