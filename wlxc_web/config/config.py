import os



#配置文件路径
CONFIG_PATH = os.path.dirname(os.path.abspath(__file__))

#项目路径
ROOT_PATH = os.path.dirname(CONFIG_PATH)

#测试用例路径
CASE_PATH = os.path.join(ROOT_PATH,"tests")

#测试报告的路径
REPORTS_PATH = os.path.join(ROOT_PATH,"reports")

#测试数据路径
DATA_PATH = os.path.join(ROOT_PATH,"data")

#LOG数据路径
LOG_PATH = os.path.join(ROOT_PATH,"logs")

#selenium等待时间
WAIT_TIME = 20