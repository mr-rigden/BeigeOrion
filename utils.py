import json
import logging
import logging.handlers
import os
import sys


def get_code_dir():
    return os.path.dirname(os.path.realpath(__file__))


config_file_path = os.path.join(get_code_dir(), "config.json")
f = open(config_file_path, "r")
CONFIG = json.load(f)
f.close()

log_path = os.path.join(get_code_dir(), "log.txt")
logger = logging.getLogger('BeigeOrion')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
logger.setLevel(logging.DEBUG)

file_handler = logging.handlers.RotatingFileHandler(log_path, maxBytes=5120)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
