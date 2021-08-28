from flask import request
from flask import templating
from flask.templating import render_template
from capstone.models import User, TrialData
from capstone.forms import RegistrationForm, LoginForm
from capstone import capstone_app, db


@capstone_app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    return render_template('register.html', title='Register', form=form)


@capstone_app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    return render_template('login.html', title='Welcome Back', form=form)



@capstone_app.route('/')
def index():
    return render_template('index.html',title='Home')

@capstone_app.route('/form')
def form():
    return render_template('form.html',title='Feedback form')

# Render all my posts from dev.to
def devPosts():
    pass


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
