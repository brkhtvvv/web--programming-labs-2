from flask import Flask
app = Flask (__name__)

@app.route("/")
@app.route("/index")
def start():
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

    <footer>
        &copy: Бархатова Ольга, ФБИ-24, 3 курс, 2024
    </footer>
</body>
</html>
"""

@app.route("/lab1")
def lab1():
    return '''
<!doctype html>
<html>
    <head>
        <title>Бархатова Ольга Викторовна, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>
        <p>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </p>
        <footer>
            &copy; Бархатова Ольга, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''