import datetime
import inspect
import logging
import os

import pytest
import toml

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.mark.usefixtures('setup')
class TestBase:
    @staticmethod
    def get_logger():
        logger = logging.getLogger(inspect.stack()[1][3])
        # prevent duplicate logging
        if logger.hasHandlers():
            logger.handlers.clear()
        # file handler object
        date_now = datetime.datetime.now()
        date = str(date_now.year) + str(date_now.month) + str(date_now.day)
        file_handler = logging.FileHandler(
            filename=f'{ROOT_DIR}\\..\\output\\logfile_{date}.log',
            mode='a',
            encoding='UTF-8',
        )
        file_format = logging.Formatter(
            '%(asctime)s %(name)-30s %(levelname)-10s %(message)s'
        )
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def get_config(group, value):
        filename = 'test_variables.toml'
        try:
            config = toml.load(f'{ROOT_DIR}\\{filename}')
            return config.get(group).get(value)
        except IOError:
            print(f'{filename} not found!')
        return None
