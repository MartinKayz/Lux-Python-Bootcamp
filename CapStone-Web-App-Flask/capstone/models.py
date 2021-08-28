# to be used later on
from capstone import db


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



class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
