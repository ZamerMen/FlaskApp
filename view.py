from app import app
from flask import render_template, request, url_for


# расчетные модули
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
    return render_template('block.html', title=title)


@app.route('/block_result', methods = ['post','get'])
def block_result():
    width_block = request.form.get('width_block')
    try:
        width_block = int(width_block)
    except:
        return render_template('block_err.html', width_block=width_block)

    print('длина участка стены равна', width_block)
    result = FBS(int(width_block))
    print(result)
    return render_template('block_result.html', width_block=width_block, result=result)


@app.route('/plat', methods=['post','get'])
def plat():
    title = 'раскладка плит'
    return render_template('plat.html', title=title)

@app.route('/plat_result', methods = ['post','get'])
def plat_result():
    try:
        width1_plat = int(request.form.get('width1_plat'))
        width2_plat = int(request.form.get('width2_plat'))
        lenght_plat = int(request.form.get('lenght_plat'))
    except:
        return render_template('plat_err.html')

    result = plat_build(width1_plat, width2_plat, lenght_plat)
    return render_template('plat_result.html', result=result,
                           width1_plat=width1_plat, width2_plat=width2_plat, lenght_plat=lenght_plat)
