import logging

from logConfigs import load_dictConfig

logger = logging.getLogger("app.logs")


def add(x, y) -> str:
    logger.warning("*utils.py* --> Adding two numbers inside src/app/utils/utils.py")
    return x + y
