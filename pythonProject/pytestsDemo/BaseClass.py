import inspect
import logging


class BaseClass:
    def getLogger(self):
        loggerName=inspect.stack()[1][3]

        logger = logging.getLogger(__name__)

        fileHandler = logging.FileHandler('logifle.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)

        return logger

