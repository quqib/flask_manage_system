from ..extensions import db
from ..models.course import Course


class CourseRepository:

    @staticmethod
    def get_all():
        return Course.query.all()


    @staticmethod
    def get_by_id(C_id):
        return Course.query.get_or_404(C_id)


    @staticmethod
    def create_course(username, email):
        pass


    @staticmethod
    def update_course():
        pass

    @staticmethod
    def delete_course(C_id):
        course = Course.query.get_or_404(C_id)
        db.session.delete(course)
        db.session.commit()

