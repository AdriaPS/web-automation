class Purchase:
    def __init__(self, browser, logger):
        self.browser = browser
        self.logger = logger
        
        self.logger.info("Purchase constructor")