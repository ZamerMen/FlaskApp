from app import app
from flask import render_template, request, url_for
from models import db
from models import Plat, Block
from datetime import datetime

### расчетные модули раскладки ###
from Func.fbs import FBS
from Func.plat import plat_build

menu = [{'name':'Раскладка плит произвольной ширины', 'url':'plat'},
        {'name':'Раскладк блоков 3 типов заданной длинны: 900,1200,2400', 'url':'block'}]


@app.route('/')
def first_page():
    return render_template('index.html', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/video')
def video():
    return render_template('video.html')


@app.route('/block', methods=['post','get'])
def block():
    title = 'раскладка блоков'
    log_query = Block.query.order_by(Block.date.desc()).limit(5)
    return render_template('block.html', title=title, log_query=log_query)


@app.route('/block_result', methods = ['post','get'])
def block_result():
    width_block = request.form.get('width_block')
    try:
        width_block = int(width_block)
    except:
        return render_template('block_err.html', width_block=width_block)

    result = FBS(int(width_block))
    query_result = f'Длина участка раскладки:{width_block}'
    p = Block(data_query=query_result, date=datetime.utcnow())
    try:
        db.session.add(p)
        db.session.commit()
    except:
        return 'ошибка базы данных'
    return render_template('block_result.html', width_block=width_block, result=result)


@app.route('/plat', methods=['post','get'])
def plat():
    title = 'раскладка плит'
    # log_query = Plat.query.all()
    log_query = Plat.query.order_by(Plat.date.desc()).limit(5)
    return render_template('plat.html', title=title, log_query=log_query)


@app.route('/plat_result', methods = ['post','get'])
def plat_result():
    try:
        width1_plat = int(request.form.get('width1_plat'))
        width2_plat = int(request.form.get('width2_plat'))
        lenght_plat = int(request.form.get('lenght_plat'))
    except:
        return render_template('plat_err.html')

    result = plat_build(width1_plat, width2_plat, lenght_plat)
    query_result = f'ширина1:{width1_plat} ширина2:{width2_plat} длина раскладки:{lenght_plat}'
    p = Plat(data_query=query_result, date=datetime.utcnow())


    try:
        db.session.add(p)
        db.session.commit()
    except:
        return 'ошибка базы данных'
    return render_template('plat_result.html', result=result,width1_plat=width1_plat, width2_plat=width2_plat, lenght_plat=lenght_plat)
