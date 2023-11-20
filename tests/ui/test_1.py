import re
import playwright
from playwright.sync_api import Playwright, sync_playwright, expect
from pom.input_form_page import TestInputFormPage


def test_simple_form_demo(set_up):
    # 1. Open LambdaTest's Selenium Playground
    # 2. Click "Simple Form Demo" under Input Forms
    page = set_up
    page.click("text=Simple Form Demo")

    # 3. Validate that the URL contains "simple-form-demo"
    expect(page).to_have_url(re.compile(".*simple-form-demo"))

    # 4. Create a variable for a string value "Welcome to LambdaTest"
    message = "Welcome to LambdaTest"

    # 5. Use this variable to enter values in the "Enter Message" text box
    page.fill("#user-message", message)
    page.wait_for_load_state("networkidle")

    # 6. Click "Get Checked Value"
    page.click("text=Get Checked Value")
    page.wait_for_load_state("networkidle")

    # 7. Validate whether the same text message is displayed in the right-hand panel
    # under the "Your Message:" section
    expect(page.locator("#user-message").nth(1)).to_contain_text(message)


def test_drag_drop_sliders(set_up):
    # Step 1: Open the LambdaTest Selenium Playground page and click "Drag & Drop Sliders"
    page = set_up
    page.click("text=Drag & Drop Sliders")
    page.wait_for_load_state("networkidle")

    # Step 2: Select the slider "Default value 15" and drag it to make it 95
    slider = page.locator('div[id="slider3"] input[type="range"]')
    slider_value = page.locator('div[id="slider3"] output[id="rangeSuccess"]')
    slider.hover()
    page.mouse.down()
    target_slider_value = 93  # because mouse down and mouse up give +1 click
    target_x = slider.bounding_box()["x"] + slider.bounding_box()["width"] * target_slider_value / 100
    target_y = slider.bounding_box()["y"] + slider.bounding_box()["height"] / 2
    page.mouse.move(target_x, target_y)
    page.mouse.up()
    page.wait_for_load_state("networkidle")
    range_value = slider_value.inner_text()
    assert range_value == "95"

def test_input_form_submit(set_up):
    # 1. Open LambdaTest's Selenium Playground
    # click “Input Form Submit” under “Input Forms”.
    page = set_up
    page.click("text=Input Form Submit")

    # 2. Click “Submit” without filling in any information in the form.
    page.click('text=Submit')

    # 3. Assert “Please fill in the fields” error message.
    error_message = page.locator('input#name[required]')
    assert error_message.is_visible()

    # 4. Fill in Name, Email, and other fields.
    # 5. From the Country drop-down, select “United States” using the text property.
    # 6. Fill all fields and click “Submit”.
    input_page = TestInputFormPage(page)
    input_page.submit_form("Tanya", "test@gmail.com", "qwerty123", "Google",
                               "google.com","United States", "Texas", "123",
                               "Liberty street", "TX", "77494")
    page.click('text=Submit')

    # 7. Once submitted, validate the success message “Thanks for contacting
    # us, we will get back to you shortly.” on the screen.
    page.wait_for_load_state("networkidle")
    locator = page.locator('.success-msg')
    expect(locator).to_contain_text("Thanks for contacting us, we will get back to you shortly")

    