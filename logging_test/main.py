import logging
import log
from next_to_main import logme
from subfolder import below_main


logger = logging.getLogger(__name__)
logger.warning('Main app')

logme()
below_main.dothing()