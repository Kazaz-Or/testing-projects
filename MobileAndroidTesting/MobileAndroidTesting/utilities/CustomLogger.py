import inspect
import logging
import os.path


def custom_logger():
    info = inspect.stack()[1][0]
    log_name = os.path.basename(info.f_locals["__file__"]).replace(".py", "")
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('../reports/testlog.log', mode='w')
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s', datefmt='%d/%m/%y %H:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
