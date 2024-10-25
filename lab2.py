from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2/a/')
def a():
    return 'без слэша'


@lab2.route('/lab2/a/')
def a2():
    return 'со слэшем'


all_flower_list = [
    {'name': 'пион', 'kolvo': 19},
    {'name': 'ромашка', 'kolvo': 17},
    {'name': 'хризантема', 'kolvo': 10},
    {'name': 'сирень', 'kolvo': 3},
]


@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(all_flower_list):
        return "такого цветка нет ", 404
    else:
        return render_template('addflower.html', flower_id=flower_id, flower=all_flower_list[flower_id])
    

@lab2.route ('/lab2/flowers/<name>')
def add_flower(name):
    for flower in all_flower_list:
        if flower['name'] == name:
            return f"Цветок с именем {name} уже существует.", 400
    all_flower_list.lab2end({'name': name, 'kolvo': 1})  
    return redirect(url_for('all_flowers'))


@lab2.route('/lab2/flower/')
def no_flower():
    return "Вы не задали имя цветка", 400   


@lab2.route('/lab2/all_flowers')
def all_flowers():
    return render_template('flowers.html', all_flower_list=all_flower_list)


@lab2.route('/lab2/flowers/clear')
def clear_flowers():
    all_flower_list.clear()
    return redirect(url_for('all_flowers'))

@lab2.route('/lab2/example')
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
    return render_template('example.html', name=name, numberLab=numberLab,
                           groupStudent=groupStudent, numberCourse=numberCourse, 
                           fruits=fruits)


@lab2.route('/lab2/')
def lab2():
    return render_template('lab2.html')


@lab2.route('/lab2/filters')
def filters():
    phrase = 'О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных...'
    return render_template('filter.html', phrase = phrase)

@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    return render_template('calc.html', a=a, b=b)


@lab2.route('/lab2/calc/')
def calc_without_numbers():
    return redirect(url_for('calc', a=1, b=1))


@lab2.route('/lab2/calc/<int:a>/')
def calc_with_a(a):
    return redirect(url_for('calc', a=a, b=1))

book_list = [
        {'author': 'Маргарет Митчелл', 'name': 'Унесенные ветром', 'genre': 'Роман', 'str': '704'}, 
        {'author': 'Лев Толстой', 'name': 'Война и мир', 'genre': 'Роман', 'str': '1225'},
        {'author': 'Фёдор Достоевский', 'name': 'Преступление и наказание', 'genre': 'Роман', 'str': '430'},
        {'author': 'Анна Ахматова', 'name': 'Реквием', 'genre': 'Поэзия', 'str': '200'},
        {'author': 'Александр Пушкин', 'name': 'Евгений Онегин', 'genre': 'Поэма', 'str': '500'},
        {'author': 'Габриэль Гарсия Маркес', 'name': 'Сто лет одиночества', 'genre': 'Роман', 'str': '417'},
        {'author': 'Френсис Скотт Фицджеральд', 'name': 'Великий Гэтсби', 'genre': 'Роман', 'str': '180'},
        {'author': 'Джордж Оруэлл', 'name': '1984', 'genre': 'Роман', 'str': '328'},
        {'author': 'Коэльо Пауло', 'name': 'Алхимик', 'genre': 'Роман', 'str': '208'},
        {'author': 'Даниэль Дефо', 'name': 'Робинзон Крузо', 'genre': 'Роман', 'str': '320'},
        {'author': 'Тургенев Иван', 'name': 'Отцы и дети', 'genre': 'Роман', 'str': '280'}
    ]


@lab2.route('/lab2/books')
def books():
    return render_template('books.html', book_list=book_list)


cars = [
    {
        "name": "Rolls-Royce Phantom",
        "image": "Rolls-Royce Phantom.jpg",
        "description": "Флагманская модель британского бренда. Воплощение роскоши и комфорта."
    },
    {
        "name": "Bentley Continental GT",
        "image": "Bentley Continental GT.jpg",
        "description": "Элегантное купе с мощным двигателем и динамичными характеристиками."
    },
    {
        "name": "Aston Martin DB11",
        "image": "Aston Martin DB11.jpg",
        "description": "Стильный и современный спортивный автомобиль с фирменным дизайном Aston Martin."
    },
    {
        "name": "Mercedes-Benz S-Class",
        "image": "Mercedes-Benz S-Class.jpg",
        "description": "Флагманский седан Mercedes-Benz, воплощение роскоши и технологичности."
    },
    {
        "name": "Maserati Ghibli",
        "image": "Maserati Ghibli.jpg",
        "description": "Итальянский седан с мощным двигателем и стильным дизайном."
    }
]


@lab2.route('/lab2/cars')
def cars_page():
    return render_template('cars.html', cars=cars)