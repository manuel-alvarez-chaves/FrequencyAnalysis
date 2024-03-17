import logging

def create_logger(path_to_file):
    # Format
    formatter = logging.Formatter(
        "%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # File handler
    fh = logging.FileHandler(path_to_file)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    # Standard output
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)

    # Logger instance
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger