import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption('--driver', action='store', default='chrome')
    parser.addoption('--headless', action='store', default=False)


@pytest.fixture
def driver(request):
    driver_name = request.config.getoption('--driver')

    with sync_playwright() as p:
        if driver_name == 'chrome':
            driver = p.chromium.launch(headless=request.config.getoption('--headless'))

        if driver_name == 'firefox':
            driver = p.firefox.launch(headless=request.config.getoption('--headless'))

        if driver_name == 'webkit':
            driver = p.webkit.launch(headless=request.config.getoption('--headless'))

        yield driver

        driver.close()
