# -*- coding: utf-8 -*-
# """
# app.py
# Created on Dec 17, 2024
# @ Author: Mazhar
# """


import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import logging

from utils import add

from configs import load_logConfigs

load_logConfigs()
logger = logging.getLogger("app.logs")
logger.info("***app.py***")


def run_task():
    logger.warning("Running a task inside src/app/app.py")
    logger.info("This info message won't be logged since level is WARNING")
    logger.error("This error message will be logged")


if __name__ == "__main__":
    run_task()
    logger.info(add(1, 2))
