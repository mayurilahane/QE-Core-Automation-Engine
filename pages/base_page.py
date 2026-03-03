# Task: Create a BasePage class with common methods (like click_element or get_text) and then create a LoginPage class that inherits from it.
class BasePage:
    def __init__(self, page):
        self.page = page
    
    def click_element(self, locator):
        self.page.click(locator)

    def navigate(self, url):
        self.page.goto(url)

    def enter_text(self, locator, text):
        self.page.fill(locator, text)
