from flask import Blueprint, render_template, request, url_for, redirect, session
lab4 = Blueprint('lab4', __name__)
 
@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')

@lab4.route('/lab4/div', methods=['GET', 'POST'])
def div():
    if request.method == 'GET':
        return render_template('lab4/div.html')
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены', back_url=url_for('lab4.lab'))
    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0:
        return render_template('lab4/div.html', error='Деление на 0 невозможно', back_url=url_for('lab4.lab'))
    
    result = x1 / x2
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result, back_url=url_for('lab4.div'))

@lab4.route('/lab4/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('lab4/add.html')
    x1 = request.form.get('x1') or '0'
    x2 = request.form.get('x2') or '0'
    if x1 == '' or x2 == '':
        return render_template('lab4/add.html', error='Оба поля должны быть заполнены', back_url=url_for('lab4.lab'))
    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0:
        return render_template('lab4/add.html', error='Деление на 0 невозможно', back_url=url_for('lab4.lab'))
    
    result = x1 + x2
    return render_template('lab4/add.html', x1=x1, x2=x2, result=result, back_url=url_for('lab4.add'))

@lab4.route('/lab4/minus', methods=['GET', 'POST'])
def minus():
    if request.method == 'GET':
        return render_template('lab4/minus.html')
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/minus.html', error='Оба поля должны быть заполнены', back_url=url_for('lab4.lab'))
    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0:
        return render_template('lab4/minus.html', error='Деление на 0 невозможно', back_url=url_for('lab4.lab'))
    
    result = x1 - x2
    return render_template('lab4/minus.html', x1=x1, x2=x2, result=result, back_url=url_for('lab4.minus'))

@lab4.route('/lab4/umnozh', methods=['GET', 'POST'])
def umnozh():
    if request.method == 'GET':
        return render_template('lab4/umnozh.html')
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/umnozh.html', error='Оба поля должны быть заполнены', back_url=url_for('lab4.lab'))
    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0:
        return render_template('lab4/umnozh.html', error='Деление на 0 невозможно', back_url=url_for('lab4.lab'))
    
    result = x1 * x2
    return render_template('lab4/umnozh.html', x1=x1, x2=x2, result=result, back_url=url_for('lab4.umnozh'))

@lab4.route('/lab4/stepen', methods=['GET', 'POST'])
def stepen():
    if request.method == 'GET':
        return render_template('lab4/stepen.html')
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/stepen.html', error='Оба поля должны быть заполнены', back_url=url_for('lab4.lab'))
    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0:
        return render_template('lab4/stepen.html', error='Деление на 0 невозможно', back_url=url_for('lab4.lab'))
    
    result = x1 ** x2
    return render_template('lab4/stepen.html', x1=x1, x2=x2, result=result, back_url=url_for('lab4.stepen'))

tree_count = 0
@lab4.route('/lab4/tree', methods = ['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)
    
    operation = request.form.get('operation')
    if operation == 'cut':
        tree_count -= 1
    elif operation == 'plant':
        tree_count +=1
    
    return redirect ('/lab4/tree')

@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            login = session['login']
            name = next(user['name'] for user in users if user['login'] == login)
        else:
            authorized = False
            login = ''
            name = ''
        return render_template('lab4/login.html', authorized=authorized, login=login, name=name)
    
    login = request.form.get('login')
    password = request.form.get('password')
    
    if not login:
        error = 'Не введён логин'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)
    if not password:
        error = 'Не введён пароль'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)
    
    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login  
            return redirect('/lab4/login') 
    
    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error=error, authorized=False, login=login)

