import logging

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s | %(name)s:%(lineno)d | %(levelname)s: %(message)s")

ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)  # Exporting logs to the screen

fh = logging.FileHandler(filename='logtest.log')
fh.setFormatter(formatter)
logger.addHandler(fh)  # Exporting logs to a file

logger.debug(f"Log level set: {logger.level}")