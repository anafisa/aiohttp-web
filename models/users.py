from . import db


class User(db.Model):
    __tablename__= 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.VARCHAR(200), nullable=False)
    password = db.Column(db.VARCHAR(200), nullable=False)
    name = db.Column(db.VARCHAR(200), nullable=False)
    sex = db.Column(db.VARCHAR(15), nullable=False)
    city = db.Column(db.VARCHAR(200), nullable=False)
    address = db.Column(db.VARCHAR(200), nullable=False)
    mobile = db.Column(db.VARCHAR(200), nullable=False)
    role = db.Column(db.Text, nullable=False)
