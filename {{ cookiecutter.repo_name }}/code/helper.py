"""
General helper file with functions relevant across use cases.

"""
import logging
import configparser

def get_logger(level='info', location = None, excl_az_storage=True):
    """Get runtime logger"""
    global logger

    # Exceptions
    if excl_az_storage:
        logging.getLogger("azure.storage.common.storageclient").setLevel(logging.WARN)

    # Level
    if level == 'info':
        _level = logging.INFO
    elif level == 'debug':
        _level = logging.DEBUG
    elif level == 'warning':
        _level = logging.WARNING

    # Format
    logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                    datefmt = '%m/%d/%Y %H:%M:%S',
                    level = _level)

    # Location
    if location is None:
        logger = logging.getLogger(__name__)
    else:
        logger = logging.getLogger(location)

    return logger

def get_config():
    """Load local config file"""
    control_header = 'maps'
    # Get config
    run_config = configparser.ConfigParser()
    run_config.read('../config.ini')
    if control_header not in run_config:
        run_config.read('./config.ini')
    if control_header not in run_config:
        logging.warning('[ERROR] Could not find correct config.ini.')
    return run_config