# open browser
# go to web page
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestPositiveScenarios:

    @pytest.mark.login
    def test_positive_login(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        time.sleep(5)

        # Go to web page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type password Password123 into Password field

        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # Pouch Submit button

        submitbutton_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submitbutton_locator.click()

        time.sleep(2)

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        actual_url = driver.current_url

        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        text_locator = driver.find_element(By.TAG_NAME, "h1")
        actual_text = text_locator.text

        assert actual_text == "Logged In Successfully"

        # Verify button Log out is displayed on the new page

        logout_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
        assert logout_button_locator.is_displayed()
