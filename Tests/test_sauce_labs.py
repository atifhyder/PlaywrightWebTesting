from playwright.sync_api import sync_playwright
import pytest


def test_sauceLabs():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/v1/")
