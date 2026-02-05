from playwright.sync_api import Page, Locator, expect
import logging

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger(__name__)

    def navigate(self, url):
        self.logger.info(f"Navigating to: {url}")
        self.page.goto(url)

    def click(self, selector):
        self.logger.info(f"Clicking element: {selector}")
        self.page.click(selector)

    def fill(self, selector, text):
        self.logger.info(f"Filling {selector} with: {text}")
        self.page.fill(selector, text)

    def get_text(self, selector):
        self.logger.info(f"Getting text from: {selector}")
        return self.page.text_content(selector)

    def is_visible(self, selector):
        return self.page.is_visible(selector)
    
    def wait_for_url(self, url_fragment):
         self.page.wait_for_url(f"**{url_fragment}**")
