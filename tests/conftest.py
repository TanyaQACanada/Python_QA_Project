import playwright
import pytest
from playwright.sync_api import sync_playwright, Playwright, Page


@pytest.fixture(scope="session")
def set_up(playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.lambdatest.com/selenium-playground")
    

    yield page
    page.close()

