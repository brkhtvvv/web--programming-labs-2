from flask import Blueprint, render_template, request, url_for
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