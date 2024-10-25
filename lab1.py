from flask import Blueprint, redirect, url_for
lab1 = Blueprint ('lab1', __name__)


@lab1.route("/lab1/")
def lab():
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
        <div>
            <a href="http://127.0.0.1:5000/menu"></a>
            <a href="http://127.0.0.1:5000/menu" class='backmenu'>Меню</a>
        </div>
        <h2>
            Реализованные роуты
        </h2>
        <ul>
            <li><a href="http://127.0.0.1:5000/lab1/oak">Дуб</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/student">Студент</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/python">Python</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/new_year">Атмосфера нового года</a></li>
        </ul>
        <footer>
            &copy; Бархатова Ольга, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''


@lab1.route('/lab1/oak')
def oak():
    return '''
<!doctype html>
<html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <h1 style='padding-left: 15px'>Дуб</h1>
        <img src="''' + url_for('static', filename='dyb.jpg') + '''" class='dyb'>
    </body>
</html>
'''


@lab1.route('/lab1/student')
def student():
    return '''
<!doctype html>
<html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <h1>Бархатова Ольга Викторовна</h1>
        <img src="''' + url_for('static', filename='nstu.png') + '''" class='nstu'>
        <div>
            <a href="http://127.0.0.1:5000/lab1" class='backmenu'>Назад</a>
        </div>
    </body>
</html>
'''


@lab1.route('/lab1/python')
def python():
    return '''
<!doctype html>
<html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <h1>Python</h1>
        <p>
            Первая версия Python была разработана в 1991 году программистом из Нидерландов Гвидо ван Россумом. В настоящее время выходят новые версии языка, которые расширяют его возможности, а сам он занимает верхние строчки рейтингов языков программирования. Python применяется во многих сферах: веб-разработка, анализ данных и машинное обучение и др.
        </p>
        <p>
            Главное достоинство Python — простота синтаксиса и команд, а также большое количество библиотек, которые содержат уже написанный программный код для решения широкого спектра задач. Python даже применяют в своих исследованиях и разработках специалисты, чьи профессии напрямую не связаны с программированием. Один из самых частых примеров — применение Python для анализа большого количества данных и нахождения корреляции между ними.
        </p>
        <img src="''' + url_for('static', filename='python.jpg') + '''" class='python'>
        <div>
            <a href="http://127.0.0.1:5000/lab1" class='backmenu'>Назад</a>
        </div>
    </body>
</html>
'''


@lab1.route('/lab1/new_year')
def new_year():
    return '''
<!doctype html>
<html>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <h1>Атмосфера нового года</h1>
        <p>
        Обычай отмечать Новый год в ночь с 31 декабря на 1 января появился в России при Петре I. До этого, с принятия христианства в 988 году, его отмечали 1 марта, а в 1492 году датой начала года закрепили 1 сентября. Тогда летоисчисление шло по византийской системе, «от сотворения мира» — то есть от 5508 года до нашей эры.
        </p>
        <p>
        В конце декабря 1699 года Петр I издал именной указ № 1736 «О праздновании Нового года». Он ввел новую систему исчисления — от Рождества Христова, и 7208 год «от сотворения мира» стал 1700 годом. =
        </p>
        <img src="''' + url_for('static', filename='new_year.jpg') + '''" class='new_year'>
        <div>
            <a href="http://127.0.0.1:5000/lab1" class='backmenu'>Назад</a>
        </div>
    </body>
</html>
'''


@lab1.errorhandler(404)
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


@lab1.errorhandler(500)
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