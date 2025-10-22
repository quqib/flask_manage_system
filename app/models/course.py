from ..extensions import db

class Course(db.Model):
    # 指定表名 课程表
    __tablename__ = 'course'
    C_id = db.Column(db.String(100), primary_key=True) # 课程主键
    Cname = db.Column(db.String(100)) # 课程名称
    T_id = db.Column(db.String(100), db.ForeignKey('Teacher.T_id')) # 教师表主键
