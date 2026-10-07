from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/o-skole')
def about_school():
    return "Toto je stránka o škole."


@app.route('/student/<name>')
def contact(name):
    return f"Toto je stránka o studentovi {name}."

@app.route('/soucet/<int:a>/<int:b>')
def sum_numbers(a, b):
    return f"Součet čísel {a} a {b} je {a + b}."    