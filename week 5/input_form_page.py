"""Hands-On 7 """
from selenium.webdriver.common.by import By
from .base_page import BasePage


class InputFormPage(BasePage):
    NAME_FIELD = (By.NAME, "name")
    EMAIL_FIELD = (By.NAME, "email")
    PHONE_FIELD = (By.NAME, "phone")
    ADDRESS_FIELD = (By.NAME, "address")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".success-msg, .alert-success")

    def fill_form(self, name: str, email: str, phone: str, address: str):
        self.wait_for_element(self.NAME_FIELD).send_keys(name)
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone)
        self.driver.find_element(*self.ADDRESS_FIELD).send_keys(address)

    def submit_form(self):
        self.wait_for_clickable(self.SUBMIT_BUTTON).click()

    def get_success_message(self) -> str:
        return self.wait_for_element(self.SUCCESS_MESSAGE).text
