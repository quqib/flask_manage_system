from ..extensions import db


class Teacher(db.Model):
    __tablename__ = 'Teacher'

    T_id = db.Column(db.String(100), primary_key=True)
    Tname = db.Column(db.String(100))