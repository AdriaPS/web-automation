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
    # Base Config to use on the code, set up as Headless false to be able to track what the robot is doing.
    # This could have also been done using a .txt file to get the config so it's more escalable, right now for testing
    # purposes, it's more efficient to do as this.
    config = BaseConfig(
        base_url="https://secretlair.wizards.com/eu/product/1250430/secret-lair-x-my-little-pony-friendship-is-magic-foil-edition",
        user_data_file=Path("userData.txt"),
        headless=False,
        guest=True,
    )
    
    # Utility variables such as the Browser (in this case Playwright), the Logger or the EncryptionHelper.
    browser = Browser(headless=config.headless)
    page = browser.page
    logger = get_logger("encrypt", Path("encrypt.log"))
    encrypt_helper = EncryptHelper(logger)
    
    # Generate logger for user and get the data from the .txt file.
    logger = get_logger("user", Path("user.log"))
    user_service = UserService(logger, config.user_data_file)
    user = user_service.get_user_data()
    priv_key_path=Path(r"RSA_Keys\private_key.pem")

    # Domain    
    # Login Page
    logger = get_logger("login", Path("login.log"))
    # Uncomment the login_page code lines if you want to test the login of the automation robot.
    # login_page = Login(page, config.base_url, logger)
    # login_page.open()
    
    # It's still needed the priv_key to the purchase_page if we want to log in instead of being a Guest.
    priv_key = encrypt_helper.get_priv_key_from_path(priv_key_path)
    # login_page.do_login(user[0], priv_key)
    
    # Purchase Page
    # Here I just send the user[0] cause we just want to be able to log in with 1 user, doesn't need to have multiple 
    # users.
    logger = get_logger("purchase", Path("purchase.log"))
    purchase_page = Purchase(page, logger)    
    purchase_page.buy_product(config.base_url, user[0], priv_key, config.guest)
    
    # I want to keep working on the page when the robot has finished the process, so I just pause the Playwright instead 
    # of .quit().
    page.pause()
    
    logger = get_logger("main", Path("main.log"))
    logger.info("Ended Web Automation process!")

if __name__ == "__main__":
    main()