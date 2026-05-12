from Domain.login_page import Login

class Purchase:
    def __init__(self, page, logger):
        self.page = page        
        self.logger = logger
        
        self.logger.info("Purchase constructor")
        
    def buy_product(self, base_url, user, priv_key):
        self.page.goto(f"{base_url}")        
        self.page.locator("#product_editions_buy_button").get_by_role("button", name="Pre-order now").click()
        self.page.locator("[data-internal-id='modal-submit']").click()
        self.page.locator("button[ng-click='goCart()']").click()