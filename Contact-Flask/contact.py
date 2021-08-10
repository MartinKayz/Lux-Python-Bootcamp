from typing_extensions import TypeGuard
from flask import Flask, render_template,request
from flask_mysqldb import MySQL


contact_me = Flask(__name__)
mysql = MySQL(contact_me)


# loading all my enviroment variables from secret file
contact_me.config.from_pyfile('settings.py')

# route to our home page
@contact_me.route('/')
def home():
    return render_template('index.html')

# route to our contact page, with form
@contact_me.route('/contact', methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        name = data['name']
        email = data['email']
        message = data['message']
        # creating a cursor object to enable connection to database, and making SQL queries
        curso = mysql.connection.cursor()
        curso.execute('INSERT INTO userdata (name, email, message) VALUES (%s, %s, %s)', (name, email, message))
        # Until now we have to manually commit our queries to the database
        mysql.connection.commit()
        # never forget to close the cursor object
        curso.close()
        return 'Success your message has been sent successfully'
    return render_template('contact.html')

# handling non-existent pages
@contact_me.errorhandler(404)
def page_not_found(error):
    return render_template('error_404_page.html'), 404


if __name__ == '__main__':
    contact_me.run(debug=True)