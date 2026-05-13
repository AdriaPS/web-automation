from turtle import isvisible
from Utility.encryption_helper import EncryptHelper

class Login:
    def __init__(self, page, base_url, logger):
        self.page = page
        self.base_url = base_url
        self.logger = logger
        
        self.logger.info("Login constructor")
    
    # Function to open the login page.
    def open(self):
        self.page.goto(self.base_url)
     
    # Function to do the login on the login page.
    def do_login(self, user, private_key):
        # First get the "Sign in" button and click it if exists.
        sign_in_button = self.page.get_by_role("link", name="Sign in")
        if sign_in_button.is_visible():
            sign_in_button.click()
        
        # Fill the name and password fields with the information from the .txt file.
        self.page.locator('input[name="email"]').fill(user["username"])
        
        # Decrypt the password and delete the password stored in memory.
        password = EncryptHelper.decrypt_password(user["password"], private_key)
        try:
            self.page.locator('input[name="password"]').fill(password)
        finally:
            del password
        
        # Get the "Log in" button and click it if exists.
        log_in_button = self.page.locator("button[type='submit']")
        if log_in_button.is_visible():
            log_in_button.click()
        
        # Finally if a new window with an "Authorize" button appears, click it (checking for a possible doble authentication).
        try:
            authorize_btn = self.page.get_by_role("button", name="Authorize")
            if authorize_btn.is_visible(timeout=2000):
                authorize_btn.click()
        except:
            pass
        
        self.page.wait_for_timeout(200)
        
        # Log the information on the log file.
        self.logger.info("Logged in as %s", user["username"])