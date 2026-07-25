"""Hands-On 7 """
from selenium.webdriver.common.by import By
from .base_page import BasePage


class SimpleFormPage(BasePage):
    # Step 51: locators as class-level tuples - never hardcoded in methods
    MESSAGE_INPUT = (By.ID, "user-message")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#showInput button")
    DISPLAYED_MESSAGE = (By.ID, "message")

    def enter_message(self, text: str):
        field = self.wait_for_element(self.MESSAGE_INPUT)
        field.clear()
        field.send_keys(text)

    def click_submit(self):
        button = self.wait_for_clickable(self.SUBMIT_BUTTON)
        button.click()

    def get_displayed_message(self) -> str:
        # No assert statements in page methods - only actions/return values.
        element = self.wait_for_element(self.DISPLAYED_MESSAGE)
        return element.text
