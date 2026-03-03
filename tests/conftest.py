import os
import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def page():
    """Setup and teardown for the Playwright page instance."""
    # Check if we are running in GitHub Actions (CI=true)
    # If CI is true, run headless. If we are local, run headed!
    is_ci = os.getenv("CI") == "true"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=is_ci)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture
def login_page(page):
    """Fixture to provide a LoginPage instance to tests."""
    return LoginPage(page)
