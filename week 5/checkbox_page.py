"""Hands-On 7"""
from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckboxPage(BasePage):
    CHECKBOX_LIST = (By.CSS_SELECTOR, "ul#colorbox li input[type='checkbox']")

    def _checkbox(self, index: int):
        checkboxes = self.driver.find_elements(*self.CHECKBOX_LIST)
        return checkboxes[index]

    def check_option(self, index: int):
        box = self._checkbox(index)
        if not box.is_selected():
            box.click()

    def uncheck_option(self, index: int):
        box = self._checkbox(index)
        if box.is_selected():
            box.click()

    def is_option_checked(self, index: int) -> bool:
        return self._checkbox(index).is_selected()
