import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestNegativeScenario:

    @pytest.mark.invaliduser
    def test_negative_username(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student2")

        # Type password Password123 into Password field

        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        time.sleep(5)
        # Pouch Submit button

        submitbutton_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submitbutton_locator.click()

        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message not displayed but it should"

        err_message = error_message_locator.text
        assert err_message == "Your username is invalid!", "error message should be 'Your user name is invalid!'"
