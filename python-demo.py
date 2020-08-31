import os
import logging 
import numpy as np

root = logging.getLogger()
if root.handlers:
    for handler in root.handlers:
        root.removeHandler(handler)
logging.basicConfig(format='%(asctime)s %(message)s',level=logging.DEBUG)

def handler(event, context):
    logging.info('hello')
    logging.info(np.array([1, 2, 3]))
    return {
        'status': 200,
        'message': 'hello world!'
    }