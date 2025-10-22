from  ..extensions import db


class Sc(db.Model):
    # 指定表名 成绩表
    __tablename__ = 'SC'
    S_id = db.Column(db.String(100), db.ForeignKey('Student.S_id')) # 学生表主键
    C_id = db.Cloumn(db.String(100), db.ForeignKey('Course.C_id')) # 课程表主键
    score = db.Column(db.String(100)) # 课程对应分数
