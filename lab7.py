from flask import Blueprint, render_template, request, abort

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def main ():
    return render_template('lab7/lab7.html')

films = [
    {
        "title": "Intouchables",
        "title_ru": "1+1",
        "year": 2011,
        "description": "Аристократ на коляске нанимает в сиделки бывшего заключенного. \
        Искрометная французская комедия с Омаром Си"
    },
    {
        "title": "Interstellar",
        "title_ru": "Интерстеллар",
        "year": 2014,
        "description": "Когда засуха, пыльные бури и вымирание растений приводят человечество \
        к продовольственному кризису, коллектив исследователей и учёных отправляется сквозь \
        червоточину (которая предположительно соединяет области пространства-времени через большое расстояние) \
        в путешествие, чтобы превзойти прежние ограничения для космических путешествий человека и найти планету с \
        подходящими для человечества условиями."
    },
    {
        "title": "The Gentlemen",
        "title_ru": "Джентльмены",
        "year": 2019,
        "description": "Один ушлый американец ещё со студенческих лет приторговывал наркотиками, а теперь придумал схему \
        нелегального обогащения с использованием поместий обедневшей английской аристократии и очень неплохо на этом разбогател. \
        Другой пронырливый журналист приходит к Рэю, правой руке американца, и предлагает тому купить киносценарий, в котором подробно \
        описаны преступления его босса при участии других представителей лондонского криминального мира — партнёра-еврея, китайской диаспоры, \
        чернокожих спортсменов и даже русского олигарха."
    },
    {
        "title": "Inception",
        "title_ru": "Начало",
        "year": 2010,
        "description": "Кобб – талантливый вор, лучший из лучших в опасном искусстве извлечения: он крадет ценные секреты из глубин подсознания во \
        время сна, когда человеческий разум наиболее уязвим. Редкие способности Кобба сделали его ценным игроком в привычном к предательству мире промышленного \
        шпионажа, но они же превратили его в извечного беглеца и лишили всего, что он когда-либо любил."
    },
    {
        "title": "The Wolf of Wall Street",
        "title_ru": "Волк с Уолл-стрит",
        "year": 2013,
        "description": "1987 год. Джордан Белфорт становится брокером в успешном инвестиционном банке. Вскоре банк закрывается после внезапного обвала индекса Доу-Джонса.\
        По совету жены Терезы Джордан устраивается в небольшое заведение, занимающееся мелкими акциями. Его настойчивый стиль общения с клиентами и врождённая харизма \
        быстро даёт свои плоды. Он знакомится с соседом по дому Донни, торговцем, который сразу находит общий язык с Джорданом и решает открыть с ним собственную фирму. \
        В качестве сотрудников они нанимают нескольких друзей Белфорта, его отца Макса и называют компанию «Стрэттон Оукмонт». В свободное от работы время Джордан прожигает \
        жизнь: лавирует от одной вечеринки к другой, вступает в сексуальные отношения с проститутками, употребляет множество наркотических препаратов, в том числе кокаин и кваалюд. \
        Однажды наступает момент, когда быстрым обогащением Белфорта начинает интересоваться агент ФБР..."
    }
]
@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return films

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if id < 0 or id >= len(films):
        abort(404)
    return films[id] 