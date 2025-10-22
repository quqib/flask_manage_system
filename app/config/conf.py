import os.path
import shutil
import sys

"""
    项目临时文件配置类
"""
class FlaskTempFile:
    # 通过获取主程序路径，最后拼成临时文件存放目录（这个参数返回的是当前执行的脚本的名字）
    mainPyPath = sys.argv[0]
    # 父文件路径
    mainParentPath = os.path.dirname(mainPyPath)
    # 临时文件路径
    temPath = mainParentPath + os.sep + 'temFile'

    @classmethod
    def iniTemDir(cls):
        """
        初始化创建临时文件目录 并清空临时文件目录的项
        :return:
        """
        cls.creatTemDir()
        cls.cleanTemDir()
        pass


    @classmethod
    def delTemDir(cls):
        pass


    @classmethod
    def cleanTemDir(cls):
        shutil.rmtree(cls.mainParentPath)
        pass


    @classmethod
    def creatTemDir(cls):
        pass


    @classmethod
    def getTemFile(cls):
        pass




