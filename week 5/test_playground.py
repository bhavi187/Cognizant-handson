"""Hands-On 6"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


# Step 45: parameterised form submission test
@pytest.mark.parametrize("message", ["Hello", "Selenium Automation", "12345"])
def test_simple_form_submission(driver, base_url, message):
    driver.get(base_url + "simple-form-demo/")

    message_input = driver.find_element(By.ID, "user-message")
    message_input.send_keys(message)
    driver.find_element(By.CSS_SELECTOR, "#showInput button").click()

    displayed = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )
    assert displayed.text == message


def test_checkbox_demo(driver, base_url):
    driver.get(base_url + "checkbox-demo/")

    first_checkbox = driver.find_element(By.CSS_SELECTOR, "#isAgeSelected")
    first_checkbox.click()
    assert first_checkbox.is_selected() is True

    first_checkbox.click()
    assert first_checkbox.is_selected() is False


def test_dropdown_selection(driver, base_url):
    driver.get(base_url + "select-dropdown-demo/")

    dropdown_element = driver.find_element(By.ID, "select-demo")
    select = Select(dropdown_element)
    select.select_by_visible_text("Wednesday")

    selected_option = select.first_selected_option
    assert selected_option.text == "Wednesday"
