import logging
import Logic as logic
import Utility as utility
from pathlib import Path

logger = ""   

def main():
    logger = utility.get_logger("Main", "main.log")
    logger.info('Start web automation')
    logic.start_chrome_automation()
    logger.info('Web automation finished')

if __name__ == '__main__':
    main()