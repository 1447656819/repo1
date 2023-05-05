from urllib.parse import urlencode

from common import yaml_handler, excel_handler, logging_handler,requests_handler
from common.mysql_handler import Mysqlhandler
from config import config
import os
import jsonpath




class Handler():
    """初始化所有的数据，在其他模块中可重复使用
    要求是从common中实例化的对象"""

    #加载python配置项
    conf = config

    #加载yaml数据
    yaml = yaml_handler.read_yaml(os.path.join(config.CONFIG_PATH,"config.yml"))

    #加载excel数据
    __excel_path = conf.DATA_PATH
    __excel_file = yaml["excel"]["file"]
    excel = excel_handler.ExcelHandler(os.path.join(__excel_path,__excel_file))

    #加载logger
    __logger_config = yaml['logger']
    logger = logging_handler.get_logger(
        name=__logger_config["name"],
        file=os.path.join(config.LOG_PATH, __logger_config["file"]),
        logger_level=__logger_config["logger_level"],
        stream_level=__logger_config["stream_level"],
        file_level=__logger_config["file_level"])
    


if __name__ == '__main__':
    pass

