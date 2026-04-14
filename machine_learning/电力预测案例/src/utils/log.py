# 设置日志输出

import logging
import os

class Logger(object):
    levels_relations = {
        'debug': logging.DEBUG, 'info': logging.INFO,
        'warning': logging.WARNING, 'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(self, root_path, log_name, level='info', fmt='%(asctime)s - %(levelname)s: %(message)s'):
        self.root_path = root_path
        self.log_name = log_name
        self.fmt = fmt
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(self.levels_relations.get(level))

    def get_logger(self):
        path = os.path.join(self.root_path, 'log')
        os.makedirs(path, exist_ok=True)
        file_name = os.path.join(path, self.log_name + '.log')
        file_handler = logging.FileHandler(file_name, encoding='utf-8', mode='a')
        formatter = logging.Formatter(self.fmt)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

        return self.logger
    


