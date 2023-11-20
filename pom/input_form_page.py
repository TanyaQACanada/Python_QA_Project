# Description: Page Object Model for Input Form page
# from playwright.sync_api import sync_playwright, Page


class TestInputFormPage:
    def __init__(self, page):
        self.page = page

    # def navigate(self):
    #     self.page.goto("https://www.lambdatest.com/selenium-playground")

    def submit_form(self, name, email, password, company, website, country, city, address1, address2, state, zipcode):
        self.page.fill("[placeholder=\"Name\"]", name)
        self.page.fill("[placeholder=\"Email\"]", email)
        self.page.fill("[placeholder=\"Password\"]", password)
        self.page.fill("[placeholder=\"Company\"]", company)
        self.page.fill("[placeholder=\"Website\"]", website)
        country_selector = 'select[name="country"]'
        self.page.select_option(country_selector, label=country)
        self.page.fill("[placeholder=\"City\"]", city)
        self.page.fill("[placeholder=\"Address 1\"]", address1)
        self.page.fill("[placeholder=\"Address 2\"]", address2)
        self.page.fill("[placeholder=\"State\"]", state)
        self.page.fill("[placeholder=\"Zip code\"]", zipcode)
