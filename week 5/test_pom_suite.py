"""Hands-On 7"""
from pages.simple_form_page import SimpleFormPage
from pages.checkbox_page import CheckboxPage
from pages.dropdown_page import DropdownPage
from pages.input_form_page import InputFormPage


def test_simple_form_submission(driver, base_url):
    page = SimpleFormPage(driver)
    page.navigate_to(base_url + "simple-form-demo/")
    page.enter_message("Hello Selenium")
    page.click_submit()
    assert page.get_displayed_message() == "Hello Selenium"


def test_checkbox_demo(driver, base_url):
    page = CheckboxPage(driver)
    page.navigate_to(base_url + "checkbox-demo/")
    page.check_option(0)
    assert page.is_option_checked(0) is True
    page.uncheck_option(0)
    assert page.is_option_checked(0) is False


def test_dropdown_selection(driver, base_url):
    page = DropdownPage(driver)
    page.navigate_to(base_url + "select-dropdown-demo/")
    page.select_day("Wednesday")
    assert page.get_selected_day() == "Wednesday"


def test_input_form_submit(driver, base_url):
    page = InputFormPage(driver)
    page.navigate_to(base_url + "input-form-demo/")
    page.fill_form(
        name="Jane Doe",
        email="jane.doe@example.com",
        phone="9876543210",
        address="123 Main Street",
    )
    page.submit_form()
    assert "success" in page.get_success_message().lower()


# Step 59 - maintenance comment:
# If the Submit button's ID changed from 'submit' to 'btn-submit' in a FLAT
# (non-POM) script, every single test file that contains a hardcoded
# driver.find_element(By.ID, 'submit') call would break, and each one would
# need to be located and edited individually - easy to miss one and leave a
# silent failure in the suite.
#
# With POM, the locator exists in exactly ONE place: the SUBMIT_BUTTON tuple
# inside the relevant page class (e.g., InputFormPage.SUBMIT_BUTTON). Updating
# that single class-level constant instantly fixes every test that uses
# page.submit_form(), because they all call through the same page method
# rather than duplicating the locator.
