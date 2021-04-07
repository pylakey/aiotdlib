import logging
from functools import wraps
from time import perf_counter

logger = logging.getLogger('measure_time')


def measure_time(func: callable):
    func_name = getattr(func, '__qualname__', '') or getattr(func, '__name__', '???')

    @wraps(func)
    def decorated(*args, **kwargs):
        start_time = perf_counter()

        try:
            return func(*args, **kwargs)
        finally:
            end_time = perf_counter() - start_time
            logger.info(f"{func_name} call finished in {end_time} seconds")

    return decorated
