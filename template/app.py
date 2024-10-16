
from dataclasses import dataclass
from distutils.log import debug
from fileinput import filename
import random
import string
import pandas as pd
from flask import *
import os
from werkzeug.utils import secure_filename


 
UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads')
 
# Define allowed files
ALLOWED_EXTENSIONS = {'csv'}
 
app = Flask(__name__)
 
# Configure upload file path flask
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 
app.secret_key = 'This is your secret key to utilize session in Flask'

Data=[]
ru_columns={'id':'ид','name':'имя','d1':'д1','d2':'д2'}
@dataclass
class Data1():
    id:int
    name:str
    d1:float
    d2:float
    def to_dict(self):
        '''Представляет экземпляр класса в виде словаря'''
        return {i_attr:self.__getattribute__(i_attr) for i_attr in self.get_headers()}
    def get_headers_(self):
        '''Представляет наименование полей класса в виде словаря'''
        return (i_attr for i_attr in [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("_")])
    @classmethod
    def get_headers(col):
        return {k:k for k,v in __class__.__annotations__.items()}


def init_data():
    Data.clear()
    for i in range(10):
        Data.append(Data1(
            id=random.randint(0, 100),
            name=''.join(random.choices(string.ascii_letters, k=7)),
            d1=random.uniform(10, 20),
            d2=random.uniform(10, 20)
            ))



@app.route('/', methods=['GET', 'POST'])
def root():
    # if request.method == 'POST':
    #   # upload file flask
    #     f = request.files.get('file')
 
    #     # Extracting uploaded file name
    #     data_filename = secure_filename(f.filename)
 
    #     f.save(os.path.join(app.config['UPLOAD_FOLDER'],
    #                         data_filename))
 
    #     session['uploaded_data_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'],
    #                  data_filename)
 
    #     return render_template('index2.html',data_filename=data_filename)
    return render_template("index.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
      # upload file flask
        f = request.files.get('file')
 
        # Extracting uploaded file name
        data_filename = secure_filename(f.filename)
 
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],
                            data_filename))
 
        session['uploaded_data_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'],
                     data_filename)
 
        return render_template('index2.html',data_filename=data_filename)
    return render_template("upload_file.html")

@app.route('/clipboard')
def clipboard():
    return render_template("from_clipboard.html")


@app.route("/api1",  methods = ['POST','GET','PUT'])
def hello():
    v_in=request.get_json()
    print(type(v_in))
    # return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
    data = {'message': 'Done', 'code': 'SUCCESS'}
    return make_response(jsonify(data), 201)


@app.route('/show_data')
def show_data():
    '''
    формирует html данные
    '''
    init_data()
    new_columns=Data[0].get_headers()
    # print(new_columns)
    for col in Data[0].get_headers():
        # print(col,ru_columns[col])
        new_columns[col]=ru_columns[col]
        pass
    return render_template('show_data.html',
                           column_names=new_columns,# column_names,
                           flows=Data)

@app.route('/export_data')
def export_data():

    '''формирует данные для xlsx'''

    file_name=os.path.join(app.config['UPLOAD_FOLDER'],'test_data.xlsx')
    init_data()
    
    df=pd.DataFrame(Data)
    new_columns=Data[0].get_headers()
    for col in Data[0].get_headers():
        # print(col,ru_columns[col])
        new_columns[col]=ru_columns[col]
    # print(new_columns)
    df=df[['d1','name','d2','id']]
    df.rename(columns=new_columns,inplace=True)
    df.to_excel(file_name, index=False,sheet_name='Тестовые данные')
    return redirect("/")


# @app.route('/show_input')
# def show_input():
#     profile=[Profile(123,0.5),Profile(321,0.3)]
#     aapp=App()
#     aapp.file_pips='D:\\repos\\Pipesim_\\test-pipesim2020.2.pips'
#     aapp.load_pips()
#     column_names=['Начало','Конец','Ветвь',	
#                   'Труба','Длина','Высота','Диаметр внешний',
#                   'Толщина стенки','Шерох','Темп-ра','Коэф тепл']
#     # return render_template('show_input.html',flows=['flow1','flow2','flow3'])
#     # print(aapp.Pipes)
#     return render_template('show_input.html',
#                            column_names=list(aapp.Pipes),# column_names,
#                            flows=aapp.Pipes)

@app.route('/excel_from_clipboard')
def from_clipboard():
    return render_template('from_clipboard.html')

if __name__ == '__main__':
    app.run(debug=True)
