"""Handson 5"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as FluentWait
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

PLAYGROUND_URL = "https://www.lambdatest.com/selenium-playground/"


def get_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def all_locator_strategies():
    driver = get_driver()
    try:
        driver.get(PLAYGROUND_URL + "simple-form-demo/")

        by_id = driver.find_element(By.ID, "user-message")
        by_name = driver.find_element(By.NAME, "message")
        by_class = driver.find_element(By.CLASS_NAME, "form-control")
        by_tag = driver.find_element(By.TAG_NAME, "input")
        by_xpath_abs = driver.find_element(
            By.XPATH, "/html/body/div[3]/div/div[2]/div/div[1]/div[2]/form/div/input"
        )
        by_xpath_rel = driver.find_element(By.XPATH, "//input[@id='user-message']")

        by_css_id = driver.find_element(By.CSS_SELECTOR, "#user-message")
        by_css_attr = driver.find_element(By.CSS_SELECTOR, "[name='message']")
        by_css_parent_child = driver.find_element(By.CSS_SELECTOR, "div.form-group > input")

        for name, el in [
            ("By.ID", by_id), ("By.NAME", by_name), ("By.CLASS_NAME", by_class),
            ("By.TAG_NAME", by_tag), ("XPath absolute", by_xpath_abs),
            ("XPath relative", by_xpath_rel), ("CSS #id", by_css_id),
            ("CSS [attr]", by_css_attr), ("CSS parent>child", by_css_parent_child),
        ]:
            assert el is not None
            print(f"{name}: found element tag={el.tag_name}")
    finally:
        driver.quit()

def checkbox_text_locators():
    driver = get_driver()
    try:
        driver.get(PLAYGROUND_URL + "checkbox-demo/")

        first_option = driver.find_element(By.XPATH, "//label[text()='Option 1']")
        print(f"Exact match label: {first_option.text}")

        all_options = driver.find_elements(By.XPATH, "//label[contains(text(),'Option')]")
        print(f"Found {len(all_options)} option labels via contains()")
    finally:
        driver.quit()


def bootstrap_alert_explicit_wait():
    driver = get_driver()
    try:
        driver.get(PLAYGROUND_URL + "bootstrap-alerts/")

        success_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "success-alert"))
        )
        success_button.click()

        alert_div = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
        )
        assert "successfully" in alert_div.text.lower()
        print(f"Alert text confirmed: {alert_div.text}")
    finally:
        driver.quit()


def sleep_vs_explicit_wait_timing():
    """Step 37: demonstrate why time.sleep() is worse than an explicit wait."""

    driver = get_driver()
    try:
        driver.get(PLAYGROUND_URL + "bootstrap-alerts/")
        start = time.time()
        driver.find_element(By.ID, "success-alert").click()
        time.sleep(3)  
        alert = driver.find_element(By.CSS_SELECTOR, ".alert-success")
        assert alert.is_displayed()
        sleep_duration = time.time() - start
        print(f"time.sleep() version took: {sleep_duration:.2f}s")
    finally:
        driver.quit()

    driver = get_driver()
    try:
        driver.get(PLAYGROUND_URL + "bootstrap-alerts/")
        start = time.time()
        driver.find_element(By.ID, "success-alert").click()
        alert = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
        )
        wait_duration = time.time() - start
        print(f"Explicit wait version took: {wait_duration:.2f}s")

        driver.quit()


def clickable_vs_visible_explanation():

    driver = get_driver()
    try:
        driver.get(PLAYGROUND_URL + "bootstrap-alerts/")
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "success-alert"))
        )
        button.click()
    finally:
        driver.quit()


def fluent_wait_for_table_row():
    driver = get_driver()
    try:
        driver.get(PLAYGROUND_URL + "table-sort-search-and-pagination-demo/")

        wait = FluentWait(
            driver,
            timeout=10,
            poll_frequency=0.5,
            ignored_exceptions=[NoSuchElementException],
        )
        row = wait.until(lambda d: d.find_element(By.CSS_SELECTOR, "table tbody tr"))
        print(f"First table row found: {row.text}")
    finally:
        driver.quit()


if __name__ == "__main__":
    all_locator_strategies()
    checkbox_text_locators()
    print(LOCATOR_RANKING)
    bootstrap_alert_explicit_wait()
    sleep_vs_explicit_wait_timing()
    clickable_vs_visible_explanation()
    fluent_wait_for_table_row()
