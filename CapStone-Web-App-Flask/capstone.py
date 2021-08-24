from flask import Flask,request
from flask.templating import render_template
from flask_migrate import Migrate
from models import db, TrialData

capstone_app = Flask(__name__)


capstone_app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Idocareboss@13@localhost:5432/flask_db"
capstone_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(capstone_app)
migrate = Migrate(capstone_app, db)



@capstone_app.route('/')
def index():
    return render_template('index.html')

@capstone_app.route('/form')
def form():
    return render_template('form.html')


@capstone_app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        new_user = TrialData(name=name, age=age)
        db.session.add(new_user)
        db.session.commit()
        return f"Done!!"
    #return render_template('form.html')


if __name__ == '__main__':
    capstone_app.run(debug=True)