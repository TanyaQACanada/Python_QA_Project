import playwright
import pytest
from playwright.sync_api import sync_playwright, Playwright, Page


@pytest.fixture()
def set_up(playwright: Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.lambdatest.com/selenium-playground")


    yield page
    browser.close()
