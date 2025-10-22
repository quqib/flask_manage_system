from ..repositories.course_repository import CourseRepository


class CourseService:

    @staticmethod
    def get_courses():
        return CourseRepository.get_all()

    @staticmethod
    def get_course(C_id):
        return CourseRepository.get_by_id(C_id)


    @staticmethod
    def create_course():
        # 可以在这里加上业务校验

        pass




