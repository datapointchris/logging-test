import logging

logger = logging.getLogger(__name__)

print('LOADED ANYWAY')

def logme():
    logger.info('This is an info log')
