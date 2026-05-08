import logging
import Logic as logic

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename='main.log', level=logging.INFO)
    logger.info('Start web automation')
    logic.startChrome
    logger.info('Web automation finished')

if __name__ == '__main__':
    main()