from playwright.sync_api import expect

def test_successful_login(login_page):
    """Verify that a standard user can log in successfully."""
    # 1. Action: Perform the login using the POM method
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    
    # 2. Assertion: Verify the landing page URL or a unique element
    # We keep assertions in the test file, not the Page Object
    expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")
    
def test_invalid_login(login_page):
    """Verify that an error message is displayed for invalid credentials."""
    login_page.load()
    login_page.login("locked_out_user", "wrong_password")
    
    # Check for the specific error message locator
    error_message = login_page.page.locator("[data-test='error']")
    expect(error_message).to_be_visible()
