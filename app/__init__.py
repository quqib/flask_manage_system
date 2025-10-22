"""
package的初始化
管理package接口
package的信息
"""
import logging
import os
from logging.handlers import RotatingFileHandler

# 配置日志
def setLogging(app):
    # 日志级别
    app.logger.setLevel(logging.DEBUG)
    # 创建日志记录器
    log_dir = os.path.join(os.getcwd(), 'log') # 查找当前目录下的日志文件
    os.makedirs(log_dir, exist_ok=True) # 如果不存在就创建一个
    # 设置日志文件路径
    log_path = os.path.join(log_dir, 'flask_test.log')
    # 创建日志处理器写入日志文件
    file_handler = RotatingFileHandler(log_path, maxBytes=10 * 1024 * 1024, backupCount=10, encoding='utf-8')
    # 设置日志格式
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    # 将处理器添加到日志记录器
    app.logger.addHandler(file_handler)


# 配置ORM
def setORM(app):
    pass

# 初始化FlaskSession
def initFlaskSession(app):
    pass

# 创建app(注册蓝图)
def createApp(app):



    # 配置日志
    setLogging(app)

    pass
