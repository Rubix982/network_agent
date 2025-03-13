import logging
import constants

def get_logger(filename: str):
    logger = logging.getLogger(filename)
    logging.basicConfig(filename=constants.NETWORK_AGENT_LOG_FILE, level=logging.DEBUG)
    return logger
