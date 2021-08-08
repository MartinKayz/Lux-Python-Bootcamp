from typing_extensions import TypeGuard
from flask import Flask, render_template,request

from flaskext.mysql import MySQL



contact_me = Flask(__name__)
mysql = MySQL(contact_me)


contact_me.config['MYSQL_DATABASE_USER'] = 'root'
contact_me.config['MYSQL_DATABASE_PASSWORD'] = 'Idocareboss@13'
contact_me.config['MYSQL_DATABASE_DB'] = 'Contactdb'
contact_me.config['MYSQL_DATABASE_HOST'] = 'localhost'

conn = mysql.connect()




@contact_me.route('/')
def home():
    return render_template('index.html')


@contact_me.route('/contact', methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        name = data['name']
        email = data['email']
        message = data['message']
        cursor = conn.cursor()
        cursor.execute('INSERT INTO userdata (name, email, message) VALUES (%s, %s)', (name, email, message))
        mysql.connection.commit()
        cursor.close()
        return 'Success'
    return render_template('contact.html')


if __name__ == '__main__':
    contact_me.run(debug=True)