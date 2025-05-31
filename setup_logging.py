__znacka__ = 'setup_logging'
__description__ = 'TODO: Add description here'


import logging

def setup_logging(log_file="application.log"):
    """
    Nastaví základní logování aplikace.
    :param log_file: Soubor, kam se budou ukládat logy.
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename=log_file)
    logger = logging.getLogger()
    return logger


def run(task):
    # TODO: implement task processing logic
    return f'Result from {__znacka__} for task: {task}'