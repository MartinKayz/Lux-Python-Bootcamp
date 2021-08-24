from flask import Flask,request
from flask import templating
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy


capstone_app = Flask(__name__)


ENV = 'dev'

if ENV == 'dev':
    capstone_app.debug = True
    capstone_app.config.from_pyfile('settings.py')
else:
    capstone_app.debug = False
    capstone_app.config.from_pyfile('settings.py')


capstone_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(capstone_app)

class TrialData(db.Model):
    __tablename__ = 'trial_data'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), unique=True)
    prog_lang = db.Column(db.String(100))
    # rating = db.Column(db.String(10))
    comments = db.Column(db.Text())
 
    def __init__(self, name,prog_lang,comments):
        self.name = name
        self.prog_lang = prog_lang
        # self.rating = rating
        self.comments = comments


 
    def __repr__(self):
        return f"{self.name}:{self.prog_lang}:{self.comments}"







@capstone_app.route('/')
def index():
    return render_template('index.html')

@capstone_app.route('/form')
def form():
    return render_template('form.html')


@capstone_app.route('/submit', methods = ['POST'])
def submit():
  
    if request.method == 'POST':
        name = request.form['name']
        prog_lang = request.form['program-language']
        comments = request.form['comments']
        print(name, prog_lang, comments, sep=' ')
        if name == '' or prog_lang == '':
            return render_template('form.html', message='Please Enter the required data')
        #if user does not exit, enter data! else flash message
        if db.session.query(TrialData).filter(TrialData.name == name).count() == 0:

            data = TrialData(name,prog_lang,comments)
            db.session.add(data)
            db.session.commit()
            return render_template('success.html')
        return render_template('form.html', message='You are already in the system!!!')


if __name__ == '__main__':
    capstone_app.run(debug=True)