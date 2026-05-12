from pathlib import Path
from config import BaseConfig
from Utility.browser import Browser
from Utility.logger import get_logger
from Utility.user_service import UserService
from Domain.login_page import Login
from Domain.purchase_page import Purchase

def main():
    logger = get_logger("main", Path("main.log"))
    logger.info("Started Web Automation process!")
    # Config
    config = BaseConfig(
        base_url="https://shop.example.com",
        user_data_file=Path("userData.txt"),
        headless=False,
    )
    
    # Utility
    browser = Browser(headless=config.headless)
    
    # Generate logger
    logger = get_logger("user", Path("user.log"))
    user_service = UserService(logger, config.user_data_file)

    # Domain
    logger = get_logger("login", Path("login.log"))
    login_page = Login(browser, logger)
    logger = get_logger("purchase", Path("purchase.log"))
    purchase_page = Purchase(browser, logger)
        
    browser.quit()
    
    logger = get_logger("main", Path("main.log"))
    logger.info("Ended Web Automation process!")

if __name__ == "__main__":
    main()