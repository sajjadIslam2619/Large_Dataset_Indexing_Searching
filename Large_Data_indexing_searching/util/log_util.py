from functools import wraps
import logging
import os


def logger(original_func):
    logging.basicConfig(filename=os.path.join(os.getcwd(), '..', 'info.log'), level=logging.INFO)

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        logging.info('{} Ran with args: {}, and kwargs: {}'.format(original_func.__name__, args, kwargs))
        return original_func(*args, **kwargs)

    return wrapper


def spent_time_measure(original_func):
    import time

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = original_func(*args, **kwargs)
        end_time = time.time()
        spent_time = end_time - start_time
        logging.info('{} ran in: {} sec'.format(original_func.__name__, spent_time))

        return result

    return wrapper


import time


@logger
@spent_time_measure
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))
