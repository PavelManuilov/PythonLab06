import LR06database as db
from flask import Flask, render_template

app = Flask(__name__)

#тестирование GitHub
@app.route('/')
@app.route('/index')
def index():
    text = '''
    <a href=/init>инициализация БД</a>
    <br>
    <a href=/view>просмотр БД</a>
    '''
    return text


@app.route('/init')
def init():
    db.initTableLR06('Lab_Rab_06')
    return 'БД инициализирована'


@app.route('/view')
def view():
    try:
        text = ''
        xconn = db.openDB()
        #text += '<!--1-->'
        dat = [{'datetime': '2024-01-01', 'description': 'НГ'},
               {'datetime': '2024-05-09', 'description': 'День Победы'}
               ]
        #text += '<!--2-->'

        dat=db.getTable(xconn,'Lab_Rab_06')
        for zap in dat:
            zap['datetime']=(zap['datetime']+' ').split(' ')[0] # берём только дату без времени



        text += render_template('view.in.html',
                                title=6,
                                var1=dat)
        #text += '<!--3-->'

        return text
        #return 'пока пусто'
    except Exception as e:

        return f'''<font color="red">
        <h1>ошибка {e}
        </h1>
        </font>
        '''
    finally:
        db.closeDB(xconn)
        #text += 'finally'

    return text


if __name__ == "__main__":
    #app.run(host='0.0.0.0')
    app.run()
