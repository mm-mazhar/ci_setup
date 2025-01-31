import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import logging

from utils import add

from logConfigs import load_dictConfig

logger = logging.getLogger("app.logs")

logger.info("***app.py***")


def run_task():
    logger.warning("Running a task inside src/app/app.py")
    logger.info("This info message won't be logged since level is WARNING")


if __name__ == "__main__":
    run_task()
    logger.info(add(1, 2))

# msg deleted
