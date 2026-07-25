"""Hands-On 4 """

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

PLAYGROUND_URL = "https://www.lambdatest.com/selenium-playground/"


# ---------------------------------------------------------------------------
# Task 1, Step 25-27: minimal script + implicit wait + headless mode
# ---------------------------------------------------------------------------
def basic_launch_and_title(headless: bool = False) -> str:
    """Open Chrome, navigate to the Playground, print & return the page title."""
    options = Options()
    if headless:
        # Step 27: run without a visible browser window
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1280,800")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                               options=options)
    try:
        # Step 26: implicit wait tells the driver to poll for up to N seconds
        # whenever it looks for an element before raising NoSuchElementException.
        #
        # This is considered bad practice as a *global* setting because it
        # applies uniformly to every find_element call in the session, even
        # ones that don't need to wait at all - this can silently slow down
        # tests and, worse, mixing implicit waits with explicit WebDriverWait
        # calls (Hands-On 5) causes unpredictable, hard-to-debug timing
        # behavior. Explicit waits let each wait be tailored to the specific
        # condition being waited for.
        driver.implicitly_wait(10)

        driver.get(PLAYGROUND_URL)
        title = driver.title
        print(f"Page title: {title}")
        return title
    finally:
        driver.quit()


# ---------------------------------------------------------------------------
# Task 2, Step 28: navigation + URL assertion + back()
# ---------------------------------------------------------------------------
def navigate_to_simple_form_and_back():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(PLAYGROUND_URL)
        driver.implicitly_wait(10)

        link = driver.find_element("link text", "Simple Form Demo")
        link.click()

        assert "simple-form-demo" in driver.current_url, (
            f"Expected 'simple-form-demo' in URL but got: {driver.current_url}"
        )
        print(f"Navigated correctly to: {driver.current_url}")

        driver.back()
        print(f"Navigated back to: {driver.current_url}")
    finally:
        driver.quit()


# ---------------------------------------------------------------------------
# Task 2, Steps 29-31: multi-window handling + screenshot + window sizing
# ---------------------------------------------------------------------------
def multi_window_and_screenshot():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(PLAYGROUND_URL)

        # Step 29: open a new tab via JS and switch to it
        driver.execute_script('window.open("https://www.google.com");')
        all_handles = driver.window_handles
        print(f"Open tabs: {len(all_handles)}")

        driver.switch_to.window(all_handles[1])
        print(f"Second tab title: {driver.title}")

        # Step 30: switch back to the original tab and take a screenshot
        driver.switch_to.window(all_handles[0])
        driver.save_screenshot("playground_screenshot.png")
        print("Screenshot saved to playground_screenshot.png")

        # Step 31: window sizing
        # Consistent window size matters because responsive web UIs render
        # different layouts (and sometimes different DOM elements, e.g.
        # a hamburger menu vs. a full navbar) at different viewport widths.
        # An inconsistent window size across test runs can make locators
        # unreliable and produce flaky failures unrelated to real bugs.
        size = driver.get_window_size()
        print(f"Current window size: {size}")
        driver.set_window_size(1280, 800)
        print(f"Resized window to: {driver.get_window_size()}")
    finally:
        driver.quit()


if __name__ == "__main__":
    basic_launch_and_title(headless=False)
    basic_launch_and_title(headless=True)
    navigate_to_simple_form_and_back()
    multi_window_and_screenshot()
