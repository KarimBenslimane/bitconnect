import logging
from logging.handlers import RotatingFileHandler

class Logger:
    logger = None

    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.ERROR)
        handler = RotatingFileHandler("var/log/"+name+".log", maxBytes=100000, backupCount=5)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, message):
        self.logger.error(message)