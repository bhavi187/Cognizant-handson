"""Hands-On 6 """
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Step 48: session-scoped base_url fixture
@pytest.fixture(scope="session")
def base_url():
    return "https://www.lambdatest.com/selenium-playground/"


# Step 41: function-scoped driver fixture (fresh browser per test = isolation)
@pytest.fixture(scope="function")
def driver():
    drv = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    drv.maximize_window()
    yield drv          # -------- setup above, teardown below --------
    drv.quit()


# Step 46: screenshot on failure hook
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver_fixture = item.funcargs.get("driver")
        if driver_fixture is not None:
            test_name = item.name.replace("/", "_")
            screenshot_path = f"{test_name}_failure.png"
            driver_fixture.save_screenshot(screenshot_path)
            print(f"\nFailure screenshot saved: {screenshot_path}")
