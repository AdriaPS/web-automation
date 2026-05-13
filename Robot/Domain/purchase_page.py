from Domain.login_page import Login
from pathlib import Path
from Utility.logger import get_logger

class Purchase:
    def __init__(self, page, logger):
        self.page = page        
        self.logger = logger
        
        self.logger.info("Purchase constructor")
      
    # Function to realize the buy of a product.
    def buy_product(self, base_url, user, priv_key, guest):
        self.page.goto(f"{base_url}")
        
        # If the button is pre-order or order, it clicks the correct one.
        preorder_btn = self.page.locator("#product_editions_buy_button").get_by_role("button", name="Pre-order now")
        order_btn = self.page.locator("#product_editions_buy_button").get_by_role("button", name="Order now")

        if preorder_btn.is_visible():
            preorder_btn.click()
        elif order_btn.is_visible():
            order_btn.click()
            
        # Then when the popup to go to the Cart appears, it clicks the proper button.    
        self.page.locator("[data-internal-id='modal-submit']").click()
        
        # Then click the "Go Cart" button if the purchase want's to be done as Guest (Guest but instead of 
        # buy with an account). If not, do log-in process.
        self.logger.info(f"Want to do the purchase as guest: {guest}")
        if guest:
            self.page.locator("button.btn.btn_reverse[aria-label='Continue as guest']").click()
        else:
            self.page.locator("a[aria-label='Log in / Sign up']").click()
            logger = get_logger("login", Path("login.log"))
            login_page = Login(self.page, base_url, self.logger)
            login_page.do_login(user, priv_key)
            
        self.logger.info(f"Purchase made successfully by user {user["username"]}")