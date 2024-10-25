from flask import Blueprint, render_template, request, make_response, redirect, url_for
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name')
    age = request.cookies.get('age')
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, name_color=name_color, age=age)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response (redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response (redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors={}
    user = request.args.get('user')
    if user == '':
        errors['user']= 'Заполните поле!'
    age = request.args.get('age')
    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)

@lab3.route('/lab3/order')
def order():
        return render_template('lab3/order.html')
@lab3.route('/lab3/pay')
def pay():
        price=0
        drink = request.args.get('drink')
        #Пусть кофе стоит 120 рублей, черный чай - 80 рублей, зеленый - 70 рублей.
        if drink == 'coffee':
             price= 120
        elif drink == 'black-tea':
             price = 80
        else:
             price=70
        #Добавка молодка удорожает напиток на 30 рублей, а сахар - на 10.
        if request.args.get('milk') == 'on':
             price += 30
        if request.args.get('sugar') == 'on':
             price += 10
        return render_template('lab3/pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    price = request.args.get('price')
    return render_template('lab3/success.html', price=price)

@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    if color:
        resp = make_response(redirect('/lab3/settings'))
        resp.set_cookie('color', color)
        return resp
    
    color = request.cookies.get('color')
    resp = make_response(render_template('lab3/settings.html', color=color))
    return resp


@lab3.route('/lab3/train_ticket')
def train_ticket():
    passenger_name = request.args.get('passenger_name')
    shelf_type = request.args.get('shelf_type')
    with_bedding = request.args.get('with_bedding')
    with_luggage = request.args.get('with_luggage')
    age = request.args.get('age')
    departure_point = request.args.get('departure_point')
    destination_point = request.args.get('destination_point')
    travel_date = request.args.get('travel_date')
    insurance_needed = request.args.get('insurance_needed')
    if passenger_name and shelf_type and age and departure_point and destination_point and travel_date:
        age = int(age)
        
        ticket_price = 1000 if age >= 18 else 700  
        if shelf_type in ['lower', 'lower_side']:
            ticket_price += 100
        if with_bedding == 'on':
            ticket_price += 75
        if with_luggage == 'on':
            ticket_price += 250
        if insurance_needed == 'on':
            ticket_price += 150
        ticket_type = "Детский билет" if age < 18 else "Взрослый билет"
        return render_template('lab3/ticket.html', 
                               passenger_name=passenger_name, 
                               ticket_type=ticket_type,
                               ticket_price=ticket_price,
                               departure_point=departure_point,
                               destination_point=destination_point,
                               travel_date=travel_date)
    return render_template('lab3/train_ticket.html')


@lab3.route('/lab3/clearCookie')
def clear_cookie():
    cookies_to_clear = ['bg_color', 'color', 'font_size']
    response = make_response(redirect('/lab3')) 
    
    for cookie in cookies_to_clear:
        if cookie in request.cookies:
            response.set_cookie(cookie, '', expires=0)
    
    return response


khl_teams = [
    {'name': 'СКА Санкт-Петербург', 'city': 'Санкт-Петербург', 'ticket_price': 2500, 'founded': 1946},
    {'name': 'ЦСКА Москва', 'city': 'Москва', 'ticket_price': 2400, 'founded': 1946},
    {'name': 'Ак Барс', 'city': 'Казань', 'ticket_price': 2200, 'founded': 1956},
    {'name': 'Металлург Магнитогорск', 'city': 'Магнитогорск', 'ticket_price': 2000, 'founded': 1955},
    {'name': 'Авангард Омск', 'city': 'Омск', 'ticket_price': 2300, 'founded': 1950},
    {'name': 'Динамо Москва', 'city': 'Москва', 'ticket_price': 2100, 'founded': 1946},
    {'name': 'Локомотив Ярославль', 'city': 'Ярославль', 'ticket_price': 1900, 'founded': 1959},
    {'name': 'Салават Юлаев', 'city': 'Уфа', 'ticket_price': 1800, 'founded': 1961},
    {'name': 'Трактор Челябинск', 'city': 'Челябинск', 'ticket_price': 1700, 'founded': 1947},
    {'name': 'Спартак Москва', 'city': 'Москва', 'ticket_price': 2000, 'founded': 1946},
    {'name': 'Амур', 'city': 'Хабаровск', 'ticket_price': 1500, 'founded': 1966},
    {'name': 'Барыс', 'city': 'Астана', 'ticket_price': 1600, 'founded': 1999},
    {'name': 'Северсталь', 'city': 'Череповец', 'ticket_price': 1400, 'founded': 1956},
    {'name': 'Нефтехимик', 'city': 'Нижнекамск', 'ticket_price': 1300, 'founded': 1968},
    {'name': 'Адмирал', 'city': 'Владивосток', 'ticket_price': 1700, 'founded': 2013},
    {'name': 'Динамо Минск', 'city': 'Минск', 'ticket_price': 1600, 'founded': 1976},
    {'name': 'Куньлунь Ред Стар', 'city': 'Пекин', 'ticket_price': 1800, 'founded': 2016},
    {'name': 'Сибирь Новосибирск', 'city': 'Новосибирск', 'ticket_price': 1500, 'founded': 1962},
    {'name': 'Витязь Подольск', 'city': 'Подольск', 'ticket_price': 1400, 'founded': 1996},
    {'name': 'Торпедо Нижний Новгород', 'city': 'Нижний Новгород', 'ticket_price': 1600, 'founded': 1947}
]


@lab3.route('/lab3/search')
def search():
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')
    if min_price is None and max_price is None:
        return render_template('/lab3/search.html')
    min_price = float(min_price) if min_price else 0
    max_price = float(max_price) if max_price else float('inf')
    # Фильтруем автомобили по диапазону цен
    filtered_khl_teams = [khl for khl in khl_teams if min_price <= khl['ticket_price'] <= max_price]
    # Отображаем результат поиска
    return render_template('/lab3/results.html', khl=filtered_khl_teams, min_price=min_price, max_price=max_price)
# Страница результатов
@lab3.route('/lab3/results')
def results():
    return render_template('lab3/results.html')