import time

from Pages.login_page import LoginPage

def test_login_with_valid_user(browser):
    page = browser.new_page()

    login_page = LoginPage(page)

    login_page.navigateTo()
    login_page.input_username('standard_user')
    login_page.input_password('secret_sauce')
    login_page.click_login()


