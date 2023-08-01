from Utils.helpers import *

def test_login_with_valid_user(browser):
    page = browser.new_page()

    page.goto('https://www.saucedemo.com/v1/')
    ele = locate_all_xpath(page, '//aaaaaah4')

    if ele:
        print(ele, 'items found')
    else:
        print(ele)
        pytest.fail('items did not found!')
