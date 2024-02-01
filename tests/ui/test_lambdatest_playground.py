import re
import playwright
from playwright.sync_api import Playwright, sync_playwright, expect
from input_form_page import TestInputFormPage
import time

# the first 3 test cases were written by me as part of the training for lambdatest certification

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

def test_js_alerts_1(set_up):
    page = set_up
    page.click("text=Javascript Alerts")
    page.wait_for_load_state("networkidle")
    page.on("dialog", lambda dialog: dialog.accept())
    page.locator("p").filter(has_text="JavaScript AlertsClick Me").get_by_role("button").click()
  #  need to add some assertion

def test_js_alerts_2(set_up):
    page = set_up
    page.click("text=Javascript Alerts")
    page.once("dialog", lambda dialog: dialog.accept())
    page.locator("p").filter(has_text="Confirm box:Click Me").get_by_role("button").click()
    page.wait_for_load_state("networkidle")  
    expect(page.locator("//p[@id='confirm-demo']").filter(has_text="You pressed OK!")).to_be_visible()
  

def test_js_alerts_3(set_up):
    page = set_up
    page.click("text=Javascript Alerts")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.locator("p").filter(has_text="Confirm box:Click Me").get_by_role("button").click()  
    page.wait_for_load_state("networkidle")  
    expect(page.locator("//p[@id='confirm-demo']").filter(has_text="You pressed CANCEL!")).to_be_visible()
    

def test_js_alerts_4(set_up):
    page = set_up
    page.click("text=Javascript Alerts")
    page.wait_for_load_state("networkidle")
    dialog_message = "test"
    page.on("dialog", lambda dialog: dialog.accept(prompt_text=f"{dialog_message}"))
    page.locator("p").filter(has_text="Prompt box:Click Me").get_by_role("button").click()
    expect(page.locator("p").filter(has_text=f"You have entered '{dialog_message}'  !")).to_be_visible()

def test_js_alerts_5(set_up):
    page = set_up
    page.click("text=Javascript Alerts")
    page.wait_for_load_state("networkidle")
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.locator("p").filter(has_text="Prompt box:Click Me").get_by_role("button").click()
  #  need to add some assertion

def test_jquery_dropdown_1(set_up):
    page = set_up
    # select country in frist dropdown
    page.click("text=JQuery Select dropdown")
    page.get_by_text("Drop Down with SearchSelect Country :").click()
    page.get_by_label("", exact=True).locator("b").click()
    page.get_by_role("treeitem", name="Denmark").click()
    expect(page.locator("//span[@id='select2-country-container']").filter(has_text="Denmark")).to_be_visible()
    # prompt country in first dropdown
    page.get_by_title("Denmark").click()
    page.get_by_role("textbox").nth(1).fill("ba")
    page.get_by_role("textbox").nth(1).press("Enter")
    page.get_by_title("Bangladesh").click()
    expect(page.locator("//span[@id='select2-country-container']").filter(has_text="Bangladesh")).to_be_visible()

def test_jquery_dropdown_2(set_up):
    page = set_up
    page.click("text=JQuery Select dropdown")
    # select multiple values with search
    page.get_by_text("Select Multiple Values with search").click()
    page.get_by_placeholder("Select state(s)").click()
    page.get_by_role("treeitem", name="Alaska").click()
    page.locator("ul").filter(has_text="×Alaska").click()
    page.get_by_role("treeitem", name="Arizona").click()
    page.get_by_text("×Alaska×Arizona").click()
    page.get_by_role("treeitem", name="Arkansas").click()
    page.get_by_text("×Alaska×Arizona×Arkansas").click()
    page.get_by_role("treeitem", name="Arkansas").click()
    expect(page.locator("ul").filter(has_text="×Alaska×Arizona")).to_be_visible()
    expect(page.locator("//div[@class='wrapper']//div[2]//div[2]").filter(has_text="×Arkansas")).to_be_hidden()
  
def test_jquery_dropdown_3(set_up):
    page = set_up
    page.click("text=JQuery Select dropdown")
    page.get_by_label("Puerto Rico").locator("b").click()
    page.get_by_role("treeitem", name="American Samoa").click()
    page.get_by_label("American Samoa").locator("span").nth(1).click()
    page.get_by_role("textbox").nth(1).fill("Guam")
    page.get_by_role("textbox").nth(1).press("ArrowDown")
    page.get_by_role("textbox").nth(1).press("ArrowDown")
    page.get_by_text("Select Country :Puerto RicoAmerican SamoaGuamNorthern Mariana IslandsUnited Stat").click()
    expect(page.locator("//div[@class='wrapper']//div[3]//div[2]").filter(has_text="American Samoa")).to_be_visible()

def test_jquery_dropdown_4(set_up):
    page = set_up
    page.click("text=JQuery Select dropdown")
    page.get_by_label("Select a file").locator("(//select[@id='files'])[1]").click()
    page.get_by_label("Select a file").select_option(value="Python")
    expect(page.locator("//select[@id='files']").filter(has_text="Python")).to_be_visible()
    page.get_by_label("Select a file").select_option(value="Ruby")
    expect(page.locator("//select[@id='files']").filter(has_text="Ruby")).to_be_visible()
    page.get_by_label("Select a file").select_option(value="C")
    expect(page.locator("//select[@id='files']").filter(has_text="C")).to_be_visible()
    page.get_by_label("Select a file").select_option(value="Unknown Script")
    expect(page.locator("//select[@id='files']").filter(has_text="Unknown Script")).to_be_visible()


def test_bootstrap_progress_bar_dialog_demo_1(set_up):
  page = set_up
  page.click("text=Progress Bar Modal")
  page.get_by_role("button", name="Show dialog (Autoclose after 2 seconds)").click()
  page.wait_for_selector('.progress-bar')
  page.wait_for_timeout(3000)
  expect(page.get_by_text("Loading")).to_be_hidden()
 
def test_bootstrap_progress_bar_dialog_demo_2(set_up):
  page = set_up
  page.click("text=Progress Bar Modal")
  page.get_by_role("button", name="Show dialog (Autoclose after 3 seconds)").click()
  page.wait_for_selector('.progress-bar')
  page.wait_for_timeout(4000)
  expect(page.get_by_text("Custom message")).to_be_hidden()
 
def test_bootstrap_progress_bar_dialog_demo_3(set_up):
  page = set_up
  page.click("text=Progress Bar Modal")
  page.get_by_role("button", name="Show dialog (Autoclose after 5 seconds)").click()
  page.wait_for_selector('.progress-bar')
  page.wait_for_timeout(6000)
  expect(page.get_by_text("Hello Mr. Alert !")).to_be_hidden()

