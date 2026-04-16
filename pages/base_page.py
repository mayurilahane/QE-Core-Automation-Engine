from utils.decorators import retry
# Task: Create a BasePage class with common methods (like click_element or get_text) and then create a LoginPage class that inherits from it.
class BasePage:
    def __init__(self, page):
        self.page = page
    
    @retry(retries=3, delay=2)
    def click_element(self, locator):
        locator.click()

    def navigate(self, url):
        self.page.goto(url)

    def enter_text(self, locator, text):
        locator.fill(text)
