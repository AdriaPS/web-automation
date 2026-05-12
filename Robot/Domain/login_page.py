class Login:
    def __init__(self, browser, logger):
        self.browser = browser
        self.logger = logger
        
        self.logger.info("Login constructor")