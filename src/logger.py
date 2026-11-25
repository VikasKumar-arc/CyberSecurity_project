import logging
logging.basicConfig(filename='security.log',level=logging.INFO)

def log(message):
    logging.info(message)