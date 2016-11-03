# coding: utf-8

import sys
import logging


def get_stdout_logger(name, fd=sys.stdout, level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers = []

    ch = logging.StreamHandler(fd)
    ch.setLevel(level)
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
