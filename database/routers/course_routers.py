from flask import Blueprint, request, jsonify
from ..services.course_service import CourseService

bp = Blueprint('course', __name__, url_prefix='/api/course')

@bp.route('', methods=['POST'])
def create_course():
    # 这种获取到的是字典类型 使用key value进行获取
    data = request.json
    print(data)
    print(type(data))
    try:

        return jsonify(f"成功！！！{data}"), 201
    except Exception as e:
        return jsonify({f"课程创建失败,失败原因{e}"}), 400



