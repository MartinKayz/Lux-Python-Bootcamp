from flask import Flask,render_template
# Flask uses render_template to render pages

app = Flask(__name__)


@app.route('/')
def index():
    return {'Message': 'Hello World'}


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')

# displaying some dynamic data
@app.route('/profile/<username>')
def profile(username):
    # user = None

    # if username in Users:
    #     user = Users[username]
    
    return f'Welcome to {username} profile'


richest = {
    'kubona': {
        'name' : 'Kubona Yafesi Martin',
        'bio' : 'founder of Kubona Investments',
        'Net Worth' : 10000
    },
    'muwaya': {
        'name' : 'Muwaya Moses Y',
        'bio' : 'founder of Muwaya Investments',
        'Net Worth' : 20000

    },
    'serina' : {
        'name' : 'Serina Banks',
        'bio' : 'founder of BankLadies Investments',
        'Net Worth' : 300000

    }
}



@app.route('/richest/<rich_name>')
def richest_people(rich_name):

    rich_person = None

    if rich_name in richest:
        rich_person = richest[rich_name]

    return render_template('profile.html', rich_name=rich_name, rich_person=rich_person)
    

if __name__ == '__main__':
    app.run(debug=True)