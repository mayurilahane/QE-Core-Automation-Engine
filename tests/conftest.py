import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def page():
    """Setup and teardown for the Playwright page instance."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # Headless=False to see the action
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture
def login_page(page):
    """Fixture to provide a LoginPage instance to tests."""
    return LoginPage(page)