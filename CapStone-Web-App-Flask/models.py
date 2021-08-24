from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TrialData(db.Model):
    __tablename__ = 'trial_data'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
 
    def __init__(self, name,age):
        self.name = name
        self.age = age
 
    def __repr__(self):
        return f"{self.name}:{self.age}"