@lab4.route('/lab4/logout', methods=['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')

users = [
    {'login': 'alex', 'password': '123', 'name': 'Alex Liks', 'gender': 'male'},
    {'login': 'bob', 'password': '555', 'name': 'Bob Wills', 'gender': 'male'},
    {'login': 'max', 'password': '321', 'name': 'Max Gilbert', 'gender': 'male'},
    {'login': 'jane', 'password': '777', 'name': 'Jane Rave', 'gender': 'female'},
]

@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    if request.method == 'GET':
        return render_template('lab4/fridge.html')

    temperature = request.form.get('temperature')
    if not temperature:
        error = 'Ошибка: не задана температура'
        return render_template('lab4/fridge.html', error=error)
    try:
        temp = float(temperature)
    except ValueError:
        error = 'Ошибка: температура должна быть числом'
        return render_template('lab4/fridge.html', error=error)
    snowflakes = None
    if temp < -12:
        message = 'Не удалось установить температуру — слишком низкое значение'
    elif temp > -1:
        message = 'Не удалось установить температуру — слишком высокое значение'
    elif -12 <= temp <= -9:
        message = f'Установлена температура: {temp}°С'
        snowflakes = 3  
    elif -8 <= temp <= -5:
        message = f'Установлена температура: {temp}°С'
        snowflakes = 2  
    elif -4 <= temp <= -1:
        message = f'Установлена температура: {temp}°С'
        snowflakes = 1  
    else:
        message = 'Неизвестная ошибка'
    return render_template('lab4/fridge.html', message=message, snowflakes=snowflakes)

corn = {
    'barley': {'name': 'ячмень', 'price': 12345},
    'oats': {'name': 'овёс', 'price': 8522},
    'wheat': {'name': 'пшеница', 'price': 8722},
    'rye': {'name': 'рожь', 'price': 14111}
}

@lab4.route('/lab4/order_grain', methods=['GET', 'POST'])
def order_grain():
    if request.method == 'POST':
        grain = request.form.get('grain')
        weight = request.form.get('weight')

        if not weight:
            message = "Ошибка: укажите вес заказа."
            return render_template('lab4/order_grain.html', message=message)
        
        try:
            weight = float(weight)
        except ValueError:
            message = "Ошибка: вес должен быть числом."
            return render_template('lab4/order_grain.html', message=message)
        
        if weight <= 0:
            message = "Ошибка: вес должен быть больше 0."
            return render_template('lab4/order_grain.html', message=message)
        
        if weight > 500:
            message = "Ошибка: такого объёма сейчас нет в наличии."
            return render_template('lab4/order_grain.html', message=message)
        
        grain_info = corn.get(grain)
        if not grain_info:
            message = "Ошибка: некорректный выбор зерна."
            return render_template('lab4/order_grain.html', message=message)
        
        price_per_ton = grain_info['price']
        grain_name_ru = grain_info['name']
        total_price = weight * price_per_ton

        discount_message = None
        if weight > 50:
            discount = 0.1  
            total_price *= (1 - discount)
            discount_message = "Применена скидка 10% за большой объём."

        message = f"Заказ успешно сформирован. Вы заказали {grain_name_ru}. Вес: {weight} т. Сумма к оплате: {total_price:.2f} руб."

        return render_template('lab4/order_grain.html', message=message, discount=discount_message)
    
    return render_template('lab4/order_grain.html')

@lab4.route('/lab4/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        name = request.form.get('name')
        if not login or not password or not name:
            error = 'Все поля обязательны для заполнения.'
            return render_template('lab4/register.html', error=error)
        
        if any(user['login'] == login for user in users):
            error = 'Логин уже занят.'
            return render_template('lab4/register.html', error=error)
        
        users.append({'login': login, 'password': password, 'name': name, 'gender': 'unknown'})
        return redirect('/lab4/login')
    
    return render_template('lab4/register.html')

@lab4.route('/lab4/users')
def users_list():
    if 'login' not in session:
        return redirect('/lab4/login')
    
    current_user = next(user for user in users if user['login'] == session['login'])
    return render_template('lab4/users.html', users=users, current_user=current_user)

@lab4.route('/lab4/delete', methods=['POST'])
def delete_user():
    login = request.form.get('login')
    users[:] = [user for user in users if user['login'] != login]
    session.pop('login', None)
    return redirect('/lab4/login')

@lab4.route('/lab4/edit', methods=['GET', 'POST'])
def edit_user():
    if 'login' not in session:
        return redirect('/lab4/login')
    
    current_user = next(user for user in users if user['login'] == session['login'])
    
    if request.method == 'POST':
        new_name = request.form.get('name')
        new_password = request.form.get('password')
        
        if new_name:
            current_user['name'] = new_name
        if new_password:
            current_user['password'] = new_password
        
        return redirect('/lab4/users')
    
    return render_template('lab4/edit.html', user=current_user)