from flask import Flask, redirect, url_for, render_template
app = Flask (__name__)

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

@app.route('/lab1/oak')
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

@app.route('/lab1/student')
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

@app.route('/lab1/python')
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

@app.route('/lab1/new_year')
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
@app.route('/lab2/a/')
def a():
    return 'без слэша'

@app.route('/lab2/a/')
def a2():
    return 'со слэшем'

all_flower_list = [
    {'name': 'пион', 'kolvo': 19},
    {'name': 'ромашка', 'kolvo': 17},
    {'name': 'хризантема', 'kolvo': 10},
    {'name': 'сирень', 'kolvo': 3},
]

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(all_flower_list):
        return "такого цветка нет ", 404
    else:
        return render_template('addflower.html', flower_id=flower_id, flower=all_flower_list[flower_id])
    
@app.route ('/lab2/flowers/<name>')
def add_flower(name):
    for flower in all_flower_list:
        if flower['name'] == name:
            return f"Цветок с именем {name} уже существует.", 400
    all_flower_list.append({'name': name, 'kolvo': 1})  
    return redirect(url_for('all_flowers'))
@app.route('/lab2/flower/')
def no_flower():
    return "Вы не задали имя цветка", 400   
@app.route('/lab2/all_flowers')
def all_flowers():
    return render_template('flowers.html', all_flower_list=all_flower_list)
@app.route('/lab2/flowers/clear')
def clear_flowers():
    all_flower_list.clear()
    return redirect(url_for('all_flowers'))

@app.route('/lab2/example')
def example ():
    name = 'Бархатова Ольга'
    numberLab = '2'
    groupStudent = 'ФБИ-24'
    numberCourse = '3 курс'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    return render_template('example.html', 
                           name=name, numberLab=numberLab, groupStudent=groupStudent, 
                           numberCourse=numberCourse, fruits=fruits)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
    phrase = 'О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных...'
    return render_template('filter.html', phrase = phrase)

@app.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    return render_template('calc.html', a=a, b=b)
@app.route('/lab2/calc/')
def calc_without_numbers():
    return redirect(url_for('calc', a=1, b=1))
@app.route('/lab2/calc/<int:a>/')
def calc_with_a(a):
    return redirect(url_for('calc', a=a, b=1))