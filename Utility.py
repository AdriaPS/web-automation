from pathlib import Path
import logging

LOG_DIR = Path("Logs")
LOG_DIR.mkdir(exist_ok=True)

def get_logger(name: str, filename: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(LOG_DIR / filename)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)

    if not logger.handlers:  # avoid duplicate handlers
        logger.addHandler(file_handler)

    return logger