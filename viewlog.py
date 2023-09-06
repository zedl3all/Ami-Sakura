"""Viewlog"""
import inspect
import os
import logging

# Configure logging settings
logging.basicConfig(filename=r'.\log\run.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', encoding='utf-8')

# Define a decorator to log return values
def log_return_value(func):
    """retuen log"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        calling_frame = inspect.currentframe().f_back
        calling_file = os.path.basename(inspect.getframeinfo(calling_frame).filename)
        logging.info(f"{func.__name__} called from file: {calling_file} returned: {result}")
        return result
    return wrapper
