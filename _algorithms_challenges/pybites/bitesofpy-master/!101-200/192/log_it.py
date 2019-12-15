import logging
from typing import Callable

logger = logging.getLogger('pybites_logger')
DEBUG = lambda x: logger.log(logging.DEBUG, x)
INFO = lambda x: logger.log(logging.INFO, x)
WARNING = lambda x: logger.log(logging.WARNING, x)
ERROR = lambda x: logger.log(logging.ERROR, x)
CRITICAL = lambda x: logger.log(logging.CRITICAL, x)


def log_it(level: Callable, msg: str) -> None:
    level(msg)


if __name__ == "__main__":
    log_it(DEBUG, "This is a debug message.")
    log_it(INFO, "This is an info message.")
    log_it(WARNING, "This is a warning message.")
    log_it(ERROR, "This is an error message.")
    log_it(CRITICAL, "This is a critical message.")
