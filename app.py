from flask import Flask, redirect, url_for, render_template
import os
from os import path
from flask_sqlalchemy import SQLAlchemy
from db import db
from urllib.parse import quote
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8

app = Flask (__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'Секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

if app.config['DB_TYPE'] == 'postgres':
    db_user = 'olya_barkhatova_own'
    db_password = '123'
    db_name = 'olya_barkhatova_own'
    host_ip = '127.0.0.1'
    host_port = 5432
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'
else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, "olya_barkhatova_own.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{db_path}'
db.init_app(app)

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return """
<!DOCTYPE html>
<html lang="ru">
<head>
    <title>НГТУ ФБ, Лабораторные работы</title>
</head>
<body>
    <header>
        НГТУ ФБ, WEB-программирование, часть 2. Список лабораторных  
    </header>

    <h1>web-сервер на flask</h1>
    <li><a href="http://127.0.0.1:5000/lab1">Первая лабораторная</a></li>
    <li><a href="http://127.0.0.1:5000/lab2">Вторая лабораторная</a></li>
    <li><a href="http://127.0.0.1:5000/lab3">Третья лабораторная</a></li>
    <li><a href="http://127.0.0.1:5000/lab4">Четвертая лабораторная</a></li>
    <li><a href="http://127.0.0.1:5000/lab5">Пятая лабораторная</a></li>  
    <li><a href="http://127.0.0.1:5000/lab6">Шестая лабораторная</a></li> 
    <li><a href="http://127.0.0.1:5000/lab7">Седьмая лабораторная</a></li> 
    <li><a href="/lab8">Восьмая лабораторная</a></li>  
    <footer>
        &copy: Бархатова Ольга, ФБИ-24, 3 курс, 2024
    </footer>
</body>
</html>
"""

@app.errorhandler(404)
def not_found_404(err):
    return '''
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        <h2>Ошибка 404 - такой страницы не существует</h2>
        <footer>
            &copy; Бархатова Ольга, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''


@app.errorhandler(500)
def not_found_500(err):
    return '''
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        <h2>Ошибка 500 - сервер не смог обработать запрос</h2>
        <footer>
            &copy; Бархатова Ольга, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''