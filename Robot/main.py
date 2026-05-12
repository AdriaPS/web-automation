from pathlib import Path
from config import BaseConfig
from Utility.browser import Browser
from Utility.encryption_helper import EncryptHelper
from Utility.logger import get_logger
from Utility.user_service import UserService
from Domain.login_page import Login
from Domain.purchase_page import Purchase

def main():
    logger = get_logger("main", Path("main.log"))
    logger.info("Started Web Automation process!")
    # Config
    config = BaseConfig(
        base_url="https://secretlair.wizards.com/eu/product/1250430/secret-lair-x-my-little-pony-friendship-is-magic-foil-edition",
        user_data_file=Path("userData.txt"),
        headless=False,
    )
    
    # Utility
    browser = Browser(headless=config.headless)
    page = browser.page
    logger = get_logger("encrypt", Path("encrypt.log"))
    encrypt_helper = EncryptHelper(logger)
    
    # Generate logger
    logger = get_logger("user", Path("user.log"))
    user_service = UserService(logger, config.user_data_file)
    user = user_service.get_user_data()
    priv_key_path=Path(r"RSA_Keys\private_key.pem")

    # Domain    
    # Login Page
    logger = get_logger("login", Path("login.log"))
    # login_page = Login(page, config.base_url, logger)
    # login_page.open()
    
    priv_key = encrypt_helper.get_priv_key_from_path(priv_key_path)
    # login_page.do_login(user[0], priv_key)
    
    # Purchase Page
    logger = get_logger("purchase", Path("purchase.log"))
    purchase_page = Purchase(page, logger)    
    purchase_page.buy_product(config.base_url, user[0], priv_key)
    
    page.pause()
    
    logger = get_logger("main", Path("main.log"))
    logger.info("Ended Web Automation process!")

if __name__ == "__main__":
    main()