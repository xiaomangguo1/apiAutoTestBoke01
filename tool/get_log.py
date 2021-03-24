# 导包
import logging.handlers
import os

from config import BASE_PATH


class GetLog:
    __logger = None

    @classmethod
    def get_log(cls):
        if cls.__logger is None:
            # 获取日志器
            cls.__logger = logging.getLogger()
            # 设置日志器级别
            cls.__logger.setLevel(logging.INFO)
            # 获取处理器控制台
            sh = logging.StreamHandler()
            # 获取处理器文件-以时间分隔
            log_path = BASE_PATH +os.sep+"log"+os.sep+"dsshop.log"
            th = logging.handlers.TimedRotatingFileHandler(filename=log_path,
                                                           when='M',
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding='utf-8')
            # 设置格式器
            fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)] - %(message)s'
            fm = logging.Formatter(fmt)
            # 将格式器添加到控制台处理器
            sh.setFormatter(fm)
            # 将格式器添加到文件处理器
            th.setFormatter(fm)
            # 将处理器添加到日志
            cls.__logger.addHandler(sh)
            cls.__logger.addHandler(th)
        return cls.__logger


# 执行信息
if __name__ == '__main__':
    logger = GetLogger.get_logger()
    logger.info("正在执行info")
    logger.error("正在执行error")
