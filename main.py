from flask import Flask
from database.routers.course_routers import bp  # 导入蓝图
from database.extensions import db

app = Flask(__name__)

# 注册蓝图！这是关键一步
app.register_blueprint(bp)

@app.route("/")
def testing():
    return "欢迎来到服务端！！！"


if __name__ == '__main__':
    app.run(debug=True)

