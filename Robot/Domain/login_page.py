from Utility.encryption_helper import EncryptHelper

class Login:
    def __init__(self, page, base_url, logger):
        self.page = page
        self.base_url = base_url
        self.logger = logger
        
        self.logger.info("Login constructor")
        
    def open(self):
        self.page.goto(self.base_url)
        
    def do_login(self, user, private_key):
        self.page.get_by_role("link", name="Sign in").click()
        
        self.page.locator('input[name="email"]').fill(user["username"])        
        password = EncryptHelper.decrypt_password(user["password"], private_key)
        try:
            self.page.locator('input[name="password"]').fill(password)
        finally:
            del password
        
        self.page.locator("button[type='submit']").click()
        
        try:
            # Wait briefly to see if the authorize button appears
            authorize_btn = self.page.get_by_role("button", name="Authorize")
            if authorize_btn.is_visible(timeout=2000):
                authorize_btn.click()
        except:
            pass
        
        self.page.wait_for_timeout(200)  # small delay to allow redirect

        #while True:
        #    url = self.page.url
        #    if "https://secretlair.wizards.com/eu" in url or "https://secretlair.wizards.com/eu#" in url or "https://secretlair.wizards.com/eu/" in url:
        #        break
        #    self.page.wait_for_timeout(100)
                                      
        self.logger.info("Logged in as %s", user["username"])