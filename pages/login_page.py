from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # define locators as attribute
        self.url = "https://www.saucedemo.com/"
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"

    def load(self):
        self.navigate(self.url)

    def login(self, user, pwd):
        # Use methods from BasePage
        self.enter_text(self.username_input, user)
        self.enter_text(self.password_input, pwd)
        self.click_element(self.login_button)