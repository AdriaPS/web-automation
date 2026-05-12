from playwright.sync_api import sync_playwright

class Browser:
    def __init__(self, headless: bool):
        self.playwright = sync_playwright().start()
        
        self.browser = self.playwright.chromium.launch(
            headless=headless,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-dev-shm-usage",
                "--no-sandbox",
            ]
        )

        # Stealth-like context
        self.context = self.browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800},
            java_script_enabled=True,
        )

        self.page = self.context.new_page()

        # Remove navigator.webdriver
        self.page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
        """)

    def get(self, url: str):
        self.page.goto(url)

    def quit(self):
        self.browser.close()
        self.playwright.stop()