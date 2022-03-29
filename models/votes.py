from . import db


class Vote(db.Model):
    __tablename__= 'votes'

    vote_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    crossroad_id = db.Column(db.Integer, db.ForeignKey('crossroads.crossroad_id'))