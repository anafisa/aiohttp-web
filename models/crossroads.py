from . import db


class Crossroad(db.Model):
    __tablename__= 'crossroads'

    crossroad_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime(timezone=True), nullable=False)
    location = db.Column(db.Text, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    map = db.Column(db.LargeBinary, nullable = False)
    description = db.Column(db.Text, nullable=False)
    votes_number = db.Column(db.Integer, nullable=False)
    status = db.Column(db.VARCHAR(200), nullable=False)
    user_id = db.Column(db.VARCHAR(200), db.ForeignKey('users.user_id'))

