import logging
import time


class MyLog:

    @staticmethod
    def my_log(msg, level, file_path):
        # 定义日志收集器 my_logger
        my_logger = logging.getLogger()
        # 设定级别
        my_logger.setLevel("INFO")
        # 设置日志输出格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        # 创建输出渠道
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)
        console_handler.setFormatter(formatter)
        file_handle = logging.FileHandler(file_path, encoding="utf-8")
        file_handle.setLevel(logging.INFO)
        file_handle.setFormatter(formatter)
        # 两者对接--指定输出渠道
        my_logger.addHandler(console_handler)
        my_logger.addHandler(file_handle)
        # 收集日志
        if level == "DEBUG":
            my_logger.debug(msg)
        elif level == "ERROR":
            my_logger.error(msg)
        elif level == "INFO":
            my_logger.info(msg)
        elif level == "WARNING":
            my_logger.warning(msg)
        else:
            my_logger.critical(msg)
        my_logger.removeHandler(console_handler)
        my_logger.removeHandler(file_handle)


if __name__ == '__main__':
    MyLog().my_log("sto 今天有点萌萌滴1", "ERROR", r"../report/logs/test_log.log")
    MyLog().my_log("sto 今天有点萌萌滴2", "INFO", r"../report/logs/test_log.log")
