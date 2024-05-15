import time

from src.logger import stru_logger


def timeit(func):
    """
    Decorator that measures the execution time of a function.
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        stru_logger.info(f"{func.__name__} took {duration:.4f} seconds.")
        return result

    return wrapper
