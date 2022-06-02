import logging
import allure


def custom_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('../reports/log.log', mode='w')
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s', datefmt='%d/%m/%y %H:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


def allure_logs(text):
    with allure.step(text):
        pass
