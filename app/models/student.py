from ..extensions import db


class Student(db.Model):
    __tablename__ = 'Student'
    S_id = db.Column(db.String(100), primary_key=True)
    Sname = db.Column(db.String(100))
    Sage = db.Column(db.DATETIME)
    Ssex = db.Column(db.String(10))
