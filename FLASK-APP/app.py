from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World, Martin!'


@app.route('/page/<int:page_num>')
def content(page_num):
    return f'<h1>Yoo.. It is your page {page_num}</h1>'

if __name__ == '__main__':
    app.run(host='',port='',debug=True)